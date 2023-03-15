#!/usr/bin/node
const myVar = process.argv.lenght;
console.log(myVar === 2 ? 'No argument' : myVar === 3 ? 'Argument found' : 'Arguments found');
