#!/usr/bin/log
const request = require('request')

request.get(process.argv[2], (err, data, body) => {
  if (err) {
    console.error(err);
  }
  let json_data = JSON.parse(body);
  for ()
});