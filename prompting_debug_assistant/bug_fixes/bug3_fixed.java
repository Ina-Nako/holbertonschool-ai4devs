// Bug 3 Fixed - Runtime exception (NullPointerException)
// Intended behavior: compute average string length ignoring nulls.
// Fix: added null check before calling str.length(), and only increment count for non-null strings.

import java.util.Arrays;
import java.util.List;

class AverageStringLength {
    public static double averageLength(List<String> items) {
        int total = 0;
        int count = 0;

        for (String str : items) {
            if (str == null) continue;  // FIX: skip null entries
            total += str.length();
            count += 1;
        }

        if (count == 0) return 0.0;
        return (double) total / count;
    }

    public static void main(String[] args) {
        // Test 1: mixed nulls
        List<String> items1 = Arrays.asList("hi", null, "world");
        assert averageLength(items1) == 3.5 : "Test 1 failed";

        // Test 2: all nulls
        List<String> items2 = Arrays.asList((String) null, null);
        assert averageLength(items2) == 0.0 : "Test 2 failed";

        // Test 3: no nulls
        List<String> items3 = Arrays.asList("abc", "de");
        assert averageLength(items3) == 2.5 : "Test 3 failed";

        System.out.println("All tests passed.");
    }
}
