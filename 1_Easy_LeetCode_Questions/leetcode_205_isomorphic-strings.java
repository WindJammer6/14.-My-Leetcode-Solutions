import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class Solution{
    public boolean isIsomorphic(String s, String t){
        Map<Character, Character> alphabetMapping = new HashMap<>();
        ArrayList<Character> mappedAlphabets = new ArrayList<>();
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        for (int i = 0; i < s.length(); i++) {

//            System.out.println(alphabetMapping.get(sArray[i]));
//            System.out.println(tArray[i]);

            if (alphabetMapping.containsKey(sArray[i]) == false) {

                // Check if there is any mapping to the same character
                if (mappedAlphabets.contains(tArray[i]) == false) {
                    alphabetMapping.put(sArray[i], tArray[i]);
                    mappedAlphabets.add(tArray[i]);
                } else {
                    return false;
                }

            } else {

                // Comparing each element in string s and t
                if (alphabetMapping.get(sArray[i]) != tArray[i]){
                    return false;
                }
            }
        }

        return true;
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        System.out.println(solution.isIsomorphic("egg", "add"));        // true
        System.out.println(solution.isIsomorphic("foo", "bar"));        // false
        System.out.println(solution.isIsomorphic("paper", "title"));    // true
        System.out.println(solution.isIsomorphic("badc", "baba"));      // false
    }
}