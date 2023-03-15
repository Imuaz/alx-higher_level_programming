#!/usr/bin/node
//const process = require('process');
const arg = process.argv[2];
console.log(typeof arg === 'undefined' ? 'No argument' : `${arg}`);
