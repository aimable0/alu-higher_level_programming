#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charprint(c) {
    if (c === undefined) {
      for (let i = this.height; i > 0; i--) {
        for (let m = this.width; m > 0; m--) {
          process.stdout.write('X');
        }
        console.log();
      }
    } else {
      for (let i = this.height; i > 0; i--) {
        for (let m = this.width; m > 0; m--) {
          process.stdout.write(c);
        }
        console.log();
      }
    }

  }

}
module.exports = Square;