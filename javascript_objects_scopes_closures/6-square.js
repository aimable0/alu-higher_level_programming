#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    // If no character is provided, default to 'X'
    if (c === undefined) {
      c = 'X';
    }

    // Loop to print each row of the square
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
