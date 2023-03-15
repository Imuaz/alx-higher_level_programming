#!/usr/bin/node
const process = require('process');
let arg = process.argv[2];
console.log( arg === undefined ? 'No argument' : `${arg}`);
