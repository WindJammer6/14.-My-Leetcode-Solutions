import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minOperations(int[] nums, int k) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < k) {
                return -1;
            }
        }

        int ans = 0;
        Map<Integer, Integer> memory = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if ((nums[i] > k) && (!memory.containsKey(nums[i]))) {
                memory.put(nums[i], 1);
                ans += 1;
            }
        }

        return ans;
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        int[] nums1 = {5,2,5,4,5};
        System.out.println(solution.minOperations(nums1, 2));    // 2

        int[] nums2 = {2,1,2};
        System.out.println(solution.minOperations(nums2, 2));    // -1

        int[] nums3 = {9,7,5,3};
        System.out.println(solution.minOperations(nums3,1));    // 4

        int[] nums4 = {1};
        System.out.println(solution.minOperations(nums4,1));    // 0

        int[] nums5 = {10,10};
        System.out.println(solution.minOperations(nums5,10));    // 0
    }
}