function findMax(arr) {
  let max = 0; // Should be initialized to the first element or -Infinity
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

// This will incorrectly return 0 because all numbers are negative
console.log("Max value:", findMax([-1, -5, -3]));