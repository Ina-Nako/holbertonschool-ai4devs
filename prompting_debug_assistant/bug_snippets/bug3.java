// Bug 3 - Runtime exception (NullPointerException)
// Intended behavior: compute average string length ignoring nulls.

import java.util.Arrays;
import java.util.List;

class AverageStringLength {
    public static double averageLength(List<String> items) {
        int total = 0;
        int count = 0;

        for (String str : items) {
            // BUG: str may be null; calling length() can throw NullPointerException
            total += str.length();
            count += 1;
        }

        if (count == 0) return 0.0;
        return (double) total / count;
    }

    public static void main(String[] args) {
        List<String> items = Arrays.asList("hi", null, "world");
        System.out.println(averageLength(items));
    }
}
