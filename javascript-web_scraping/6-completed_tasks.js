#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2)[0]

request(url, (error, response, body) => {
  
  if (error) {
    console.error(error);
  } else {
    let arr = {}
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
        if (data[i].userId in arr && data[i].completed === true) {
            arr[data[i].userId] += 1; 
        } else if (data[i].completed === true){
            arr[data[i].userId] = 1;
        }
    }
    console.log(arr);
  }

})
