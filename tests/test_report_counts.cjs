const {test} = require('node:test');
const assert = require('node:assert/strict');
const {setup} = require('./report_harness.cjs');

test('coverage uses the singular word for one project', () => {
  const ui = setup([]);
  assert.match(ui.get('coverage').textContent, /across 1 project\./);
  assert.doesNotMatch(ui.get('coverage').textContent, /1 projects/);
});
