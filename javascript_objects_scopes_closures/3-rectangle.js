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
}
module.exports = Rectangle;
