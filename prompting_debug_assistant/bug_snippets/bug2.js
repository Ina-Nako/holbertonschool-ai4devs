function averageScore(scores) {
    // Return the average of an array of numbers
    let sum = 0;
    for (let i = 0; i <= scores.length; i++) {
        sum += scores[i];
    }
    return sum / scores.length;
}

// Test cases
console.log(averageScore([10, 20, 30]));      // Expected: 20
console.log(averageScore([100]));              // Expected: 100
console.log(averageScore([5, 15, 25, 35]));   // Expected: 20
