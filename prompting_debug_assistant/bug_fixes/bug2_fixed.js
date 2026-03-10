// Bug 2 Fixed - Logical error (dedupe)
// Intended behavior: remove duplicates and return ascending numbers.
// Fix: inverted the condition so numbers are added only when NOT already present.

function dedupeAndSort(numbers) {
  const result = [];

  for (let i = 0; i < numbers.length; i++) {
    if (!result.includes(numbers[i])) {  // FIX: added ! to invert condition
      result.push(numbers[i]);
    }
  }

  return result.sort((a, b) => a - b);
}

// Tests
console.assert(
  JSON.stringify(dedupeAndSort([3, 1, 2, 3, 2, 4, 1])) === JSON.stringify([1, 2, 3, 4]),
  "Test 1 failed"
);
console.assert(
  JSON.stringify(dedupeAndSort([5, 5, 5])) === JSON.stringify([5]),
  "Test 2 failed"
);
console.assert(
  JSON.stringify(dedupeAndSort([])) === JSON.stringify([]),
  "Test 3 failed"
);
console.log("All tests passed.");
