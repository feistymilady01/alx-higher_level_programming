#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

// const file = fs.readFileSync(args[2], 'utf-8'); use try catch here.
fs.writeFile(args[2], args[3], 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
  // return;
});
