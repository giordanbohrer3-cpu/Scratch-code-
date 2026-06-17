// Sonda a física: segura → e pula em momentos específicos, logando a trajetória.
const fs = require('fs');
const VM = require('scratch-vm');
const sb3 = process.argv[2] || '/home/user/Scratch-code-/Dupla_das_Artes.sb3';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const fakeRenderer = require('./fakerender');

(async () => {
  const vm = new VM();
  vm.attachRenderer(fakeRenderer());
  await vm.loadProject(fs.readFileSync(sb3));
  const stage = () => vm.runtime.getTargetForStage();
  const gv = n => { const v = stage().lookupVariableByNameAndType(n, ''); return v ? Number(v.value) : undefined; };
  const T = n => vm.runtime.targets.find(t => t.isOriginal && t.getName() === n);
  const key = (k, d) => vm.postIOData('keyboard', { key: k, isDown: d });

  vm.start(); vm.greenFlag();
  await sleep(500);
  vm.runtime.startHats('event_whenthisspriteclicked', null, T('Botao'));
  await sleep(7700); // intro
  console.log('modo apos intro =', gv('modo'));

  key('ArrowRight', true);
  let jumpedA = false, jumpedB = false;
  for (let t = 0; t < 70; t++) {
    const x = T('Theo').x, y = T('Theo').y, no = gv('no_theo');
    // pular ao encostar no obstáculo A (perto de -53) e no B (perto de 71)
    if (!jumpedA && x > -56 && x < -50 && no === 1) {
      key(' ', true); await sleep(80); key(' ', false); jumpedA = true;
    } else if (jumpedA && !jumpedB && x > 66 && x < 76 && no === 1) {
      key(' ', true); await sleep(80); key(' ', false); jumpedB = true;
    }
    if (t % 4 === 0)
      console.log(`t=${(t*0.1).toFixed(1)}s x=${x.toFixed(0)} y=${y.toFixed(0)} no=${no} ` +
        `it=${gv('item1')}${gv('item2')}${gv('item3')}${gv('item4')} ok=${gv('Theo_ok')}${gv('Lia_ok')} modo=${gv('modo')}`);
    await sleep(100);
  }
  key('ArrowRight', false);
  console.log('FINAL fase=', gv('fase'), 'modo=', gv('modo'), 'pontos=', gv('Pontos'));
  vm.stopAll(); process.exit(0);
})().catch(e => { console.log('FATAL', e); process.exit(3); });
