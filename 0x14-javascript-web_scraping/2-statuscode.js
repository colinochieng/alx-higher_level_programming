#!/usr/bin/node
const request = new Request(process.argv[2])
const response = fetch(request)
console.log(response.json())