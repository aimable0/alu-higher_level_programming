#!/usr/bin/node
exports.callMeMoby = (x, thefunction) => {
  for (let i = 0; i < x; i++) {
    thefunction();
  };
};
