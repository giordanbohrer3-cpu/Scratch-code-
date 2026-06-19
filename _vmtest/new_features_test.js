// Testa, na FASE 2: plataformas flutuantes (pousar por cima), itens por dono,
// e cadeados (tranca/destranca). Vai direto à fase 2 via broadcast.
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
  const sv = (n, val) => { const v = stage().lookupVariableByNameAndType(n, ''); if (v) v.value = val; };
  const T = n => vm.runtime.targets.find(t => t.isOriginal && t.getName() === n);
  const key = (k, d) => vm.postIOData('keyboard', { key: k, isDown: d });
  let fails = 0;
  const check = (c, m) => { console.log((c ? 'PASS' : 'FAIL') + ': ' + m); if (!c) fails++; };

  vm.start(); vm.greenFlag();
  await sleep(400);
  // vai direto p/ a fase 2
  sv('fase', 2);
  vm.runtime.startHats('event_whenbroadcastreceived', { BROADCAST_OPTION: 'carregar_fase' });
  let t0 = Date.now();
  while (gv('modo') !== 2 && Date.now() - t0 < 9000) await sleep(150);
  await sleep(400);
  check(gv('fase') === 2 && gv('modo') === 2, 'fase 2 jogando (modo=' + gv('modo') + ')');

  // ---- PLATAFORMA FLUTUANTE: Lia anda até a base da pilha (x~140) e sobe ----
  for (let i = 0; i < 40; i++) {
    const lx = T('Lia').x;
    key('ArrowRight', lx < 138); key('ArrowLeft', lx > 142);
    if (gv('no_lia') === 1 && Math.abs(lx - 140) < 8) { key('ArrowUp', true); await sleep(90); key('ArrowUp', false); }
    if (T('Lia').y > -45) break;
    await sleep(110);
  }
  key('ArrowRight', false); key('ArrowLeft', false);
  await sleep(700);   // deixa assentar na plataforma
  check(gv('no_lia') === 1 && T('Lia').y > -45,
        'Lia POUSOU e ficou parada na plataforma flutuante (y=' + T('Lia').y.toFixed(0) + ')');

  // ---- ITENS POR DONO (estaciona o outro personagem longe) ----
  const o3 = T('Objeto3');              // item da Lia
  sv('item3', 0);
  for (let i = 0; i < 12; i++) { T('Lia').setXY(225, -90); T('Theo').setXY(o3.x, o3.y + 9); await sleep(40); }
  check(gv('item3') === 0, 'Theo NÃO pega item da Lia (item3=0)');
  for (let i = 0; i < 14; i++) { T('Theo').setXY(-230, -90); T('Lia').setXY(o3.x, o3.y + 9); await sleep(40); }
  check(gv('item3') === 1, 'Lia pega o próprio item (item3=1)');

  // item1 (Theo): Lia não pega
  const o1 = T('Objeto1'); sv('item1', 0);
  for (let i = 0; i < 12; i++) { T('Theo').setXY(225, -90); T('Lia').setXY(o1.x, o1.y + 9); await sleep(40); }
  check(gv('item1') === 0, 'Lia NÃO pega item do Theo (item1=0)');

  // ---- CADEADOS ----
  check(T('CadeadoT').visible === true && gv('cadT') === 0, 'cadeado da porta Theo TRANCADO');
  sv('item1', 1); sv('item2', 1); sv('item3', 1); sv('item4', 1);
  await sleep(800);
  check(gv('cadT') === 1 && gv('cadL') === 1, 'cadeados ABRIRAM após coletar tudo');
  check(T('CadeadoT').visible === false && T('CadeadoL').visible === false, 'cadeados sumiram (portas liberadas)');

  console.log('\nRESULTADO: ' + (fails === 0 ? 'TODOS OS TESTES PASSARAM ✓' : fails + ' FALHA(S)'));
  vm.stopAll(); process.exit(fails === 0 ? 0 : 1);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
