class Solution {
    public int missingNumber(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length+1; i++){
            hashmap.put(i, 0);
        }

        // To print out the HashMap visually:
        // for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
        //     System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
        // }

        for (int j : nums){
            hashmap.put(j, 1);
        }

        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            if (entry.getValue() == 0){
                return entry.getKey();
            }
        }
        return -1;
    }
}