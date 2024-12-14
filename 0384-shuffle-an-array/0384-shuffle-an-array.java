class Solution {
    private int[] origin;
    private int[] array;
    private Random random = new Random();

    public Solution(int[] nums) {
        this.array = nums.clone();
        this.origin = nums.clone();
    }
    
    public int[] reset() {
        this.array = this.origin.clone();
        return this.array;
    }
    
    public int[] shuffle() {
        int[] shuffled = this.array.clone();
        
        for (int i = shuffled.length - 1; i > 0; i--) {
            int j = random.nextInt(i + 1);
            
            int temp = shuffled[j];
            shuffled[j] = shuffled[i];
            shuffled[i] = temp;
        }
        
        return shuffled;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */