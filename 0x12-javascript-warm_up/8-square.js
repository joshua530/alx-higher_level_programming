#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; ++row) {
    console.log('X'.repeat(size));
  }
}
