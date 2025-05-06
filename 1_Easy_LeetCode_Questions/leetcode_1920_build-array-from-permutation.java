import java.util.Arrays;

class Solution {
    public int[] buildArray(int[] nums) {
        int[] newArray = new int[nums.length];

        for (int i = 0; i < nums.length; i++){
            newArray[i] = nums[nums[i]];
        }

        return newArray;

    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {0,2,1,5,3,4};
        System.out.println(Arrays.toString(solution.buildArray(nums1)));      // [0,1,2,4,5,3]

        int[] nums2 = {5,0,1,2,3,4};
        System.out.println(Arrays.toString(solution.buildArray(nums2)));      // [4,5,0,1,2,3]

    }
}
