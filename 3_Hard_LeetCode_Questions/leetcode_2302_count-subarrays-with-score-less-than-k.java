class Solution {

    // Approach 1: Sliding window approach (inspired approach from 'Approach 2: My optimised Sliding
    // window approach with reference to solution from ChatGPT' from 'Leetcode 713 - Subarray Product
    // Less Than K' (works) (note this question assumes no negative integers in the input array)

    // Since in the discussion tab in this Leetcode question said the approach for this question is
    // quite similar to that for Leetcode '713 - Subarray Product Less Than K'. See my solution to
    // 'Leetcode 713 - Subarray Product Less Than K' for more explanation about this approach
    public long countSubarrays(int[] nums, long k) {
        // Handling edge case where k <= 1
        if (k <= 1) {
            return 0;
        }


        // Using the hint: "For each j, let opt(j) be the smallest i so that
        // nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function."
        long count = 0;
        int opt_j = 0;      // opt(j) be the smallest i (left index) so that nums[i] * nums[i+1] * ... * nums[j] is
                            // less than k. opt is an increasing function
        long sum = 0;
        long length = 0;

        for (int j = 0; j < nums.length; j++) {         // j is for each ending index

            sum += nums[j];
            length += 1;

            // sum * length = score
            while ((sum * length >= k) && (opt_j < nums.length)){
                sum -= nums[opt_j];
                length -= 1;
                opt_j += 1;
            }

            count += j - opt_j + 1;
        }

        return count;
    }
}



class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {2,1,4,3,5};
        long k1 = 10;
        System.out.println(solution.countSubarrays(nums1, k1)); // 6

        int[] nums2 = {1,1,1};
        long k2 = 5;
        System.out.println(solution.countSubarrays(nums2, k2)); // 5
    }
}
