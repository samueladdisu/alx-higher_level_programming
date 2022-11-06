#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length - 1;
  const newList = [];
  while (size >= 0) {
    newList.push(list[size]);
    size--;
  }
  return newList;
};
