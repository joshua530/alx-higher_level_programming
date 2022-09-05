#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)) num = 1;

function factorial (n, memo = {}) {
  if (n === 0 || n === 1) {
    return 1;
  }
  if (n in memo) {
    return memo[n];
  }
  const fact = n * (factorial(n - 1));
  memo[n] = fact;
  return memo[n];
}
console.log(factorial(num));
