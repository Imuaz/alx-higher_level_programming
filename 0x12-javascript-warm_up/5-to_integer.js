#!/usr/bin/node
const args = process.argv;
let toNo= parseInt(args[2]);
console.log(isNaN(toNo) ? 'Not a number' : `My number: ${toNo}`);
