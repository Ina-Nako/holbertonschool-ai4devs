// Bug 2 - Logical error (dedupe)
// Intended behavior: remove duplicates and return ascending numbers.

function dedupeAndSort(numbers) {
  const result = [];

  for (let i = 0; i < numbers.length; i++) {
    // BUG: this adds the number only if it is already present.
    if (result.includes(numbers[i])) {
      result.push(numbers[i]);
    }
  }

  return result.sort((a, b) => a - b);
}

const input = [3, 1, 2, 3, 2, 4, 1];
console.log(dedupeAndSort(input)); // expected [1,2,3,4]
