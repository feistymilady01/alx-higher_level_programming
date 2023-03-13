#!/usr/bin/node
const args = process.argv;
const length = args.length;
let temp;
const array = [];
for (let i = 2; i < length; i++) {
  array[i] = parseInt(args[i]);
}
/* for (let j = 2; j < length; j++)
{
  console.log(array[j])
} */
if (length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      if (array[j] > array[i]) {
        temp = array[j];
        array[j] = array[i];
        array[i] = temp;
      }
    }
  }
  console.log(array[3]);
}
/* console.log(args[3]); */
