// Testa controles INDIVIDUAIS: Theo=WASD, Lia=setas, ESPAÇO = os dois pulam.
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
  const T = n => vm.runtime.targets.find(t => t.isOriginal && t.getName() === n);
  const key = (k, d) => vm.postIOData('keyboard', { key: k, isDown: d });
  let fails = 0;
  const check = (c, m) => { console.log((c ? 'PASS' : 'FAIL') + ': ' + m); if (!c) fails++; };
  const press = async (k, ms = 250) => { key(k, true); await sleep(ms); key(k, false); await sleep(120); };

  vm.start(); vm.greenFlag();
  await sleep(500);
  vm.runtime.startHats('event_whenthisspriteclicked', null, T('Botao'));
  await sleep(7700);
  check(gv('modo') === 2, 'jogando (modo 2)');
  await sleep(400);
  check(T('Chao').currentCostume === 0, 'chão da fase 1 (costume 0). atual=' + T('Chao').currentCostume);
  check(T('Obstaculo').currentCostume === 0, 'obstáculo da fase 1 (costume 0)');

  // --- Theo anda com D (e NÃO com setas) ---
  let tx = T('Theo').x, lx = T('Lia').x;
  await press('d', 400);
  check(T('Theo').x > tx + 15, 'Theo anda para a direita com D');
  check(Math.abs(T('Lia').x - lx) < 3, 'Lia NÃO se move com D');

  // --- Lia anda com seta direita (e NÃO Theo) ---
  tx = T('Theo').x; lx = T('Lia').x;
  await press('ArrowRight', 400);
  check(T('Lia').x > lx + 15, 'Lia anda para a direita com a seta');
  check(Math.abs(T('Theo').x - tx) < 3, 'Theo NÃO se move com a seta');

  // --- Theo volta com A ---
  tx = T('Theo').x;
  await press('a', 300);
  check(T('Theo').x < tx - 10, 'Theo anda para a esquerda com A');

  // --- ESPAÇO faz os DOIS pularem ---
  await sleep(300);
  let ty = T('Theo').y, ly = T('Lia').y;
  key(' ', true); await sleep(110); key(' ', false);
  await sleep(150);
  check(T('Theo').y > ty + 12 && T('Lia').y > ly + 12, 'ESPAÇO faz Theo E Lia pularem juntos');
  await sleep(900);

  // --- W pula só o Theo; seta-cima pula só a Lia ---
  ty = T('Theo').y; ly = T('Lia').y;
  key('w', true); await sleep(110); key('w', false); await sleep(150);
  check(T('Theo').y > ty + 12 && Math.abs(T('Lia').y - ly) < 6, 'W pula só o Theo');
  await sleep(900);
  ty = T('Theo').y; ly = T('Lia').y;
  key('ArrowUp', true); await sleep(110); key('ArrowUp', false); await sleep(150);
  check(T('Lia').y > ly + 12 && Math.abs(T('Theo').y - ty) < 6, 'Seta-cima pula só a Lia');
  await sleep(900);

  // --- avançar de fase muda o chão/obstáculo ---
  console.log('... concluindo fase 1 para checar troca de cenário ...');
  ['item1', 'item2', 'item3', 'item4', 'Theo_ok', 'Lia_ok'].forEach(v => {
    const vv = stage().lookupVariableByNameAndType(v, ''); if (vv) vv.value = 1;
  });
  await sleep(3600);
  check(gv('fase') === 2, 'avançou para a fase 2');
  await sleep(7800); // intro da fase 2
  check(gv('modo') === 2 && T('Chao').currentCostume === 1, 'chão MUDOU para a fase 2 (costume 1). atual=' + T('Chao').currentCostume);
  check(T('Obstaculo').currentCostume === 1, 'obstáculo MUDOU para a fase 2');

  // partículas de fundo (clones) existem
  const clones = vm.runtime.targets.filter(t => !t.isOriginal && t.getName() === 'Particula').length;
  check(clones >= 10, 'partículas de fundo animadas (clones=' + clones + ')');

  console.log('\nRESULTADO: ' + (fails === 0 ? 'TODOS OS TESTES PASSARAM ✓' : fails + ' FALHA(S)'));
  vm.stopAll(); process.exit(fails === 0 ? 0 : 1);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
