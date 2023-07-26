#!/usr/bin/node
const request = require('request');
const uri = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request.get(process.argv[2], (err, data, body) => {
  if (err) {
    console.error(err);
  }
  const jsonData = JSON.parse(body);
  const array = [];
  for (let i = 0; jsonData.results[i]; i++) {
    array.push(jsonData.results[i].characters);
  }
  for (let idx = 0; array[idx]; idx++) {
    if (array[idx].includes(uri)) {
      count++;
    }
  }
  console.log(count);
});
