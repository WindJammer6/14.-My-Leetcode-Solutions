import java.util.HashMap;
import java.util.Map;

class Solution {
    
    public int arithmeticTriplets(int[] nums, int diff) {
        Map<Integer, Integer> map = new HashMap<>();
        int counter = 0;

        for (int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }

        for (int j = 0; j < nums.length; j++){
            
            if ((map.containsKey(nums[j] + diff)) && (map.containsKey(nums[j] + diff + diff))){
                counter += 1;
                
            }
            
        }
        
        return counter;
        
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {0,1,4,6,7,10};
        int diff1 = 3;
        System.out.println(solution.arithmeticTriplets(nums1, diff1));      // 2

        int[] nums2 = {4,5,6,7,8,9};
        int diff2 = 2;
        System.out.println(solution.arithmeticTriplets(nums2, diff2));      // 2
    }
}
