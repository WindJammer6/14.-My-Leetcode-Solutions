import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countLargestGroup(int n) {
        Map<Integer, ArrayList<Integer>> groups = new HashMap<>();

        for (int i = 1; i < n + 1; i++) {
            String stringNum = String.valueOf(i);
            char[] charNum = stringNum.toCharArray();

            int addition = 0;
            for (char c : charNum) {
                int cNum = Integer.parseInt(String.valueOf(c));
                addition += cNum;
            }

            if (groups.containsKey(addition) == true) {
                ArrayList<Integer> group = groups.get(addition);

                group.add(i);
            } else {
                ArrayList<Integer> newGroup = new ArrayList<>();
                newGroup.add(i);
                groups.put(addition, newGroup);
            }

            System.out.println(groups.values());
        }

//        System.out.println(groups.values());
//        System.out.println(groups.keySet());

        int maxSize = 0;
        for (ArrayList<Integer> arr : groups.values()){
            if (arr.size() > maxSize) {
                maxSize = arr.size();
            }
        }

        int count = 0;
        for (ArrayList<Integer> arr : groups.values()){
            if (arr.size() == maxSize) {
                count += 1;
            }
        }

        return count;
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        System.out.println(solution.countLargestGroup(13));     // 4
        System.out.println(solution.countLargestGroup(2));      // 2
        System.out.println(solution.countLargestGroup(24));     // 5
        System.out.println(solution.countLargestGroup(40));     // 1
        System.out.println(solution.countLargestGroup(264));    // 2
    }
}

// This question's logic: Why when input n = 24, output is 5?
// 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24

// [1,10], [2,11,20], [3,12,21], [4,13,22], [5,14,23], [6,15,24], [7,16], [8,17], [9,18], [19]