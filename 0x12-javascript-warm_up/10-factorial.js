#!/usr/bin/node

const args = process.argv;
let result;

function factorial (a) {
  if (a < 2 || isNaN(a)) {
    return 1;
  } else {
    result = a * (factorial(a - 1));
    /* console.log(result); */
  }
  return result;
  /* console.log(result); */
}

console.log(factorial(parseInt(args[2])));
