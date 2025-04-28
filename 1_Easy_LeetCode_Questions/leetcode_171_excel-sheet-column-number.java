import java.util.HashMap;
import java.util.Map;

class Solution {

    // Pattern:
    //Label | Number
    //  A   |  1
    //  B   |  2
    //  ... | ...
    //  Z   |  26
    //  AA  |  27
    //  AB  |  28
    //  ... | ...
    //  AZ  |  52
    //  BA  |  53
    //  ... | ...
    //  BZ  |  78

    // Figuring out the general formula by doing observation/trial and error on different examples to
    // find patterns:
    
    // First example, let input be "ZY":
    // The pattern is lets say I have "ZY", the first character has already been through 26 rounds of 26
    // characters, since its at "Z", and the second character has been through zero rounds, but is currently
    // at the 25th character, "Y", "ZY" = 26 * 26 + 25 = 701

    // Second example, let input be "AAA":
    // The pattern is lets say I have "AAA", by observation/trial and error, "AAA" should have the
    // column number of 703, which is equal to 1 * 26^2 + 1 * 26^1 + 1 * 26^0

    // Third example, let input be "BAB":
    // The pattern is lets say I have "AAA", by observation/trial and error, "AAA" should have the
    // column number of 1380, which is equal to 2 * 26^2 + 1 * 26^1 + 2 * 26^0
    public int titleToNumber(String columnTitle) {

        Map<Character, Integer> alphabetToNumberMapping = new HashMap<>();
        alphabetToNumberMapping.put('A', 1);
        alphabetToNumberMapping.put('B', 2);
        alphabetToNumberMapping.put('C', 3);
        alphabetToNumberMapping.put('D', 4);
        alphabetToNumberMapping.put('E', 5);
        alphabetToNumberMapping.put('F', 6);
        alphabetToNumberMapping.put('G', 7);
        alphabetToNumberMapping.put('H', 8);
        alphabetToNumberMapping.put('I', 9);
        alphabetToNumberMapping.put('J', 10);
        alphabetToNumberMapping.put('K', 11);
        alphabetToNumberMapping.put('L', 12);
        alphabetToNumberMapping.put('M', 13);
        alphabetToNumberMapping.put('N', 14);
        alphabetToNumberMapping.put('O', 15);
        alphabetToNumberMapping.put('P', 16);
        alphabetToNumberMapping.put('Q', 17);
        alphabetToNumberMapping.put('R', 18);
        alphabetToNumberMapping.put('S', 19);
        alphabetToNumberMapping.put('T', 20);
        alphabetToNumberMapping.put('U', 21);
        alphabetToNumberMapping.put('V', 22);
        alphabetToNumberMapping.put('W', 23);
        alphabetToNumberMapping.put('X', 24);
        alphabetToNumberMapping.put('Y', 25);
        alphabetToNumberMapping.put('Z', 26);

        int columnNumber = 0;

        char[] columnTitleCharArray = columnTitle.toCharArray();

        for (int i = 0; i < columnTitleCharArray.length; i++){
//            System.out.println(Math.pow(26, (columnTitleCharArray.length - i - 1)));
            columnNumber += alphabetToNumberMapping.get(columnTitleCharArray[i]) * Math.pow(26, (columnTitleCharArray.length - i - 1));
        }

        return columnNumber;

    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        System.out.println(solution.titleToNumber("A")); // 2
        System.out.println(solution.titleToNumber("AB")); // 28
        System.out.println(solution.titleToNumber("ZY")); // 701
    }
}