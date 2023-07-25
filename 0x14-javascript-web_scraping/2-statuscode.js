#!/usr/bin/node
const request = require('request')

request.get(process.argv[2]).on('response', (request) => {
  console.log(`code: ${response.statusCode}`)
})