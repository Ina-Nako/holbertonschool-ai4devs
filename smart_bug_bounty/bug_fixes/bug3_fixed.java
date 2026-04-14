public class StringCompare {
    public static void main(String[] args) {
        String input = new String("SECRET");
        
        // Fix: Use .equals() for content comparison instead of ==
        if ("SECRET".equals(input)) {
            System.out.println("Access Granted");
        } else {
            System.out.println("Access Denied");
        }
    }
}
