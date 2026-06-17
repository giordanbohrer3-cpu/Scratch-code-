// Teste de jogabilidade com pacing real (renderer stub). Valida física,
// pulo simultâneo, coleta, bloqueio por obstáculo, avanço de fase e vitória.
const fs = require('fs');
const VM = require('scratch-vm');
const fakeRenderer = require('./fakerender');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const vm = new VM();
  vm.attachRenderer(fakeRenderer());
  await vm.loadProject(fs.readFileSync(process.argv[2] || '/home/user/Scratch-code-/Dupla_das_Artes.sb3'));
  const stage = () => vm.runtime.getTargetForStage();
  const gv = n => { const v = stage().lookupVariableByNameAndType(n, ''); return v ? Number(v.value) : undefined; };
  const sv = (n, val) => { const v = stage().lookupVariableByNameAndType(n, ''); if (v) v.value = val; };
  const T = n => vm.runtime.targets.find(t => t.isOriginal && t.getName() === n);
  const key = (k, d) => vm.postIOData('keyboard', { key: k, isDown: d });
  let fails = 0;
  const check = (c, m) => { console.log((c ? 'PASS' : 'FAIL') + ': ' + m); if (!c) fails++; };

  vm.start(); vm.greenFlag();
  await sleep(600);
  check(gv('modo') === 0, 'título (modo 0)');
  check(T('Botao').visible === true, 'botão visível no título');

  vm.runtime.startHats('event_whenthisspriteclicked', null, T('Botao'));
  await sleep(400);
  check(gv('modo') === 1 && gv('fase') === 1, 'clicar inicia intro da fase 1');

  console.log('... intro de 7s ...');
  await sleep(7600);
  check(gv('modo') === 2, 'começa a jogar (modo 2)');
  await sleep(500);
  check(gv('no_theo') === 1 && gv('no_lia') === 1, 'os dois repousam no chão (no=1)');
  check(Math.abs(T('Theo').y + 94) < 6 && Math.abs(T('Lia').y + 94) < 6, 'y de repouso ~ -94');

  // PULO SIMULTÂNEO com ESPAÇO
  const tyA = T('Theo').y, lyA = T('Lia').y;
  key(' ', true); await sleep(110); key(' ', false);
  await sleep(140);
  check(T('Theo').y > tyA + 12 && T('Lia').y > lyA + 12,
        'ESPAÇO faz Theo E Lia pularem juntos');
  await sleep(900); // pousar

  // ANDAR + COLETA do item de chão
  key('ArrowRight', true);
  await sleep(800);
  check(T('Theo').x > -150, 'andou para a direita');
  check(gv('item1') === 1 && gv('Pontos') >= 5, 'coletou item 1 (chão) e ganhou pontos');

  // BLOQUEIO pelo obstáculo A (sem pular, fica preso antes dele)
  await sleep(1100);
  const xb = T('Theo').x;
  check(xb < -40 && xb > -60, 'bloqueado pelo obstáculo A (x~-53). x=' + xb.toFixed(0));
  check(gv('item2') === 0, 'sem pular, não alcança o item no topo (item2=0)');

  // PULAR por cima do A (segurando direita)
  key(' ', true); await sleep(110); key(' ', false);
  await sleep(1300);
  check(T('Theo').x > -10, 'após pular passou do obstáculo A. x=' + T('Theo').x.toFixed(0));
  check(gv('item2') === 1, 'coletou item 2 (topo do pedestal)');
  key('ArrowRight', false);
  await sleep(300);

  // FORÇAR conclusão (testa pipeline de avanço de fase)
  console.log('... forçando conclusão da fase ...');
  ['item1', 'item2', 'item3', 'item4', 'Theo_ok', 'Lia_ok'].forEach(v => sv(v, 1));
  await sleep(400);
  check(gv('modo') === 3, 'conclusão dispara transição (modo 3)');
  await sleep(3400);
  check(gv('fase') === 2 && gv('modo') === 1, 'avançou para a fase 2 (intro)');

  // VITÓRIA: completar a fase 5
  console.log('... testando vitória ...');
  sv('fase', 5); sv('modo', 2);
  await sleep(300);
  ['item1', 'item2', 'item3', 'item4', 'Theo_ok', 'Lia_ok'].forEach(v => sv(v, 1));
  await sleep(3800);
  check(gv('modo') === 4 && gv('fase') === 6, 'completou a fase 5 -> vitória');
  const conf = vm.runtime.targets.filter(t => !t.isOriginal && t.getName() === 'Confete').length;
  check(conf > 0, 'confete na vitória (clones=' + conf + ')');

  console.log('\nRESULTADO: ' + (fails === 0 ? 'TODOS OS TESTES PASSARAM ✓' : fails + ' FALHA(S)'));
  vm.stopAll(); process.exit(fails === 0 ? 0 : 1);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
