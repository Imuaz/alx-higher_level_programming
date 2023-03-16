#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    let i = 0;
    let outputs = '';
    while (i < this.height) {
      i++;
      for (let j = 0; j < this.width; j++) {
        outputs = outputs + 'X';
      }
      console.log(outputs);
      outputs = '';
    }
  }
};
