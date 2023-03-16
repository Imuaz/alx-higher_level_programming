#!/usr/bin/node
const toNo = parseInt(process.argv[2]);
console.log(isNaN(toNo) ? 'Not a number' : `My number: ${toNo}`);
