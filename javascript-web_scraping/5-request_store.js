#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const fileName = process.argv.slice(2)[1];
const url = process.argv.slice(2)[0];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
