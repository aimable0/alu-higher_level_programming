#!/usr/bin/node
const fileName = process.argv.slice(2)[0];
const content = process.argv.slice(2)[1];
const fs = require('fs');
fs.writeFile(fileName, content, (err) => {
  if (err) {
    console.log(err);
  }
});
