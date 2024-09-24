#!/usr/bin/node
const args = process.argv.slice(2);
const numArr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", 
	"0", "-"];

//check if string is number or not
if (args.length >= 1) {
	let arg1 = args[0]

	if (numArr.includes(arg1[0])) {
		console.log("My number:", parseInt(args[0]))
	} else {
		console.log('Not a number')
	}
} else {
	console.log("Not a number")
}
