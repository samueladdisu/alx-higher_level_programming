#!/usr/bin/node
const proc = require('process');
const firstNum = Number(proc.argv[2]);
const secondNum = Number(proc.argv[3]);
function add (a, b) {
  return a + b;
}
console.log(add(firstNum, secondNum));
