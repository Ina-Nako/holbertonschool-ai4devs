function startCountdown() {
  // Intended to print: "Counting: 0", "Counting: 1", "Counting: 2"
  // with a small delay between each.
  
  for (var i = 0; i < 3; i++) {
    setTimeout(function() {
      // Current issue: Using 'var' inside a loop with an asynchronous function.
      // Because 'var' is function-scoped, by the time the timeout runs,
      // the loop has finished and 'i' is already 3.
      console.log("Counting: " + i);
    }, 100);
  }
}

startCountdown();
