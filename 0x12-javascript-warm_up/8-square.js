#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < x) {
    let element = '';
    for (let j = 0; j < x; j++) element += 'X';
    console.log(element);
    i++;
  }
}
