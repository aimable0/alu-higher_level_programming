#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (_size) {
    super(_size, _size); // we are calling the Rectangle constructor..
    this.size = _size; // after calling the superclass we can now do a reference.
  }
}
module.exports = Square;
