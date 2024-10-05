#!/usr/bin/node 

const request = require('request');

const url = process.argv.slice(2)[0]
request('url', (error, response,body) => {
  if(!error && response.statuCode === 200) {
    console.log("code:", response.statusCode);
  } else {
      console.error('Error occured:', error);
  }
})
  
