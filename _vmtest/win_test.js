// Verifica que dá para VENCER a fase com os controles separados:
// Theo com D (+W/espaço), Lia com seta-direita (+seta-cima/espaço).
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
  await sleep(7700);

  // segura os dois para a direita; pula com ESPAÇO quando algum trava
  key('d', true); key('ArrowRight', true);
  let lastTx = -999, lastLx = -999, stuckT = 0, stuckL = 0;
  for (let i = 0; i < 60 && gv('modo') === 2; i++) {
    const tx = T('Theo').x, lx = T('Lia').x;
    stuckT = Math.abs(tx - lastTx) < 1 ? stuckT + 1 : 0;
    stuckL = Math.abs(lx - lastLx) < 1 ? stuckL + 1 : 0;
    if (stuckT >= 2 || stuckL >= 2) { key(' ', true); await sleep(90); key(' ', false); }
    lastTx = tx; lastLx = lx;
    await sleep(180);
  }
  key('d', false); key('ArrowRight', false);

  const done = gv('modo') !== 2;  // saiu do modo jogar => completou
  console.log('Theo.x=' + T('Theo').x.toFixed(0) + ' Lia.x=' + T('Lia').x.toFixed(0) +
    ' itens=' + [1,2,3,4].map(i=>gv('item'+i)).join('') +
    ' ok=' + gv('Theo_ok') + gv('Lia_ok') + ' modo=' + gv('modo') + ' fase=' + gv('fase'));
  await sleep(3600);
  const ok = gv('fase') === 2;
  console.log((ok ? 'PASS' : 'FAIL') + ': dá para vencer a fase 1 com controles separados e avança p/ fase 2');
  console.log('\nRESULTADO: ' + (ok ? 'VENCEU ✓' : 'NÃO COMPLETOU'));
  vm.stopAll(); process.exit(ok ? 0 : 1);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
