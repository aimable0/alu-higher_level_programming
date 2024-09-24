#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (num) {
  if (isNaN(num) || num <= 0) {
    return 1;
  }

  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(args[0]));
