import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int nums1Pointer = 0;
        int nums2Pointer = 0;
        int iteratorPointer = 0;

        int[] nums1Copy = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++){
            nums1Copy[i] = nums1[i];
        }

        while ((nums1Pointer < m) && (nums2Pointer < n)) {
            if (nums2.length == 0){
                break;
            }

            int currentNums1PointerElement = nums1Copy[nums1Pointer];
            int currentNums2PointerElement = nums2[nums2Pointer];

//            System.out.println("");
//            System.out.println(String.format("This is the nums1Pointer: %d", nums1Pointer));
//            System.out.println(String.format("This is the nums2Pointer: %d", nums2Pointer));
//            System.out.println(String.format("This is the currentNums1PointerElement: %d", currentNums1PointerElement));
//            System.out.println(String.format("This is the currentNums2PointerElement: %d", currentNums2PointerElement));

            if (currentNums1PointerElement > currentNums2PointerElement){
                nums1[iteratorPointer] = currentNums2PointerElement;
                nums2Pointer += 1;
                iteratorPointer += 1;
            } else{
                nums1[iteratorPointer] = currentNums1PointerElement;
                nums1Pointer += 1;
                iteratorPointer += 1;
            }
        }

//        System.out.println(String.format("This is the iterativePointer: %d", iteratorPointer));
//        System.out.println(String.format("This is the nums1Pointer: %d", nums1Pointer));
//        System.out.println(String.format("This is the nums2Pointer: %d", nums2Pointer));

        while (nums1Pointer < m) {
            nums1[iteratorPointer] = nums1Copy[nums1Pointer];
            nums1Pointer += 1;
            iteratorPointer += 1;
        }

        while (nums2Pointer < n) {
            nums1[iteratorPointer] = nums2[nums2Pointer];
            nums2Pointer += 1;
            iteratorPointer += 1;
        }
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1a = {1, 2, 3, 0, 0, 0};
        int[] nums2a = {2, 5, 6};
        solution.merge(nums1a, 3, nums2a, 3);
        System.out.println(Arrays.toString(nums1a)); // [1, 2, 2, 3, 5, 6]

        int[] nums1b = {1};
        int[] nums2b = {};
        solution.merge(nums1b, 1, nums2b, 0);
        System.out.println(Arrays.toString(nums1b)); // [1]

        int[] nums1c = {0};
        int[] nums2c = {1};
        solution.merge(nums1c, 0, nums2c, 1);
        System.out.println(Arrays.toString(nums1c)); // [1]

        int[] nums1d = {4, 5, 6, 0, 0, 0};
        int[] nums2d = {1, 2, 3};
        solution.merge(nums1d, 3, nums2d, 3);
        System.out.println(Arrays.toString(nums1d)); // [1, 2, 3, 4, 5, 6]

        int[] nums1e = {-1, 0, 0, 3, 3, 3, 0, 0, 0};
        int[] nums2e = {1, 2, 2};
        solution.merge(nums1e, 6, nums2e, 3);
        System.out.println(Arrays.toString(nums1e)); // [-1,0,0,1,2,2,3,3,3]
    }
}
