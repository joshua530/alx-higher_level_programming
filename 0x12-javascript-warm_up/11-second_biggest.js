#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
  process.exit(0);
}

const nums = process.argv.slice(2);
nums.sort((a, b) => a - b);
nums.pop();
console.log(nums[nums.length - 1]);
