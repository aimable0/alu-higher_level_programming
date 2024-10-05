#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2)[0];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < data.results.length; i++) {
      const charArray = data.results[i].characters;
      for (let m = 0; m < charArray.length; m++) {
        if (charArray[m].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
