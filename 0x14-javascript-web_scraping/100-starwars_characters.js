#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + process.argv[2], (err, head, body) => {
  if (err) {
    console.err(err);
    return;
  }
  const filmCharacters = JSON.parse(body).characters;
  for (let idx = 0; filmCharacters[idx]; idx++) {
    request.get(filmCharacters[idx]).on('data', (data) => {
      console.log(JSON.parse(data).name);
    });
  }
});
