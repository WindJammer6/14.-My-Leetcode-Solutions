import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> arrayList = new ArrayList<>();

        if (nums.length == 0){
            return arrayList;
        }

        int leftIndex = 0;
        int rightIndex = 0;

        while (leftIndex < nums.length){
            rightIndex = leftIndex;

            while (rightIndex + 1 < nums.length){

                if (nums[rightIndex + 1] == nums[rightIndex] + 1){
                    rightIndex += 1;
                } else{
                    break;
                }
            }

            System.out.println("rightIndex: " + rightIndex);
            System.out.println("leftIndex: " + leftIndex);

            if (leftIndex == rightIndex){
                arrayList.add("" + nums[leftIndex]);
            } else {
                arrayList.add(nums[leftIndex] + "->" + nums[rightIndex]);
            }

            if (leftIndex == rightIndex){
                leftIndex += 1;
            } else {
                leftIndex = rightIndex + 1;
            }

        }


        return arrayList;
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {0,1,2,4,5,7};
        System.out.println(solution.summaryRanges(nums1).toString()); // ["0->2","4->5","7"]

        int[] nums2 = {0,2,3,4,6,8,9};
        System.out.println(solution.summaryRanges(nums2).toString()); // ["0","2->4","6","8->9"]
    }
}
