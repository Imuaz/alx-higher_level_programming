#!/usr/bin/node

const myAgv = process.argv.length;
console.log(myAgv === 2 ? 'No argument' : myAgv === 3 ? 'Argument found' : 'Arguments found');
