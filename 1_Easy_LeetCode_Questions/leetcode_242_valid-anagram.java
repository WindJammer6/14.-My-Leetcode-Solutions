import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] charArrayS = s.toCharArray();
        char[] charArrayT = t.toCharArray();
        Arrays.sort(charArrayS);
        Arrays.sort(charArrayT);

        if (charArrayS.length != charArrayT.length){
            return false;
        }

        for (int i = 0; i < charArrayS.length; i++){
            if (charArrayS[i] != charArrayT[i]){
                return false;
            }
        }

        return true;
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        String s1 = "anagram";
        String t1 = "nagaram";
        System.out.println(solution.isAnagram(s1, t1));   // true

        String s2 = "rat";
        String t2 = "car";
        System.out.println(solution.isAnagram(s2, t2));   // false
    }
}