const request = require('request');
const fs = require('fs');
const fileName  = process.argv.slice(2)[1];
const url = process.argv.slice(2)[0];

request(url, (error, response, body) => {
    if (error) {
        console.log(err);
    } else {
        fs.writeFile(fileName, body, (err) =>
            console.log(err))
    }
})
