function calculateTotal(prices) {
  let total = 0;
  // Fix: Changed <= to < to avoid accessing out-of-bounds index
  for (var i = 0; i < prices.length; i++) {
    total += prices[i];
  }
  return total;
}

const items = [10.99, 5.50, 3.00];
console.log("Total:", calculateTotal(items)); // Output: 19.49
