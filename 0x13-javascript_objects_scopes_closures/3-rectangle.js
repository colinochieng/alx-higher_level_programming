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
    while (i < this.height) {
      let j = 0;
      let raw = '';
      while (j < this.width) {
        raw += 'X';
        j++;
      }
      console.log(raw);
      i++;
    }
  }
};
