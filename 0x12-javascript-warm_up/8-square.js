#!/usr/bin/node
const proc = require('process');
const num = Math.floor(Number(proc.argv[2]));
let i = 0;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (i < num) {
    console.log('X'.repeat(num));
    i++;
  }
}
