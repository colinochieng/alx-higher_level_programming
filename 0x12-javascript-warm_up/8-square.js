#!/usr/bin/node
let i = 0;
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (i < num) {
    let j = 0;
    let width = '';
    while (j < num) {
      width += 'X';
      j++;
      }
    console.log(width);
    i++;
    }
}
