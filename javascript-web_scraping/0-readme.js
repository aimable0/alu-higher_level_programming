#!/usr/bin/node
const fileName = process.argv.slice(2)[0];
const fs = require('fs'); 
fs.readFile(fileName, encoding='utf-8', (err, data) => {
	if (err) {
		console.log(err);
		return;
	}
	console.log(data);
})
