#!/usr/bin/node
const args = process.argv.slice(2); // saves the array if arg from cmd line
const text = 'C is fun';

// check if the argument is provided.

if (args.length === 1) {
  const times = args[0]; // save the 3 arg as a number of times

  // check if the arg is valid positive number.
  if (/^[1-9]\d*$/.test(times)) {
    // prints text number of times
    for (let i = times; i > 0; i--) {
      console.log(text);
    }
  }
} else {
  console.log('Missing number of occurrences');
}
