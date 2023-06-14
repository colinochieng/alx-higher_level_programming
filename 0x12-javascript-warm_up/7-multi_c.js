#!/usr/bin/node
let i = 0;
const num = parseInt(process.argv[2]);

if (isNaN(num)) console.log('Missing number of occurrences');

while (i < num) {
  console.log('C is fun');
  i++;
}
