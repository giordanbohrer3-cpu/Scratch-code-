const fs = require('fs');
const VM = require('scratch-vm');
const fakeRenderer = require('./fakerender');
const sleep = ms => new Promise(r => setTimeout(r, ms));
const PH = parseInt(process.argv[2] || '2', 10);
(async () => {
  const vm = new VM(); vm.attachRenderer(fakeRenderer());
  await vm.loadProject(fs.readFileSync('/home/user/Scratch-code-/Dupla_das_Artes.sb3'));
  const stage = () => vm.runtime.getTargetForStage();
  const gv = n => { const v = stage().lookupVariableByNameAndType(n, ''); return v ? Number(v.value) : undefined; };
  const sv = (n, val) => { const v = stage().lookupVariableByNameAndType(n, ''); if (v) v.value = val; };
  const T = n => vm.runtime.targets.find(t => t.isOriginal && t.getName() === n);
  const key = (k, d) => vm.postIOData('keyboard', { key: k, isDown: d });
  function target(items, dx, dy) { for (const it of items) if (gv(it.v) === 0) { const o = T(it.s); return [o.x, o.y]; } return [dx, dy]; }
  const prev = {};
  function nav(c, items, dvx, dvy, no, K) {
    const [tx, ty] = target(items, gv(dvx), gv(dvy));
    const ch = T(c), dx = tx - ch.x;
    const g = gv(no) === 1;
    let goR = dx > 3, goL = dx < -3;
    if (ty < ch.y - 22 && g && Math.abs(dx) < 14) { goR = true; goL = false; }  // sai da plataforma p/ cair
    key(K.r, goR); key(K.l, goL);
    const needUp = ty > ch.y + 6, stuck = Math.abs(ch.x - (prev[c] || 0)) < 0.7 && Math.abs(dx) > 4;
    key(K.u, g && (needUp || stuck)); prev[c] = ch.x;
    return [tx, ty];
  }
  const THEO = [{ v: 'item1', s: 'Objeto1' }, { v: 'item2', s: 'Objeto2' }];
  const LIA = [{ v: 'item3', s: 'Objeto3' }, { v: 'item4', s: 'Objeto4' }];
  const KT = { l: 'a', r: 'd', u: 'w' }, KL = { l: 'ArrowLeft', r: 'ArrowRight', u: 'ArrowUp' };

  vm.start(); vm.greenFlag(); await sleep(400);
  sv('fase', PH); vm.runtime.startHats('event_whenbroadcastreceived', { BROADCAST_OPTION: 'carregar_fase' });
  let t0 = Date.now(); while (gv('modo') !== 2 && Date.now() - t0 < 9000) await sleep(150);
  console.log('fase', gv('fase'), 'portas Theo(', gv('dtx'), gv('dty'), ') Lia(', gv('dlx'), gv('dly'), ')');
  t0 = Date.now();
  for (let i = 0; i < 120 && gv('modo') === 2; i++) {
    const tt = nav('Theo', THEO, 'dtx', 'dty', 'no_theo', KT);
    const tl = nav('Lia', LIA, 'dlx', 'dly', 'no_lia', KL);
    if (i % 8 === 0) console.log(`t=${((Date.now() - t0) / 1000).toFixed(1)} ` +
      `Theo(${T('Theo').x.toFixed(0)},${T('Theo').y.toFixed(0)},no${gv('no_theo')})->（${tt[0].toFixed(0)},${tt[1].toFixed(0)}) it12=${gv('item1')}${gv('item2')} ok=${gv('Theo_ok')} | ` +
      `Lia(${T('Lia').x.toFixed(0)},${T('Lia').y.toFixed(0)},no${gv('no_lia')})->(${tl[0].toFixed(0)},${tl[1].toFixed(0)}) it34=${gv('item3')}${gv('item4')} ok=${gv('Lia_ok')}`);
    await sleep(95);
  }
  console.log('FIM modo=', gv('modo'), 'fase=', gv('fase'));
  vm.stopAll(); process.exit(0);
})().catch(e => { console.log('FATAL', e); process.exit(3); });
