#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
/*request.get(process.argv[2], (err, response, body) => {
  if (err) { console.error(err); } else {
    fs.writeFile(process.argv[3], body, err => {
      if (err) { console.error(err); }
    });
  }
});*/
