#!/usr/bin/node

const args = process.argv.slice(2);

function factorial(i) {	

	let factorial = 1
	
	if (/^[1-9]\d*$/.test(i)) {
		i = parseInt(i);
		while (i !== 0) {
			factorial *= i;
			i--;
		}
		return factorial;


	} else {
		return "1";
	}
}
console.log(factorial(args[0]));
