#!/usr/bin/node
const arr = require('./100-data').list;
const copy = arr.map((x, index) => x * index);
console.log(arr);
console.log(copy);
