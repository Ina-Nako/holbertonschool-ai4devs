function removeDuplicates(arr) {
    // Return a new array with duplicates removed, preserving order
    const seen = {};
    const result = [];
    for (let i = 0; i < arr.length; i++) {
        if (!seen[arr[i]]) {
            result.push(arr[i]);
        }
    }
    return result;
}

// Test cases
console.log(removeDuplicates([1, 2, 2, 3, 1]));       // Expected: [1, 2, 3]
console.log(removeDuplicates([false, 0, "", null]));   // Expected: [false, 0, "", null]
console.log(removeDuplicates(["a", "b", "a"]));        // Expected: ["a", "b"]
