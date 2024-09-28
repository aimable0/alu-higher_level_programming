#!/bin/node
class Rectangle {
  constructor (_w, _h) {
    if (_w > 0 && _h > 0) {
      this.width = _w;
      this.height = _h;
    }
  }
}
module.exports = Rectangle;
