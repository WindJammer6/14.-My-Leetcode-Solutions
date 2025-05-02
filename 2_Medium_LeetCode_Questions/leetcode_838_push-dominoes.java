import java.util.Arrays;

class Solution {

    // Approach 1: My Brute-force Nearest Influence approach (dosen't work, exceeds time limit since this approach is O(n^2))

    // Using a hint from the discussion section: Think of the "." dominoes in terms of how far away they are
    // from the influential dominoes. Think of distance as influence and only the nearest influential domino
    // can exert control. Add all influences for both directions.

    // My Approach:
    // 1. iterate through the string
    // 2. if it is L or R, then do nothing
    // 3. else, it must be a '.', then look for closest (if there is any) L or R leftwards and rightwards
    //    (using Two Pointers)
    //    Cases: (see the multiple cases below)


    // Multiple cases for closest leftward and closest rightward:
    // Case 1: L and L      => L
    // Case 2: R and R      => R
    // Case 3: '.' and '.'  => '.'

    // Case 4: L and R      => '.'
    // Case 5: R and L      => Depends on distance

    // Case 6: '.' and L    => L
    // Case 7: L and '.'    => '.'

    // Case 8: '.' and R    => '.'
    // Case 9: R and '.'    => R
    public char searchNearestLorR(char[] charArray, int index){
        char[] array = new char[2];
        array[0] = '.';
        array[1] = '.';

        int leftIndex = index;
        int rightIndex = index;

        int distanceLeftWard = 0;
        int distanceRightWard = 0;

        // Search leftward
        while (leftIndex > 0){
            leftIndex -= 1;
            distanceLeftWard += 1;

            if (rightIndex <= 0){
                array[0] = '.';
                break;
            }

            if (charArray[leftIndex] == 'L'){
                array[0] = 'L';
                break;
            }

            if (charArray[leftIndex] == 'R'){
                array[0] = 'R';
                break;
            }
        }

        // Search rightward
        while (rightIndex < charArray.length){
            rightIndex += 1;
            distanceRightWard += 1;

            if (rightIndex >= charArray.length){
                array[1] = '.';
                break;
            }

            if (charArray[rightIndex] == 'L'){
                array[1] = 'L';
                break;
            }

            if (charArray[rightIndex] == 'R'){
                array[1] = 'R';
                break;
            }
        }

        System.out.println(Arrays.toString(array));

        // Case 1: L and L      => L
        if ((array[0] == 'L') && (array[1] == 'L')){
            return 'L';
        }

        // Case 2: R and R      => R
        else if ((array[0] == 'R') && (array[1] == 'R')){
            return 'R';
        }

        // Case 3: '.' and '.'  => '.'
        else if ((array[0] == '.') && (array[1] == '.')){
            return '.';
        }

        // Case 4: L and R      => '.'
        else if ((array[0] == 'L') && (array[1] == 'R')){
            return '.';
        }

        // Case 5: R and L      => Depends on distance
        else if ((array[0] == 'R') && (array[1] == 'L')){
            if (distanceLeftWard > distanceRightWard) {
                return 'L';
            } else if (distanceLeftWard < distanceRightWard) {
                return 'R';
            } else {
                return '.';
            }
        }

        // Case 6: '.' and L    => L
        else if ((array[0] == '.') && (array[1] == 'L')){
            return 'L';
        }

        // Case 7: L and '.'    => '.'
        else if ((array[0] == 'L') && (array[1] == '.')){
            return '.';
        }

        // Case 8: '.' and R    => '.'
        else if ((array[0] == '.') && (array[1] == 'R')){
            return '.';
        }

        // Case 9: R and '.'    => R
        else if ((array[0] == 'R') && (array[1] == '.')){
            return 'R';
        }

        else {
            return '.';
        }

    }

    public String pushDominoes1(String dominoes) {
        char[] dominoesArray = dominoes.toCharArray();
        char[] dominoesArrayCopy = dominoesArray.clone();

        for (int i = 0; i < dominoesArray.length; i++){
            if (dominoesArray[i] == '.') {
                dominoesArrayCopy[i] = searchNearestLorR(dominoesArray, i);
            }
        }

        String dominoesArrayCopyString = new String(dominoesArrayCopy);
        return dominoesArrayCopyString;

    }


    // Approach 2: Two Pass Forces approach (works, O(n))

    // Approach:
    // The 2-passes method is a fast and elegant way to solve the domino push problem in O(n)
    // time using a physics-inspired approach:

    // First pass: Simulate the influence of 'R' dominoes pushing right
    // Second pass: Simulate the influence of 'L' dominoes pushing left
    // Final pass: Combine the two "forces" to decide what each domino becomes

    // Each domino gets a net force:
    // + force from 'R' (right push)
    // - force from 'L' (left push)

    // The domino "falls" in the direction of the stronger force
    public String pushDominoes2(String dominoes) {
        char[] dominoesArray = dominoes.toCharArray();
        int[] dominoesRightSweepArrayCopy = new int[dominoes.length()];
        int[] dominoesLeftSweepArrayCopy = new int[dominoes.length()];
        int[] dominoesCombinedArrayCopy = new int[dominoes.length()];
        char[] dominoesFinalArrayCopy = new char[dominoes.length()];

        int force;

        // First pass (from left to right, creating the right force)
        force = 0;
        for (int i = 0; i < dominoes.length(); i++){
            if (dominoesArray[i] == 'R') {
                force = dominoesArray.length;
            } else if (dominoesArray[i] == 'L') {
                force = 0;
            } else {
                force = Math.max(force - 1, 0);
            }
            dominoesRightSweepArrayCopy[i] = force;
        }

        // Second pass (from right to left, creating the left force)
        force = 0;
        for (int i = dominoes.length() - 1; i >= 0; i--){
            if (dominoesArray[i] == 'L') {
                force = dominoesArray.length;
            } else if (dominoesArray[i] == 'R') {
                force = 0;
            } else {
                force = Math.max(force - 1, 0);
            }
            dominoesLeftSweepArrayCopy[i] = -force;
        }

        // Combining the two passes
        for (int i = 0; i < dominoes.length(); i++){
            dominoesCombinedArrayCopy[i] = dominoesLeftSweepArrayCopy[i] + dominoesRightSweepArrayCopy[i];
        }
        System.out.println(Arrays.toString(dominoesCombinedArrayCopy));

        // Creating the final dominoes Array
        for (int i = 0; i < dominoes.length(); i++){
            if (dominoesCombinedArrayCopy[i] == 0){
                dominoesFinalArrayCopy[i] = '.';
            } else if (dominoesCombinedArrayCopy[i] < 0) {
                dominoesFinalArrayCopy[i] = 'L';
            } else {
                dominoesFinalArrayCopy[i] = 'R';
            }
        }

        String dominoesFinalArrayCopyString = new String(dominoesFinalArrayCopy);
        return dominoesFinalArrayCopyString;
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        System.out.println(solution.pushDominoes1("RR.L")); // "RR.L"
        System.out.println(solution.pushDominoes1(".L.R...LR..L..")); // "LL.RR.LLRRLL.."
        System.out.println(solution.pushDominoes1(".L.R.")); // "LL.RR"

        System.out.println(solution.pushDominoes2("RR.L")); // "RR.L"
        System.out.println(solution.pushDominoes2(".L.R...LR..L..")); // "LL.RR.LLRRLL.."
        System.out.println(solution.pushDominoes2(".L.R.")); // "LL.RR"
    }
}
