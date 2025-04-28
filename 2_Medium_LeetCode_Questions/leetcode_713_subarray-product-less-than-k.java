class Solution {

    // Approach 1: My Sliding Window approach (dosen't work, exceed time limit) (note this question
    // assumes no negative integers in the input array)

    // My Sliding Window Approach:
    // For each ending index j, I tried to manually find the smallest starting index opt(j) such that:
    //          Product of nums[opt(j)..j] < k
    // and then count all valid subarrays ending at j.

    // Table of values:
    // Let nums = [10,5,2,6],
    // j    opt(j)	Valid Subarrays  	Subarrays Count
    // 0    0	          [10]	            +1
    // 1    0	      [10,5], [5]	        +2
    // 2    1	       [5,2], [2]	        +2
    // 3    1	    [5,2,6], [2,6], [6]	    +3

    // Explanation:
    // - At j=0: Only [10] is valid, so +1.
    // - At j=1: [10,5] and [5] are both valid, so +2.
    // - At j=2: [5,2] and [2] are valid, so +2.
    // - At j=3: [5,2,6], [2,6], [6] are valid, so +3.
    
    // How Count is Computed
    // For each j:
    //          count of subarrays = j − opt(j) + 1
    // because:
    // - Each starting index between opt(j) and j (inclusive) forms a valid subarray ending at j.
    // - Total number of valid subarrays = (j - opt(j) + 1).

    // Key Observations:
    // - I correctly identified that opt(j) is non-decreasing:
    //              opt(j) ≤ opt(j+1).
    // - For each j, the number of new subarrays can be counted without restarting the scan from scratch.
    // - However, my original for-loop approach still re-calculated too much instead of reusing previous work effectively.
    // - That caused Time Limit Exceeded (TLE) on large arrays.

    // How to Improve
    // - In the optimized sliding window approach:
    // - Instead of walking backward for each j,
    // - I should maintain a moving i (opt(j)) forward only when needed.
    // - No need to reset product for every new j.
    // - This reduces time complexity from O(n²) to O(n).

    // 📈 Final Result
    // - Correct intuition: counting valid subarrays by (j - opt(j) + 1).
    // - Needed improvement: avoid full recomputation for each new j, use continuous sliding window 
    //   (expand right, shrink left).
    public int numSubarrayProductLessThanK1(int[] nums, int k) {
        int count = 0;
        int j;              // j is for each ending index

        for (int i = 0; i < nums.length; i++) {
            j = i;

            int lengthOfSubarray = 0;
            int product = 1;
            int z;
            for (z = j; z > -1; z--) {

                // Product must be strictly less than k
                product *= (nums[z]);
                System.out.println("nums[z]: " + nums[z]);
                System.out.println("Product: " + product);
                System.out.println("lengthOfSubarray: " + lengthOfSubarray);

                if (product >= k) {
                    System.out.println("Break!");
                    break;
                }

                lengthOfSubarray += 1;

            }

            count += lengthOfSubarray;
        }

        return count;
    }


    ////////////////////////////////////////////////////////////////////////////////


    // Approach 2: My optimised Sliding window approach with reference to solution from ChatGPT
    // (works)  (note this question assumes no negative integers in the input array)

    // Suggested approach, an optimisation from my 'Approach 1: Sliding window approach' by ChatGPT:
    // Step                           | Action
    // 1. Start                       | product = 1, i = 0
    // 2. For each j                  | Expand window by multiplying product
    // 3. While product ≥ k           | Shrink window by moving i and dividing product
    // 4. After shrinking             | i = opt(j)
    // 5. Count subarrays in window   | Add (j - i + 1) to total count

    // Why is counting subarrays in window done with the formula of (j - i + 1)?
    // 🧠 Why is the number of subarrays = j - i + 1?
    // At every moment, you are looking at a window:
    //        [i,i+1,i+2,…,j]
    //
    // ✅ You want to know:
    // - How many subarrays end exactly at j,
    // - and start anywhere from i to j (inclusive).
    //
    // 📚 Visualize:
    // Suppose i=2, j=5:
    // Start index (s) | End index (j=5) | Subarray
    //      2          |       5         | nums[2..5]
    //      3          |       5         | nums[3..5]
    //      4          |       5         | nums[4..5]
    //      5          |       5         | nums[5..5]

    // ✅ How many subarrays?
    // - 2 → 5
    // - 3 → 5
    // - 4 → 5
    // - 5 → 5
    // There are 4 subarrays.

    // ✅ How to calculate:
    //          count=(5−2)+1=4
    // (We add 1 because both i and j are inclusive.)
    //
    // 🎯 General formula:
    // If window is [i, j] inclusive:
    // - Total subarrays ending at j = number of choices for start index s,
    //    where i ≤ s ≤ j.
    //
    // ✅ Number of start choices = j−i+1.
    public int numSubarrayProductLessThanK2(int[] nums, int k) {

        // Handling edge case where k <= 1
        if (k <= 1) {
            return 0;
        }


        // Using the hint: "For each j, let opt(j) be the smallest i so that
        // nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function."
        int count = 0;
        int opt_j = 0;      // opt(j) be the smallest i (left index) so that nums[i] * nums[i+1] * ... * nums[j] is
                            // less than k. opt is an increasing function
        int product = 1;

        for (int j = 0; j < nums.length; j++) {         // j is for each ending index

            product *= nums[j];

            while ((product >= k) && (opt_j < nums.length)){
                product /= nums[opt_j];
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

        int[] nums1 = {10,5,2,6};
        int k1 = 100;
        System.out.println(solution.numSubarrayProductLessThanK1(nums1, k1)); // 8

        int[] nums2 = {1,2,3};
        int k2 = 0;
        System.out.println(solution.numSubarrayProductLessThanK1(nums2, k2)); // 0



        int[] nums3 = {10,5,2,6};
        int k3 = 100;
        System.out.println(solution.numSubarrayProductLessThanK2(numss3, k3)); // 8

        int[] nums4 = {1,2,3};
        int k4 = 0;
        System.out.println(solution.numSubarrayProductLessThanK2(nums4, k4)); // 0

        int[] nums5 = {10,9,10,4,3,8,3,3,6,2,10,10,9,3};
        int k5 = 19;
        System.out.println(solution.numSubarrayProductLessThanK2(nums5, k5)); // 18
    }
}
