#!/usr/bin/node
const request = require('request');

const obj = {};
request.get(process.argv[2], (err, response, body) => {
  if (err) { console.error(err); }
  const data = JSON.parse(body);
  for (let idx = 0; data[idx]; idx++) {
    if (data[idx].userId in obj) {
      if (data[idx].completed === true) { obj[data[idx].userId]++; }
    } else {
      obj[data[idx].userId] = 0;
      if (data[idx].completed === true) { obj[data[idx].userId]++; }
    }
  }
  console.log(obj);
});
