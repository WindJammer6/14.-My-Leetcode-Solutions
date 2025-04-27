import java.util.ArrayList;

class Solution {
    public int countSubarrays(int[] nums) {
        ArrayList<int[]> allSubarrays = new ArrayList<>();
        int[] arrayOfLengthThree;

        for (int i = 0; i < nums.length; i++){
            if (i + 2 < nums.length){

                System.out.println(nums[i]);
                System.out.println(nums[i+1]);
                System.out.println(nums[i+2]);
                System.out.println("");

                if ((nums[i] + nums[i+2]) * 2 == nums[i+1]){
                    arrayOfLengthThree = new int[3];
                    arrayOfLengthThree[0] = nums[i];
                    arrayOfLengthThree[1] = nums[i+1];
                    arrayOfLengthThree[2] = nums[i+2];

                    allSubarrays.add(arrayOfLengthThree);
                }


            }

        }

        return allSubarrays.size();
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {1,2,1,4,1};
        System.out.println(solution.countSubarrays(nums1)); // 1

        int[] nums2 = {1,1,1};
        System.out.println(solution.countSubarrays(nums2)); // 0
    }
}
