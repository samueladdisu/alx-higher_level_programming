#!/usr/bin/node
const Base = require('./5-square');
module.exports = class Square extends Base {
  charPrint (c) {
    let char = 'X';
    if (c) {
      char = c;
    }
    let i = 0;
    while (i < Math.floor(Number(this.width))) {
      console.log(String(char).repeat(Math.floor(Number(this.height))));
      i++;
    }
  }
};
