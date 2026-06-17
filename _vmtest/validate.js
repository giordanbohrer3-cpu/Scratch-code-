// Valida um .sb3: carrega no scratch-vm, roda a bandeira verde, avança frames,
// e reporta erros/exceções. Uso: node validate.js caminho.sb3 [frames]
const fs = require('fs');
const path = require('path');
const VM = require('scratch-vm');
const JSZip = require('jszip');

const sb3Path = process.argv[2];
const frames = parseInt(process.argv[3] || '120', 10);

const problems = [];
const origErr = console.error;
console.error = (...a) => { problems.push('console.error: ' + a.join(' ')); };
const origWarn = console.warn;
console.warn = (...a) => { problems.push('console.warn: ' + a.join(' ')); };

(async () => {
  const buf = fs.readFileSync(sb3Path);
  const zip = await JSZip.loadAsync(buf);
  const projectJSON = await zip.file('project.json').async('string');

  // Storage simples: serve assets do próprio zip
  const vm = new VM();
  const storage = vm.runtime.storage;

  // Carrega project.json + assets manualmente (sem renderer)
  const sprNames = [];
  let runtimeErrors = [];
  vm.runtime.on('PROJECT_LOADED', () => {});
  // captura exceções de blocos
  const origStep = vm.runtime._step.bind(vm.runtime);
  vm.runtime._step = function () {
    try { return origStep(); }
    catch (e) { runtimeErrors.push('step: ' + (e && e.stack || e)); }
  };

  try {
    await vm.loadProject(buf);
  } catch (e) {
    console.log('LOAD_ERROR: ' + (e && e.stack || e));
    process.exit(2);
  }

  // Conta alvos/blocos
  const targets = vm.runtime.targets;
  const realTargets = targets.filter(t => !t.isOriginal ? false : true);
  let totalBlocks = 0, badInputs = 0, opcodes = {};
  for (const t of targets) {
    if (!t.blocks) continue;
    const all = t.blocks._blocks || {};
    for (const id in all) {
      totalBlocks++;
      const b = all[id];
      opcodes[b.opcode] = (opcodes[b.opcode] || 0) + 1;
      // valida que cada bloco tem opcode conhecido pela engine
      if (!vm.runtime.getOpcodeFunction(b.opcode) &&
          !['procedures_definition','procedures_prototype','procedures_call',
            'argument_reporter_string_number','argument_reporter_boolean'].includes(b.opcode) &&
          !b.shadow && !b.opcode.endsWith('_menu') &&
          !['looks_costume','looks_backdrops','sensing_keyoptions',
            'sensing_touchingobjectmenu','control_create_clone_of_menu',
            'event_whenflagclicked','event_whenbroadcastreceived','event_whenthisspriteclicked',
            'event_whenkeypressed','control_start_as_clone'].includes(b.opcode)) {
        problems.push('UNKNOWN_OPCODE ' + b.opcode + ' in ' + t.getName());
      }
    }
  }

  // Roda a bandeira verde e avança frames
  vm.start();
  vm.greenFlag();
  for (let i = 0; i < frames; i++) {
    try { vm.runtime._step(); } catch (e) { runtimeErrors.push('manualstep: ' + e); }
  }

  console.log('TARGETS: ' + targets.map(t => t.getName()).join(', '));
  console.log('TOTAL_BLOCKS: ' + totalBlocks);
  console.log('THREADS_RUNNING: ' + vm.runtime.threads.length);
  console.log('PROBLEMS: ' + problems.length);
  problems.slice(0, 40).forEach(p => console.log('  - ' + p));
  console.log('RUNTIME_ERRORS: ' + runtimeErrors.length);
  runtimeErrors.slice(0, 20).forEach(p => console.log('  ! ' + p));
  console.log(problems.length === 0 && runtimeErrors.length === 0 ? 'VALIDATION_OK' : 'VALIDATION_ISSUES');
  process.exit(0);
})().catch(e => { console.log('FATAL: ' + (e && e.stack || e)); process.exit(3); });
