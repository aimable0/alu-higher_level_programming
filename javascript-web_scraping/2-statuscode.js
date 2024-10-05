#!/usr/bin/node 
const request = require('request');

const url = process.argv.slice(2)[0];
request(url, (error, response, body) => {
    console.log("code:", response.statusCode);
})