#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let outputs = '';
    while (i < this.height) {
      i++;
      let j = 0;
      while (j < this.width) {
        outputs = outputs + 'X';
        j++;
      }
      console.log(outputs);
      outputs = '';
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
