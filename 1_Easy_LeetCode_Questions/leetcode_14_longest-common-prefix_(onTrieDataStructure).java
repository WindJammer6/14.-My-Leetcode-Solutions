import java.util.AbstractMap;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

// Approach 1: Brute force method (works)
class Solution {
    public String longestCommonPrefix(String[] strs) {
        int[] lengthArray = new int[strs.length];

        // Step 1: Initialize an array to store lengths of each string
        for (int i = 0; i < strs.length; i++){
            lengthArray[i] = strs[i].length();
        }

        // Step 2: Find the shortest word in the array
        String shortestWord = "";
        int lengthOfShortestWord = Integer.MAX_VALUE;
        for (int i = 0; i < strs.length; i++){
            if (lengthArray[i] < lengthOfShortestWord){
                lengthOfShortestWord = lengthArray[i];
                shortestWord = strs[i];
            }
        }

        // Step 3: Character-by-character comparison up to length of shortest word
        for (int j = 0; j < lengthOfShortestWord; j++) {
            for (int i = 0; i < strs.length; i++) {
                // System.out.println(strs[i].charAt(j));
                // System.out.println(shortestWord.charAt(j));
                if (!(strs[i].charAt(j) == shortestWord.charAt(j))){
                    return shortestWord.substring(0, j);
                }
            }
        }

        // Step 4: If all characters matched up to the length of the shortest word,
        //         then the shortest word itself is the longest common prefix
        return shortestWord;
    }
}




// Approach 2: Using Trie Data Structure, with reference to the approach explained by this Leetcode solution (works)
// Source: https://leetcode.com/problems/longest-common-prefix/solutions/6614689/java-solution-using-trie/ (Leetcode)

// Approach:
// Trie is well known for solving prefix-related string problems efficiently.

// In my implementation, I built a Trie and added an extra variable called filled to each node. This variable keeps
// track of how many child nodes are present at a given node. It becomes very useful while traversing the Trie, especially
// when trying to determine if a node is a branching point.

//In the find() method, I start traversal from the root and continue moving down the Trie as long as the current node has
// exactly one child (filled == 1) and no word ends at that node (eow == false). This ensures that we only include
// characters that are common across all inserted strings. The traversal stops at the point where the common prefix
// ends — either because a word ends or multiple branches appear.



// Implementing the Trie Data Structure (code taken from my solution for Leetcode 208 - Implement Trie (Prefix Tree))
class TrieNode{

    Map<Character, TrieNode> childrens = new HashMap<>();

    boolean isWord = false;

    char character;

    TrieNode(){

    }

    TrieNode(char character){
        this.childrens = new HashMap<>();
        this.isWord = false;
        this.character = character;
    }

    TrieNode(HashMap<Character, TrieNode> childrens, boolean isWord, char character){
        this.childrens = childrens;
        this.isWord = isWord;
        this.character = character;
    }
}


class Trie {

    TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public void insert(String word) {
        char[] charArray = word.toCharArray();

        TrieNode iterator = this.root;

        for (int i = 0; i < charArray.length; i++){
            if (!iterator.childrens.containsKey(charArray[i])) {
                iterator.childrens.put(charArray[i], new TrieNode(charArray[i]));
            }

            iterator = iterator.childrens.get(charArray[i]);
        }

        iterator.isWord = true;
    }

    public boolean search(String word) {
        char[] charArray = word.toCharArray();

        TrieNode iterator = this.root;

        for (int i = 0; i < charArray.length; i++){
            if (!iterator.childrens.containsKey(charArray[i])) {
                return false;
            } else{
                iterator = iterator.childrens.get(charArray[i]);
            }
        }

        if (!iterator.isWord){
            return false;
        } else{
            return true;
        }
    }

    public boolean startsWith(String prefix) {
        char[] charArray = prefix.toCharArray();

        TrieNode iterator = this.root;

        for (int i = 0; i < charArray.length; i++){
            if (!iterator.childrens.containsKey(charArray[i])) {
                return false;
            } else{
                iterator = iterator.childrens.get(charArray[i]);
            }
        }

        return true;
    }

    public void delete(String word) {
        TrieNode current = root;
        Stack<Map.Entry<TrieNode, Character>> stack = new Stack<>();

        // Traverse the Trie and store the path
        for (char ch : word.toCharArray()) {
            if (!current.childrens.containsKey(ch)) {
                System.out.println("Word not in Trie Data Structure");
                return;
            }
            stack.push(new AbstractMap.SimpleEntry<>(current, ch));
            current = current.childrens.get(ch);
        }

        // If the final node is not a word, the word doesn't exist
        if (!current.isWord) {
            System.out.println("Word not in Trie Data Structure");
            return;
        }

        // Unmark the word
        current.isWord = false;

        // Clean up unnecessary nodes
        while (!stack.isEmpty()) {
            Map.Entry<TrieNode, Character> entry = stack.pop();
            TrieNode parent = entry.getKey();
            char ch = entry.getValue();
            TrieNode child = parent.childrens.get(ch);

            if (child.childrens.isEmpty() && !child.isWord) {
                parent.childrens.remove(ch);
            } else {
                break; // Stop if child has other children or is end of another word
            }
        }
    }


    // -------------------------
    // Print Trie Data Structure
    // -------------------------
    // Done by ChatGPT
    public void print() {
        printHelper(root, "", true);
    }

    private void printHelper(TrieNode node, String prefix, boolean isTail) {
        int size = node.childrens.size();
        int i = 0;
        for (Map.Entry<Character, TrieNode> entry : node.childrens.entrySet()) {
            TrieNode child = entry.getValue();
            char ch = entry.getKey();

            boolean isLast = (i == size - 1);
            System.out.println(prefix + (isTail ? "|-- " : "|-- ") + ch + (child.isWord ? " (*)" : ""));    // The (*) indicates the end of a valid word.

            // Recursive call with updated prefix
            printHelper(child, prefix + (isTail ? "    " : "|   "), isLast);
            i++;
        }
    }
}

class Solution2 {
    public String longestCommonPrefix(String[] strs) {
        Trie trie = new Trie();
        StringBuilder longestCommonPrefixString = new StringBuilder();

        for (String str : strs){
            if (str.isEmpty()) {
                return ""; // edge case fix
            }
            trie.insert(str);
        }

        TrieNode iterator = trie.root;

        while (!(iterator.childrens.isEmpty())){
            if (!(iterator.childrens.keySet().size() == 1) || iterator.isWord){
                break;
            } else{
                longestCommonPrefixString.append(iterator.childrens.keySet().toArray()[0]);
            }

            iterator = iterator.childrens.get(iterator.childrens.keySet().toArray()[0]);
        }

        return longestCommonPrefixString.toString();
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        String[] array1 = {"flower","flow","flight"};
        String[] array2 = {"dog","racecar","car"};
        String[] array3 = {"abca","aba","aaab"};

        System.out.println(solution.longestCommonPrefix(array1));    // "fl"
        System.out.println(solution.longestCommonPrefix(array2));    // ""
        System.out.println(solution.longestCommonPrefix(array3));    // "a"


        Solution2 solution2 = new Solution2();

        String[] array4 = {"flower","flow","flight"};
        String[] array5 = {"dog","racecar","car"};
        String[] array6 = {"abca","aba","aaab"};
        String[] array7 = {"ab","a"};

        System.out.println(solution2.longestCommonPrefix(array4));    // "fl"
        System.out.println(solution2.longestCommonPrefix(array5));    // ""
        System.out.println(solution2.longestCommonPrefix(array6));    // "a"
        System.out.println(solution2.longestCommonPrefix(array7));    // "a"
    }
}