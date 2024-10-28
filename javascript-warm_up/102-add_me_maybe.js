#!/usr/bin/node
exports.addMeMaybe = (number, thefunction) => {
  number++;
  thefunction(number);
};
