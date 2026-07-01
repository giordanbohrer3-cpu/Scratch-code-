// Bot de navegação: cada personagem busca seus 2 itens e depois a sua porta.
// Verifica que TODAS as 5 fases co-op são venciveis até a vitória.
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

  // alvo de um personagem: 1º item próprio não coletado, senão a porta
  function target(items, doorx, doory) {
    for (const it of items) if (gv(it.v) === 0) { const o = T(it.s); return [o.x, o.y, false]; }
    return [doorx, doory, true];
  }
  const prev = { Theo: 0, Lia: 0 };
  function nav(c, items, dvx, dvy, no, K) {
    const [tx, ty, isDoor] = target(items, gv(dvx), gv(dvy));
    const ch = T(c), dx = tx - ch.x;
    const grounded = gv(no) === 1;
    let goR = dx > 3, goL = dx < -3;
    if (ty < ch.y - 22 && grounded && Math.abs(dx) < 14) { goR = true; goL = false; }
    key(K.r, goR); key(K.l, goL);
    const needUp = ty > ch.y + 6;
    const stuck = Math.abs(ch.x - prev[c]) < 0.7 && Math.abs(dx) > 4;
    key(K.u, grounded && (needUp || stuck));
    prev[c] = ch.x;
  }
  const THEO = [{ v: 'item1', s: 'Objeto1' }, { v: 'item2', s: 'Objeto2' }];
  const LIA = [{ v: 'item3', s: 'Objeto3' }, { v: 'item4', s: 'Objeto4' }];
  const KT = { l: 'a', r: 'd', u: 'w' }, KL = { l: 'ArrowLeft', r: 'ArrowRight', u: 'ArrowUp' };

  vm.start(); vm.greenFlag();
  await sleep(400);
  vm.runtime.startHats('event_whenthisspriteclicked', null, T('Botao'));

  let maxFase = 1; const seen = {}; const t0 = Date.now();
  while (Date.now() - t0 < 220000) {
    const modo = gv('modo'), fase = gv('fase');
    if (fase > maxFase) { maxFase = fase; console.log(`  -> avancou p/ fase ${fase} em t=${((Date.now()-t0)/1000).toFixed(1)}s, pontos=${gv('Pontos')}`); }
    if (fase === 6) break;
    if (modo === 2) {
      if (!seen[fase]) { seen[fase] = Date.now(); console.log(`  fase ${fase}: entrou em t=${((Date.now()-t0)/1000).toFixed(1)}s`); }
      nav('Theo', THEO, 'dtx', 'dty', 'no_theo', KT);
      nav('Lia', LIA, 'dlx', 'dly', 'no_lia', KL);
    } else { ['a', 'd', 'w', 'ArrowLeft', 'ArrowRight', 'ArrowUp'].forEach(k => key(k, false)); }
    await sleep(95);
  }
  ['a', 'd', 'w', 'ArrowLeft', 'ArrowRight', 'ArrowUp'].forEach(k => key(k, false));

  const ok = gv('fase') === 6;
  console.log('fase final=' + gv('fase') + ' modo=' + gv('modo') + ' pontos=' + gv('Pontos') + ' maxFase=' + maxFase);
  console.log((ok ? 'PASS' : 'FAIL') + ': as 5 fases co-op sao venciveis ate a vitoria');
  console.log('\nRESULTADO: ' + (ok ? 'ZEROU ✓' : 'parou na fase ' + maxFase));
  vm.stopAll(); process.exit(ok ? 0 : 1);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
