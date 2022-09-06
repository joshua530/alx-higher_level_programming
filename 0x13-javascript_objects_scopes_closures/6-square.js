#!/usr/bin/node
const Base = require('./5-square');
class Square extends Base {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let row = 0; row < this.height; ++row) { console.log(c.repeat(this.width)); }
    }
  }
}
module.exports = Square;
