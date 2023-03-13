#!/usr/bin/node

const args = process.argv;

const output = parseInt(args[2]);
if (isNaN(output)) {
  console.log('Not a number');
} else {
  console.log('My number:', output);
}
