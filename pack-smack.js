const { execFile } = require('child_process');
const path = require('path');
const express = require('express');
const ansiToHtml = require('ansi-to-html');
const convert = new ansiToHtml();

const binaryPath = path.join(__dirname, 'dist', 'sense_falcon_sensor');

function runBinary(res) {
  execFile(binaryPath, (error, stdout, stderr) => {
    if (error) {
      if (res) return res.status(500).send(error.message);
      console.error(`Error: ${error.message}`);
      return;
    }
    if (stderr) console.error(`stderr: ${stderr}`);
    if (res) return res.send(`<pre>${convert.toHtml(stdout)}</pre>`);
    console.log(`stdout:\n${stdout}`);
  });
}

const arg = process.argv[2];
if (arg === '--run-once') {
  runBinary();
} else {
  const app = express();
  app.get('/run', (req, res) => runBinary(res));
  app.listen(3000, () => console.log('Status check available at http://localhost:3000/run'));
}
