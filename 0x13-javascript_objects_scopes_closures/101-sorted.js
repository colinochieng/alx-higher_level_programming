#!/usr/bin/node
const obj = require('101-data.js').dict;
const arr = {};
for (const key in obj) {
  if (obj[key] in arr) {
    arr[obj[key]].push(key);
  } else {
    arr[obj[key]] = [key];
  }
}

console.log(arr);
