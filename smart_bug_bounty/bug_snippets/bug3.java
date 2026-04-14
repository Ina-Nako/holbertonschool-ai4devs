public class StringCompare {
    public static void main(String[] args) {
        String input = "SECRET";
        
        // Intended to check if the input matches the password
        if (input == "SECRET") {
            // Current issue: Using == for String comparison instead of .equals()
            System.out.println("Access Granted");
        } else {
            System.out.println("Access Denied");
        }
    }
}
