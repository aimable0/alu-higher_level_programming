#!/usr/bin/env node
exports.addMeMaybe = (number, thefunction)  => {
  number++;
  thefunction(number);
}
