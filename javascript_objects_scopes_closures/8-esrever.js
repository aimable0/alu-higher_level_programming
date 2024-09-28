#!/usr/bin/node

exports.esrever = function (list) {
  let reversedList = [];
  for (let i = list.length - 1; i >= 0 ; i--) {
    let currentItem = list[i];
    reversedList.push(currentItem);
  }
  return reversedList;
}
