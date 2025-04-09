import java.util.ArrayList;

class Solution {
    public int hammingWeight(int n) {
        ArrayList<Integer> binaryArray = new ArrayList<Integer>();

        // Code to convert a decimal to binary
        // Source: https://www.geeksforgeeks.org/program-decimal-binary-conversion/ (GeekforGeeks)
        // Using Approach 1: Division by 2 (O(log n) Time Complexity and O(1) Space Complexity)
        // 1. Repeatedly divide the number by 2
        // 2. Record the remainder at each step (it will be 0 or 1)
        // 3. The binary number is the remainders in reverse order
        int number = n;
        while (number > 0){
            System.out.println(number);
            if (number % 2 == 0){
                binaryArray.add(0, 0);
            } else {
                binaryArray.add(0, 1);
            }

            number = number / 2;
        }
        System.out.println(binaryArray);


        // Count the number of '1's in the binaryArray
        int counter = 0;
        for (int i = 0; i < binaryArray.size(); i++){
            if (binaryArray.get(i) == 1){
                counter += 1;
            }
        }
        return counter;
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        System.out.print(solution.hammingWeight(11));    // 3
        System.out.print(solution.hammingWeight(128));    // 1
        System.out.print(solution.hammingWeight(2147483645));    // 30
    }
}