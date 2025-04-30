class Solution {
    public int findNumbers(int[] nums) {
        int numberOfNumbersWithEvenNumberDigits = 0;
        int counter;
        long current;
        for (int i = 0; i < nums.length; i++){
            current = nums[i];
            counter = 0;

            // Count number of digits
            while (current >= 1.0){
                System.out.println(current);
                current /= 10;
                counter += 1;
            }

            if (counter % 2 == 0){
                numberOfNumbersWithEvenNumberDigits += 1;
            }
        }

        return numberOfNumbersWithEvenNumberDigits;
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {12,345,2,6,7896};
        System.out.println(solution.findNumbers(nums1)); // 2

       int[] nums2 = {555,901,482,1771};
       System.out.println(solution.findNumbers(nums2)); // 1
    }
}