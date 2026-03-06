public class ArrayBug {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        // This loop tries to access an index beyond the array's bounds
        for (int i = 0; i <= numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }
}
