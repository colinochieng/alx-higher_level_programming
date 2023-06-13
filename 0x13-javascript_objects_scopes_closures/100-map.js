#!/usr/bin/node
const List = require('./100-data.js').list;
const newL = List.map((val, idx) => val * idx);
console.log(List);
console.log(newL);
