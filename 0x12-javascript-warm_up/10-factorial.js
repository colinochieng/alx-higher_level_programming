#!/usr/bin/node
const num = process.argv[2];

function factorial (num) {
  if (num === 1) {
    return 1;
  } else if (isNaN(num)) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(num));
