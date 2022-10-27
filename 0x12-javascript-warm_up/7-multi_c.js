#!/usr/bin/node
const proc = require('process');
const num1 = Number(proc.argv[2]);
const num2 = Number(proc.argv[2]);
let i = 0;
if ((num1 !== num2) || num1 === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (i < num1) {
    console.log('C is fun');
    i++;
  }
}
