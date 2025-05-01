// Using Hint 2: Try to use two-pointers. Set one pointer to the left and one to the right of the
// array. Always move the pointer that points to the lower line.

// Crucial part of this algorithm: Why do we 'Always move the pointer that points to the lower line'?
// How does this ensure we find the maximum amount of water, without missing any possible cases?

// As explained by this Leetcode solution, which proved that this algorithm works:
// Source:
// https://leetcode.com/problems/container-with-most-water/solutions/5139915/video-simple-two-pointer-solution/?envType=problem-list-v2&envId=oizxjoit
// (Leetcode)
// After that, we want to move one of the pointers. How can we judge it? It's simple. We want to keep
// taller height between left and right because there is a possibility that we will get max area with
// the taller height.

// In this case,
//          left vs right = 1 vs 7

// So we move the left pointer to next.
//          0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L             R
// max_area = 8

// We will repeat the same process until we break left < right condition. I'll speed up.
//          0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L             R
// max_area = 8
// current_area = 7 * 7 = 49
// max_area = max(8, 49) = 49
// Move R to next

//          0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L           R
// max_area = 49
// current_area = 6 * 3 = 18
// max_area = max(49, 18) = 49
// Move R to next

//          0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L         R
// max_area = 49
// current_area = 5 * 8 = 40
// max_area = max(49, 40) = 49
// Move L to next

// In the above case, we can also move R instead of L because L and Rare the same(= 8).
//         0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L       R
// max_area = 49
// current_area = 4 * 6 = 14
// max_area = max(49, 24) = 49
// Move L to next

//          0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L     R
// max_area = 49
// current_area = 3 * 2 = 6
// max_area = max(49, 6) = 49
// Move L to next

//          0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L   R
// max_area = 49
// current_area = 2 * 5 = 10
// max_area = max(49, 10) = 49
// Move L to next

//  0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L R
// max_area = 49
// current_area = 1 * 4 = 4
// max_area = max(49, 4) = 49
// Move L to next

// Now L and R are the same index. We stop iteration.
//  0,1,2,3,4,5,6,7,8 (= index)
//         [1,8,6,2,5,4,8,3,7]
//            L
//            R
// return 49
class Solution {
    public int maxArea(int[] height) {
        int leftIndex = 0;
        int rightIndex = height.length - 1;

        int amountOfWater;
        int mostAmountOfWater = 0;

        while (leftIndex < rightIndex) {
            amountOfWater = Math.min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex);
            System.out.println(amountOfWater);

            if (amountOfWater > mostAmountOfWater){
                mostAmountOfWater = amountOfWater;
            }

            if (Math.min(height[leftIndex], height[rightIndex]) == height[leftIndex]){
                leftIndex += 1;
            } else {
                rightIndex -= 1;
            }
        }

        return mostAmountOfWater;
    }
}



class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] height1 = {1,8,6,2,5,4,8,3,7};
        System.out.println(solution.maxArea(height1)); // 49

        int[] height2 = {1,1};
        System.out.println(solution.maxArea(height2)); // 1
    }
}
