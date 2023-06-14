#!/usr/bin/node
if (process.argv.length < 3) { 
  console.log(0);
  process.exit(0);
}
let arr = process.argv.slice(2).map((num) => parseInt(num));

arr.sort(function(a, b) {
    return b - a;
  });

let i;
let maxNum = arr[0];
for (i = 0; arr[i] !== undefined; i++) {
  if (arr[i] < maxNum) {
    console.log(arr[i]);
    process.exit(0);
    }
}

console.log(0);
