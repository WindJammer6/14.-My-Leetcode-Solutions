// Following the approach from this Leetcode solution:
// Source: https://leetcode.com/problems/sqrtx/solutions/3706594/easy-explained-solution-beats-100/ (Leetcode)

// Approach:
//  1. We first check if x is 0 or 1. If it is, we know that the square root of 0 and 1 is 0 
//    and 1 respectively, so we directly return x.
//  2. For any other value of x, we set up a search range between 1 and x. We initialize 
//    two variables start and end to represent the range.
//  3. Now comes the clever part: We use a while loop to repeatedly divide the search range 
//    in half (Binary Search) to find the square root.
//  4. In each iteration of the loop, we calculate the middle value mid using the formula 
//    start + (end - start) / 2. This formula ensures that we don't encounter any integer 
//    overflow when dealing with large values of x.
//  5. Next, we calculate the square of mid and compare it with x.
//  6. If the square of mid is greater than x, we know the square root lies in the lower half 
//    of the search range. So, we move the end pointer to the left to narrow down the search range.
//  7. If the square of mid is equal to x, we have found the square root! So, we return mid 
//    as the answer.
//  8. If the square of mid is less than x, we know the square root lies in the upper half 
//    of the search range. So, we move the start pointer to the right to continue the search.
//  9. We repeat steps 4 to 8 until the start pointer becomes greater than the end pointer. 
//    At this point, we have found the floor value of the square root, and end holds that value.
// 10. To ensure that we return the correct floor value of the square root, we round down 
//     the value of end to the nearest integer using the Math.round() method.

class Solution {
    public int mySqrt(int x) {
        if ((x == 0) || (x == 1)) {
            return x;
        }

        int squareRootOfX = binarySearchAlgorithmModified(x);

        return squareRootOfX;
    }

    // Binary Search Algorithm modified to fit the context of this question
    public int binarySearchAlgorithmModified(int x){
        int leftIndex = 0;
        int rightIndex = x - 1;
        int middleIndex;

        while (leftIndex <= rightIndex) {
            middleIndex = (leftIndex + rightIndex) / 2;
//            System.out.println(middleIndex);
//            System.out.println(rightIndex);
//            System.out.println(leftIndex);

            // Convert result to long datatype before squaring to avoid integer overflow
            // Without (long), middleIndex * middleIndex could face overflow for large x
            if ((long) middleIndex * middleIndex > x){
                rightIndex = middleIndex - 1;
            } else if ((long) middleIndex * middleIndex < x) {
                leftIndex = middleIndex + 1;
            } else {
                return middleIndex;
            }
        }

        return rightIndex;
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        System.out.println(solution.mySqrt(4));    // 2
        System.out.println(solution.mySqrt(8));    // 2
        System.out.println(solution.mySqrt(3));    // 1
        System.out.println(solution.mySqrt(2147395599));    // 46339
    }
}