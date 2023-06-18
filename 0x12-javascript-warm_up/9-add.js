#!/usr/bin/node

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add (a, b) {
  if (isNaN(b) || isNaN(a)) console.log('NaN');
  else console.log(a + b);
}

add(num1, num2);
