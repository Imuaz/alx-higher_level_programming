#!/usr/bin/node
const myVar = process.argv.length;
console.log(myVar === 3 ? 'Argument found' : myVar < 3 ? 'No argument' : 'Arguments found');
