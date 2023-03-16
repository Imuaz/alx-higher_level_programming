#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  let i = list.length -1;
  while (i >= 0) {
    reverseList.push(list[i]);
    i--;
  }
  return reverseList;
};
