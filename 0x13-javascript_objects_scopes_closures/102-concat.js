#!/usr/bin/node
const fs = require('fs');
const proc = require('process');
const args = proc.argv;
const A = fs.readFileSync(args[2], 'utf8');
const B = fs.readFileSync(args[3], 'utf8');
fs.writeFileSync(args[4], A + B);
