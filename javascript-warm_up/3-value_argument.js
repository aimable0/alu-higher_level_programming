#!/usr/bin/node
const args = process.argv;
let len = 0
for (x in args) {
	len++;
}
if (len >= 3) {
	console.log(args[2]);
} else {
	console.log("No argument");
}
