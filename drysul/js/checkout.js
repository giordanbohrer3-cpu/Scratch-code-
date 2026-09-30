/* Central de vendas — compra em 4 etapas: pedido → entrega → pagamento → pronto.
   DEMONSTRAÇÃO: nenhum pagamento é processado e nenhum dado sai do aparelho.
   Versão final: a etapa de pagamento pede ao servidor da loja uma cobrança (o servidor recalcula
   os preços pelo catálogo dele) e leva o cliente ao checkout seguro do provedor (Pix/cartão).
   A confirmação chega por webhook do provedor, nunca pelo navegador. */
(function () {
  'use strict';

  var A = window.DrysulApp, V = window.DrysulVendas, D = window.DRYSUL;
  if (!A || !V || !D) return;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var BRL = A.BRL, esc = A.esc, loja = D.loja;

  var dlg = $('#checkout'), form = $('#co-form');
  var secoes = $$('.co-step', form), marcas = $$('#co-steps li');
  var btNext = $('#co-next'), btBack = $('#co-back');
  var elLinhas = $('#co-lines'), elTotal = $('#co-total'), elNota = $('#co-total-note'), elRes = $('#co-result'), elHint = $('#co-pay-hint');
  var st = { etapa: 1, av: null, numero: null, pago: false };

  var NOMES_PAG = { pix: 'Pix', credito: 'Cartão de crédito', debito: 'Cartão de débito', whatsapp: 'Combinar no WhatsApp' };

  function valor(nome) { var el = form.elements[nome]; return el ? String(el.value || '').trim() : ''; }
  function entrega() { return valor('entrega') || 'retirada'; }
  function pagamento() { return valor('pagamento') || 'pix'; }

  /* ---------- abrir ---------- */
  function abrir(origem) {
    st.av = A.avaliacao();
    if (st.av.canal !== 'online') { A.toast('Este pedido segue pelo WhatsApp.'); A.abrirOrcamento(origem); return; }
    st.numero = null; st.pago = false;
    renderLinhas();
    irPara(1, false);
    A.abrirDialogo(dlg, origem);
  }

  function renderLinhas() {
    elLinhas.innerHTML = st.av.linhas.map(function (l) {
      var p = A.produto(l.id);
      return '<li class="co-line">' + A.ill(p.icone) +
        '<div><p class="co-line__n">' + esc(p.nome) + '</p><p class="co-line__m">' + esc(p.emb) + ' · ' + l.qtd + ' × ' + BRL.format(p.preco) + '</p></div>' +
        '<b>' + BRL.format(l.total) + '</b></li>';
    }).join('');
    elTotal.textContent = BRL.format(st.av.subtotal);
  }

  /* ---------- navegação entre etapas ---------- */
  function irPara(n, foco) {
    st.etapa = n;
    secoes.forEach(function (s) { s.hidden = Number(s.getAttribute('data-step')) !== n; });
    marcas.forEach(function (m) {
      var k = Number(m.getAttribute('data-s'));
      m.classList.toggle('is-done', k < n);
      if (k === n) m.setAttribute('aria-current', 'step'); else m.removeAttribute('aria-current');
    });
    if (n === 3) ajustarPagamento();
    atualizarRodape();
    form.scrollTop = 0;
    if (foco !== false) { var h = $('.co-h', secoes[n - 1]) || $('h3', secoes[n - 1]); if (h) h.focus({ preventScroll: true }); }
  }

  function atualizarRodape() {
    var e = entrega();
    elNota.textContent = e === 'entrega' ? '+ taxa de entrega a combinar' : 'Retirada na loja, sem custo';
    btBack.hidden = st.etapa === 1 || (st.etapa === 4 && (st.pago || pagamento() === 'whatsapp'));
    var rotulo = {
      1: 'Continuar',
      2: 'Ir para o pagamento',
      3: { pix: 'Gerar Pix', credito: 'Pagar com segurança', debito: 'Pagar com segurança', whatsapp: 'Enviar pedido no WhatsApp' }[pagamento()],
      4: st.pago || pagamento() === 'whatsapp' ? 'Concluir' : 'Simular pagamento aprovado'
    }[st.etapa];
    $('span', btNext).textContent = rotulo;
  }

  function ajustarPagamento() {
    var soWhats = entrega() === 'entrega';
    elHint.hidden = !soWhats;
    $$('input[name="pagamento"]', form).forEach(function (r) {
      r.disabled = soWhats && r.value !== 'whatsapp';
      r.closest('.opt').classList.toggle('is-disabled', r.disabled);
    });
    if (soWhats) form.elements.pagamento.value = 'whatsapp';
    else if (pagamento() === 'whatsapp' && !st.escolheuWhats) form.elements.pagamento.value = 'pix';
  }

  /* ---------- validação dos dados ---------- */
  function erro(input, msg) {
    var m = document.getElementById(input.getAttribute('aria-describedby'));
    if (msg) { input.setAttribute('aria-invalid', 'true'); m.textContent = msg; m.hidden = false; }
    else { input.removeAttribute('aria-invalid'); m.textContent = ''; m.hidden = true; }
    return !msg;
  }
  function validarDados() {
    var nome = form.elements.nome, tel = form.elements.telefone, email = form.elements.email;
    var ok = [
      erro(nome, nome.value.trim().length < 3 ? 'Informe seu nome para identificarmos o pedido.' : ''),
      erro(tel, V.telefoneValido(tel.value) ? '' : 'Informe um WhatsApp com DDD, ex.: (55) 99999-9999.'),
      erro(email, V.emailValido(email.value) ? '' : 'Confira o e-mail ou deixe em branco.')
    ];
    if (ok.indexOf(false) !== -1) { var f = $('[aria-invalid="true"]', form); if (f) f.focus(); return false; }
    tel.value = V.formatarTelefone(tel.value);
    return true;
  }

  /* ---------- mensagem do pedido ---------- */
  function mensagemPedido() {
    var pag = pagamento();
    var L = ['Olá, Drysul! Pedido ' + st.numero + ' feito pelo site.', '', '*Itens*'];
    st.av.linhas.forEach(function (l) {
      var p = A.produto(l.id);
      L.push('• ' + l.qtd + ' × ' + p.nome + ' — ' + p.emb.toLowerCase() + ' (' + BRL.format(p.preco) + '/' + p.un + ') = ' + BRL.format(l.total));
    });
    L.push('', 'Total dos produtos: ' + BRL.format(st.av.subtotal));
    L.push('Recebimento: ' + (entrega() === 'entrega' ? 'entrega no endereço (combinar taxa)' : 'retirada na loja'));
    L.push('Pagamento: ' + (st.pago ? NOMES_PAG[pag] + ' — aprovado (demonstração)' : NOMES_PAG[pag]));
    L.push('', 'Nome: ' + valor('nome'), 'WhatsApp: ' + valor('telefone'));
    if (valor('email')) L.push('E-mail: ' + valor('email'));
    return L.join('\n').replace(/ /g, ' ');
  }
  function linkWhats() { return loja.whatsUrl + '?text=' + encodeURIComponent(mensagemPedido()); }

  /* ---------- resultado (etapa 4) ---------- */
  function qrDemo(seed) {
    var n = 25, s = 0, cells = '';
    for (var i = 0; i < seed.length; i++) s = (s * 31 + seed.charCodeAt(i)) >>> 0;
    function rnd() { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }
    function finder(x, y) {
      return '<rect x="' + x + '" y="' + y + '" width="7" height="7"/><rect x="' + (x + 1) + '" y="' + (y + 1) + '" width="5" height="5" fill="#fff"/><rect x="' + (x + 2) + '" y="' + (y + 2) + '" width="3" height="3"/>';
    }
    for (var y = 0; y < n; y++) for (var x = 0; x < n; x++) {
      var inFinder = (x < 8 && y < 8) || (x > 16 && y < 8) || (x < 8 && y > 16);
      if (!inFinder && rnd() < 0.48) cells += 'M' + x + ' ' + y + 'h1v1h-1z';
    }
    return '<svg class="qr" viewBox="-2 -2 29 29" role="img" aria-label="QR Code ilustrativo de demonstração, não pagável">' +
      '<rect x="-2" y="-2" width="29" height="29" fill="#fff"/><g fill="#10162B">' + finder(0, 0) + finder(18, 0) + finder(0, 18) + '<path d="' + cells + '"/></g>' +
      '<g transform="rotate(-18 12.5 12.5)"><rect x="3" y="10" width="19" height="5.5" fill="#EF5023"/><text x="12.5" y="14.1" text-anchor="middle" font-size="3.6" font-weight="800" fill="#10162B" font-family="Archivo, sans-serif" letter-spacing=".3">DEMO</text></g></svg>';
  }

  function renderResultado() {
    var pag = pagamento(), total = BRL.format(st.av.subtotal), num = esc(st.numero);
    if (st.pago) {
      elRes.innerHTML = '<div class="co-ok">' + A.icon('i-check') +
        '<h3 class="co-h" tabindex="-1">Pagamento aprovado</h3>' +
        '<p>Pedido <b>' + num + '</b> · ' + total + ' · ' + esc(NOMES_PAG[pag]) + '</p>' +
        '<p class="co-ok__info">' + (entrega() === 'entrega'
          ? 'A equipe entra em contato pelo WhatsApp para combinar a entrega.'
          : 'Retire na loja: ' + esc(loja.endereco) + ' — ' + esc(loja.bairro) + '. Informe o número do pedido.') + '</p>' +
        (valor('email') ? '<p class="co-ok__info">Na versão final, o comprovante vai para ' + esc(valor('email')) + '.</p>' : '') +
        '<a class="btn btn--outline" href="' + esc(linkWhats()) + '" target="_blank" rel="noopener">' + A.icon('i-whats') + '<span>Avisar a loja no WhatsApp</span></a>' +
        '<p class="co-demo-note">Demonstração: nenhum valor foi cobrado.</p></div>';
      return;
    }
    if (pag === 'whatsapp') {
      elRes.innerHTML = '<div class="co-ok">' + A.icon('i-whats') +
        '<h3 class="co-h" tabindex="-1">Pedido enviado para o WhatsApp</h3>' +
        '<p>Pedido <b>' + num + '</b> · ' + total + '</p>' +
        '<p class="co-ok__info">A conversa abriu com o pedido pronto. A equipe confirma estoque, ' + (entrega() === 'entrega' ? 'taxa de entrega ' : '') + 'e forma de pagamento.</p>' +
        '<a class="btn btn--outline" href="' + esc(linkWhats()) + '" target="_blank" rel="noopener">' + A.icon('i-whats') + '<span>Abrir o WhatsApp de novo</span></a></div>';
      return;
    }
    if (pag === 'pix') {
      elRes.innerHTML = '<div class="co-pix"><h3 class="co-h" tabindex="-1">Pague com Pix</h3>' +
        '<p>Pedido <b>' + num + '</b> · <b>' + total + '</b></p>' + qrDemo(st.numero) +
        '<div class="field"><label for="co-pix-code"><span>Pix copia e cola</span></label><input id="co-pix-code" value="Gerado pelo provedor de pagamento na versão final" readonly disabled></div>' +
        '<ol class="co-howto"><li>Abra o app do seu banco e escolha Pix.</li><li>Leia o QR Code ou cole o código.</li><li>A confirmação chega aqui em segundos.</li></ol>' +
        '<p class="co-demo-note">QR Code ilustrativo: não é pagável.</p></div>';
      return;
    }
    elRes.innerHTML = '<div class="co-card"><h3 class="co-h" tabindex="-1">Pagamento seguro com ' + esc(NOMES_PAG[pag].toLowerCase()) + '</h3>' +
      '<p>Pedido <b>' + num + '</b> · <b>' + total + '</b></p>' +
      '<div class="co-provider">' + A.icon('i-lock') + '<div><b>Ambiente do provedor de pagamento</b>' +
      '<span>Na versão final, você é levado à página segura do provedor (ex.: Mercado Pago ou PagBank) para digitar o cartão. ' +
      'A Drysul não vê nem guarda os dados do cartão.</span></div></div>' +
      '<p class="co-demo-note">Demonstração: use o botão abaixo para simular a aprovação.</p></div>';
  }

  /* ---------- ações ---------- */
  function avancar() {
    if (st.etapa === 1) { irPara(2); return; }
    if (st.etapa === 2) { if (validarDados()) irPara(3); return; }
    if (st.etapa === 3) {
      st.numero = V.numeroPedido();
      if (pagamento() === 'whatsapp') window.open(linkWhats(), '_blank', 'noopener');
      renderResultado(); irPara(4);
      return;
    }
    if (st.etapa === 4) {
      if (!st.pago && pagamento() !== 'whatsapp') {
        st.pago = true;
        A.limparPedido();
        renderResultado(); atualizarRodape();
        var h = $('.co-h', elRes); if (h) h.focus({ preventScroll: true });
        A.toast('Pedido ' + st.numero + ' aprovado (demonstração).');
        return;
      }
      if (pagamento() === 'whatsapp') A.limparPedido();
      A.fecharDialogo(dlg);
    }
  }
  btNext.addEventListener('click', avancar);
  btBack.addEventListener('click', function () { if (st.etapa > 1) irPara(st.etapa - 1); });
  form.addEventListener('submit', function (ev) { ev.preventDefault(); avancar(); });
  form.addEventListener('change', function (ev) {
    if (ev.target.name === 'pagamento') st.escolheuWhats = ev.target.value === 'whatsapp';
    if (ev.target.name === 'entrega' || ev.target.name === 'pagamento') atualizarRodape();
  });
  form.addEventListener('input', function (ev) { if (ev.target.getAttribute('aria-invalid') === 'true') erro(ev.target, ''); });
  form.elements.telefone.addEventListener('blur', function () {
    if (V.telefoneValido(this.value)) this.value = V.formatarTelefone(this.value);
  });
  $('[data-co="editar"]', form).addEventListener('click', function () {
    var origem = dlg._retorno;
    A.fecharDialogo(dlg);
    A.abrirOrcamento(origem);
  });

  window.DrysulCheckout = { abrir: abrir };
})();
