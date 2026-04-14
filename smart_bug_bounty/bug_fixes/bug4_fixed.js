function startCountdown() {
  // Fix: Changed 'var' to 'let' to provide block-scoping for each iteration
  for (let i = 0; i < 3; i++) {
    setTimeout(function() {
      console.log("Counting: " + i);
    }, 100);
  }
}

startCountdown(); // Output: 0, 1, 2 (sequentially)
