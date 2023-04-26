#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

// const file = fs.readFileSync(args[2], 'utf-8'); use try catch here.
fs.readFile(args[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.toString());
});
