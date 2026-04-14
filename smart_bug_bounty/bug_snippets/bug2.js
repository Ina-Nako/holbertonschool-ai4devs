function calculateTotal(prices) {
  let total = 0;

  // Intended to add up all prices in the array
  for (var i = 0; i <= prices.length; i++) {
    // Current issue: Off-by-one error (accessing index out of bounds)
    total += prices[i];
  }

  return total;
}

const items = [10.99, 5.50, 3.00];
console.log("Total:", calculateTotal(items));
