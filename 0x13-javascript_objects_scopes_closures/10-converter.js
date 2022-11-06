#!/usr/bin/node
exports.converter = function (base) {
// Return a funciton that takes a number and convert to base specified in parent function
  return (num) => num.toString(base);
};
