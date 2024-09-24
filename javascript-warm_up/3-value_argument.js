#!/usr/bin/node
const args = process.argv;
let len = 0;

// loop through the array and know the length
for (x in args) {
  len++; // increment lenght each time.
}

if (len >= 3) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
