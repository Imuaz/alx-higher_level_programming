#!/usr/bin/node

const array = process.argv[2];
if (array === undefined){
  console.log('No argument');
}else {
  console.log(array);
}
