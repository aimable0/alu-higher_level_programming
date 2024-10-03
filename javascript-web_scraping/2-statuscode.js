#!/usr/bin/node

const url = process.argv.slice(2)[0];
const request = require('request');

request.addEventListener('readystatechange', () => {
  if (request.status == 200) {
    console.log("code:", request.status);
  }
})
request.open('GET', url);
request.send();
