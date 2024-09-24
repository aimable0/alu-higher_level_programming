#!/usr/bin/node
const args = process.argv.slice(2);
const x = "X";
if (args.length == 1) {
	if (/^[1-9]\d*$/.test(args[0])) {
		let size = args[0]

		for (let i = size; i > 0; i--) {
			for (let m = size; m > 0; m--) {
				process.stdout.write(x)
			}
			console.log("");
		}

	} else {
		console.log("Missing size");
	}

} else {
	console.log("Missing size");
}
