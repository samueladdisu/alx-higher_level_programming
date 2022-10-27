#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < Math.floor(Number(x))) {
    theFunction();
    i++;
  }
};
