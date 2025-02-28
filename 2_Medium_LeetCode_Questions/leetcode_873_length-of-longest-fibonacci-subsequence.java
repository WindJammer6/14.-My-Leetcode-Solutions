import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class test{
    public static void main(String[] args){
        Solution solution = new Solution();
        int[] arr = {1,2,3,4,5,6,7,8};  // 5, {1,2,3,5,8}
        int[] arr2 = {1,3,7,11,12,14,18}; // 3, {7,11,18}
        int[] arr3 = {2,4,7,8,9,10,14,15,18,23,32,50}; // 5, {4,14,18,32,50}
        int[] arr4 = {1,3,5}; // 0

        System.out.println(solution.lenLongestFibSubseq(arr));
        System.out.println(solution.lenLongestFibSubseq(arr2));
        System.out.println(solution.lenLongestFibSubseq(arr3));
        System.out.println(solution.lenLongestFibSubseq(arr4));

        // Expected outputs:
        // - Example 1:
        //   Input: arr = [1,2,3,4,5,6,7,8]
        //   Output: 5
        //   Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

        // - Example 2:
        //   Input: arr = [1,3,7,11,12,14,18]
        //   Output: 3
        //   Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
    }

}

// Improved solution with the implementation of a Hash Table and using the 'containsKey' function
// for O(1) search operation on the Hash Table instead of O(n) search operation on the ArrayList
// in the previous solution
class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        ArrayList<Integer> tempArrayList = new ArrayList<Integer>();
        Map<Integer, Integer> tempHashMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < arr.length; i++){
            tempHashMap.put(arr[i], i);
        }

        int lengthOfLongestSubstring = 0;

        for (int j = 0; j < arr.length - 1; j++) {

            for (int z = j + 1; z < arr.length; z++) {
                tempArrayList = new ArrayList<>();
                int indexOne = j;
                int indexTwo = z;
                tempArrayList.add(arr[indexOne]);
                tempArrayList.add(arr[indexTwo]);

                int sumOfIndexOneElementAndIndexTwoElement = arr[j] + arr[z];

                while (indexTwo != arr.length-1){
                    if (tempHashMap.containsKey(sumOfIndexOneElementAndIndexTwoElement) == true) {
                        tempArrayList.add(sumOfIndexOneElementAndIndexTwoElement);
                        int indexThree = tempHashMap.get(sumOfIndexOneElementAndIndexTwoElement);
                        indexOne = indexTwo;
                        indexTwo = indexThree;

                        sumOfIndexOneElementAndIndexTwoElement = arr[indexOne] + arr[indexTwo];
                        // System.out.print(sumOfIndexOneElementAndIndexTwoElement);
                        // System.out.println("marker");
                    }
                    else{
                        break;
                    };
                }

                if (lengthOfLongestSubstring < tempArrayList.size()) {
                    lengthOfLongestSubstring = tempArrayList.size();
                }

//                String listString = tempArrayList.toString();
//                System.out.println(listString);
            }
        }

        if (lengthOfLongestSubstring == 2) {
            return 0;
        } else {
            return lengthOfLongestSubstring;
        }
    }
}


// Triple for loop brute force method with ArrayList only. Don't work and exceeds the time limit for
// the longer test cases
class Solution2 {
    public int lenLongestFibSubseq(int[] arr) {
        ArrayList<Integer> tempArrayList = new ArrayList<>();

        int lengthOfLongestSubstring = 0;

        for (int j = 0; j < arr.length - 1; j++) {

            for (int z = j + 1; z < arr.length; z++) {
                tempArrayList = new ArrayList<>();
                int indexOne = j;
                int indexTwo = z;
                tempArrayList.add(arr[indexOne]);
                tempArrayList.add(arr[indexTwo]);

                for (int i = z + 1; i < arr.length; i++) {
//                    System.out.println(indexOne);
//                    System.out.println(indexTwo);
//                    System.out.printf("%d + %d = %d", arr[indexOne], arr[indexTwo], arr[i]);
                    if (arr[indexOne] + arr[indexTwo] == arr[i]) {
                        tempArrayList.add(arr[i]);
                        indexOne = indexTwo;
                        indexTwo = i;
                    }


                    if (lengthOfLongestSubstring < tempArrayList.size()) {
                        lengthOfLongestSubstring = tempArrayList.size();
                    }

//                    String listString = tempArrayList.toString();
//                    System.out.println(listString);
                }
            }
        }

        if (lengthOfLongestSubstring == 2) {
            return 0;
        } else {
            return lengthOfLongestSubstring;
        }
    }
}