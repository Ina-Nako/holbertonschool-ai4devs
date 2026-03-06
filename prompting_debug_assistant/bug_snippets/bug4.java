public class InventoryManager {
    private int[] stock = new int[10];
    
    public void initializeStock(int[] values) {
        // Initialize with provided values
        for (int i = 0; i <= values.length; i++) {  // Bug: <= should be <
            stock[i] = values[i];
        }
    }
    
    public int getTotalStock() {
        int total = 0;
        for (int i = 0; i < stock.length; i++) {
            total += stock[i];
        }
        return total;
    }
    
    public static void main(String[] args) {
        InventoryManager manager = new InventoryManager();
        int[] inventory = {5, 10, 3, 7, 2};
        manager.initializeStock(inventory);
        System.out.println("Total: " + manager.getTotalStock());
    }
}