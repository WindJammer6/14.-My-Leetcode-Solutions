class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int leftIndex = 0;
        int rightIndex;

        while (leftIndex + 1 < nums.length){
            rightIndex = leftIndex + 1;

            for (int i = 0; i < k; i++){
//                System.out.println(leftIndex);
//                System.out.println(rightIndex);
//                System.out.println(String.format("nums[leftIndex]: %d", (nums[leftIndex])));
//                System.out.println(String.format("nums[rightIndex]: %d", (nums[rightIndex])));
                if (rightIndex + i< nums.length) {
                    if (nums[leftIndex] == nums[rightIndex + i]){
                        return true;
                    }

                } else{
                    break;
                }
            }

            leftIndex += 1;
        }

        return false;
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {1,2,3,1};
        int k1 = 3;
        System.out.println(solution.containsNearbyDuplicate(nums1, k1)); // true

        int[] nums2 = {1,0,1,1};
        int k2 = 1;
        System.out.println(solution.containsNearbyDuplicate(nums2, k2)); // true

        int[] nums3 = {1,2,3,1,2,3};
        int k3 = 2;
        System.out.println(solution.containsNearbyDuplicate(nums3, k3)); // false

        int[] nums4 = {99,99};
        int k4 = 2;
        System.out.println(solution.containsNearbyDuplicate(nums4, k4)); // true
    }
}
