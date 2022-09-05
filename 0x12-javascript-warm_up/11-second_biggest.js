#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
  process.exit(0);
}

let largest = parseInt(process.argv[2], 10);
let largest2;
for (let i = 3; i < process.argv.length; ++i) {
  const current = parseInt(process.argv[i], 10);
  if (largest < current) {
    largest2 = largest;
    largest = current;
  }
}
// all the numbers are equal
if (isNaN(largest2)) {
  largest2 = largest;
}
console.log(largest2);
