class Solution {
    public boolean isPalindrome(String s) {

        // Replace any character that’s not a digit, a letter, or a whitespace character with an empty string
        s = s.replaceAll("\\p{Punct}", "");

        // Replace all whitespaces with an empty string
        s = s.replaceAll("\\s", "");

        // Bring a letters to lowercase
        s = s.toLowerCase();

        // Convert string to an array
        char[] charArray = s.toCharArray();

        // The two pointers
        int left = 0;
        int right = s.length() - 1;
        while (right > left){
            if (charArray[left] != charArray[right]) {
                return false;
            }

            right -= 1;
            left += 1;

            System.out.println(right);
            System.out.println(left);
        }

        return true;
    }
}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();
        String s1 = "A man, a plan, a canal: Panama";
        System.out.println(solution.isPalindrome(s1));    // true

        String s2 = "race a car";
        System.out.println(solution.isPalindrome(s2));    // false

        String s3 = " ";
        System.out.println(solution.isPalindrome(s3));    // true
    }
}