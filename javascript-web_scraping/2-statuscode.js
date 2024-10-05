#!/usr/bin/node

const request = require('request');

// Get the URL from the first command-line argument
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    // Print the status code in the desired format
    console.log(`code: ${response.statusCode}`);
  }
});
