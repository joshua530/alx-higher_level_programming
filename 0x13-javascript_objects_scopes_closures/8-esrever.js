#!/usr/bin/node
exports.esrever = function (list) {
  for (let beg = 0, end = list.length - 1; beg < end; ++beg, --end) {
    const tmp = list[beg];
    list[beg] = list[end];
    list[end] = tmp;
  }
  return list;
};
