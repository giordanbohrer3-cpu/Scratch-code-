// Autoplay: segura os dois p/ a direita e pula sempre que está no chão.
// Verifica que TODAS as 5 fases (layouts diferentes) são venciveis até a vitória.
const fs = require('fs');
const VM = require('scratch-vm');
const fakeRenderer = require('./fakerender');
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const vm = new VM();
  vm.attachRenderer(fakeRenderer());
  await vm.loadProject(fs.readFileSync('/home/user/Scratch-code-/Dupla_das_Artes.sb3'));
  const stage = () => vm.runtime.getTargetForStage();
  const gv = n => { const v = stage().lookupVariableByNameAndType(n, ''); return v ? Number(v.value) : undefined; };
  const T = n => vm.runtime.targets.find(t => t.isOriginal && t.getName() === n);
  const key = (k, d) => vm.postIOData('keyboard', { key: k, isDown: d });

  vm.start(); vm.greenFlag();
  await sleep(500);
  vm.runtime.startHats('event_whenthisspriteclicked', null, T('Botao'));

  key('d', true); key('ArrowRight', true);
  let maxFase = 1, lastSeen = {};
  const t0 = Date.now();
  while (Date.now() - t0 < 95000) {
    const modo = gv('modo'), fase = gv('fase');
    if (fase > maxFase) maxFase = fase;
    if (fase === 6) break;                       // vitória
    if (modo === 2) {
      // pula sempre que algum está no chão (atravessa obstáculos)
      if (gv('no_theo') === 1 || gv('no_lia') === 1) { key(' ', true); await sleep(70); key(' ', false); }
      const k = 'f' + fase;
      if (!lastSeen[k]) { lastSeen[k] = true; console.log('  entrou na fase ' + fase +
        ' (chão costume ' + T('Chao').currentCostume + ', obst ' + T('Obstaculo').currentCostume + ')'); }
    }
    await sleep(110);
  }
  key('d', false); key('ArrowRight', false);

  const fase = gv('fase'), modo = gv('modo');
  console.log('Fase final=' + fase + ' modo=' + modo + ' Pontos=' + gv('Pontos') + ' maxFase=' + maxFase);
  const ok = fase === 6;
  console.log((ok ? 'PASS' : 'FAIL') + ': venceu todas as 5 fases ate o Museu Completo');
  console.log('\nRESULTADO: ' + (ok ? 'ZEROU O JOGO ✓' : 'parou na fase ' + maxFase));
  vm.stopAll(); process.exit(ok ? 0 : 1);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
