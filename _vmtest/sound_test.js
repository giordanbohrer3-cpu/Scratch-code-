// Confirma que cada som dispara no momento certo (intercepta os blocos de som).
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

  // intercepta os blocos de som para contar o que tocou
  const plays = {};
  vm.runtime._primitives['sound_play'] = (args) => { plays[args.SOUND_MENU] = (plays[args.SOUND_MENU] || 0) + 1; };
  vm.runtime._primitives['sound_playuntildone'] = (args) => {
    plays[args.SOUND_MENU] = (plays[args.SOUND_MENU] || 0) + 1; return new Promise(r => setTimeout(r, 60));
  };
  let fails = 0;
  const check = (c, m) => { console.log((c ? 'PASS' : 'FAIL') + ': ' + m); if (!c) fails++; };

  vm.start(); vm.greenFlag();
  await sleep(700);
  check(plays['musica'] > 0, 'MÚSICA de fundo tocando em loop');

  // clicar em Jogar
  vm.runtime.startHats('event_whenthisspriteclicked', null, T('Botao'));
  await sleep(300);
  check(plays['clique'] > 0, 'som ao clicar em Jogar');

  // entra na fase 2 p/ testar o resto (pula a intro)
  sv('fase', 2);
  vm.runtime.startHats('event_whenbroadcastreceived', { BROADCAST_OPTION: 'carregar_fase' });
  let t0 = Date.now(); while (gv('modo') !== 2 && Date.now() - t0 < 9000) await sleep(150);
  await sleep(200);

  // coletar item
  sv('item1', 1); await sleep(250);
  check(plays['coletar'] > 0, 'som ao coletar item');

  // pular
  sv('vy_theo', 14); await sleep(200); sv('vy_theo', 0);
  check(plays['pulo'] > 0, 'som ao pular');

  // andar (pressiona a tecla de verdade p/ o Theo caminhar no chão)
  const before = plays['passo'] || 0;
  const key = (k, d) => vm.postIOData('keyboard', { key: k, isDown: d });
  key('d', true);
  await sleep(900);
  key('d', false);
  check((plays['passo'] || 0) > before, 'som ao andar (passos), tocou ' + ((plays['passo'] || 0) - before) + 'x');

  // destravar portas (todos os itens)
  sv('item1', 1); sv('item2', 1); sv('item3', 1); sv('item4', 1);
  await sleep(400);
  check(plays['destravar'] > 0, 'som ao destravar as portas');

  // festa ao zerar
  vm.runtime.startHats('event_whenbroadcastreceived', { BROADCAST_OPTION: 'vitoria' });
  await sleep(300);
  check(plays['festa'] > 0, 'som de festa/confete ao finalizar');

  console.log('\ncontagem:', JSON.stringify(plays));
  console.log('RESULTADO: ' + (fails === 0 ? 'TODOS OS SONS DISPARAM ✓' : fails + ' FALHA(S)'));
  vm.stopAll(); process.exit(fails === 0 ? 0 : 1);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
