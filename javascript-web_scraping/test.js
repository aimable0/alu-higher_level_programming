const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
  
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let taskArr = {};
    let i = 0

    //loop here..
    let count = 0
    while(i < 200) {
        if (data[i].completed === true) {
            for (let m = 0; m < 20; m++) {
                taskAArr[data[]]
            }
        }
        i++
    }
  } 


})
