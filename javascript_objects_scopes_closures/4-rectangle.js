#!/usr/bin/node

class Rectangle {
  constructor (_w, _h) {
    if (_w > 0 && _h > 0) {
      this.width = _w;
      this.height = _h;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--) {
      for (let m = this.width; m > 0; m--) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

module.exports = Rectangle;
