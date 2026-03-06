function concatenateNumbers(a, b) {
  // This will perform string concatenation instead of addition
  return a + "" + b; // Should be a + b for numerical sum
}

console.log("Result:", concatenateNumbers(5, 10)); // Expected: 15, Actual: "510"