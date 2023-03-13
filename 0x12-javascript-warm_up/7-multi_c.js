#!/usr/bin/node

const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (args[2]; args[2] > 0; args[2]--) {
    console.log('C is fun');
  }
}
