// Using the approach from this Leetcode solution using Trie Data Structure and Top-Down Dynamic Programming
// (memoization):
// Source:
// https://leetcode.com/problems/word-break/solutions/6690289/trie-with-memoization/?envType=problem-list-v2&envId=oizxjoit
// (Leetcode)

// Approach:
// 1. Build a Trie from the given word dictionary.
// 2. Recursively check if the string can be segmented starting from index 0.
// 3. At each recursive call:
//    3a. Start from the current Trie node (initially root).
//    3b. Move through the Trie matching characters of s starting at the current index.
//    3c. If at any point the Trie node marks the end of a word (isEnd == true), try to segment the
//        remaining string starting from the root node again.
// 4. Use a memoization map keyed by (index, Trie node) to store results and avoid recomputation.



// The top-down dynamic programming (with memoization) code is partially taken from my school's
// lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
// and base cases for this question and modified the top-down dynamic programming (with memoization)
// code to this context to answer this question

// Analyzing for potential patterns for the question with trial and error: NIL

// Subproblems to solve:
// “Can string s up to index k be segmented into a space-separated sequence of one or more dictionary
// words?

// So to determine if for string s to index k can be segmented into a space-separated sequence of one or
// more dictionary words:
//          To determine if s[0:i] can be broken, loop through all possible split points j from 0 to i,
//          and check:
//          - If s[0:j] can be broken (DP[j] == true), and
//          - If s[j:i] is a valid word in the dictionary,
//            then set DP[i] = true.

// We want to compute this for all j from 1 up to i.


// Recurrence:
//          To determine if s[0:i] can be broken, loop through all possible split points j from 0 to i,
//          and check:
//          - If s[0:j] can be broken (DP[j] == true), and
//          - If s[j:i] is a valid word in the dictionary,
//            then set DP[i] = true.


// Base case(s):
// - if j = s.length, DP(j) = true


// Using top-down approach (with memoization):
// Pseudocode:
//	Initialize 𝑚𝑒𝑚𝑜 = {}

//  function word_break(s, wordList):
//	Require: s is a string
//  1. TrieNode root = TRIE_DATA_STRUCTURE of the words in with 'wordList';
//  2. return wordBreakRecursiveChecker(s, j, root, 𝑚𝑒𝑚𝑜)


// wordBreakRecursiveChecker(s, j, root, 𝑚𝑒𝑚𝑜)
//  Let j be current index
//  Let i be end index

//	1. if j in 𝑚𝑒𝑚𝑜 then:
//  2.  	return 𝑚𝑒𝑚𝑜[j]
//	3. if j == s.length then:
//	4.  	𝑚𝑒𝑚𝑜[j] ← true
//  5.  	return true

//  6. TrieNode currentTrieNode = root

//  7. for k from j to i, do
//  8.     if s[k] not in iterator.childrens:
//  9.         break

// 10.     currentTrieNode = currentTrieNode.contains.get(s[k])
//
// 11.     if iterator.isWord == true:
// 12.         if wordBreakRecursiveChecker(s, k + 1, root, 𝑚𝑒𝑚𝑜) == true
// 13.                𝑚𝑒𝑚𝑜[j] = true
// 14.                return true

// 15. 𝑚𝑒𝑚𝑜[j] = false
// 16. return false



import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;
import java.util.Stack;


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


class Solution {

    public boolean wordBreak(String s, List<String> wordDict) {
        Map<Integer, Boolean> memo = new HashMap<>();

        Trie trie = new Trie();

        // Build the Trie Data Structure
        for (String word : wordDict) {
            trie.insert(word);
        }
        trie.print();

        return wordBreakRecursiveChecker(s, 0, trie.root, memo);

    }


    public boolean wordBreakRecursiveChecker(String s, int j, TrieNode root, Map<Integer, Boolean> memo){
        j = j;
        int i = s.length();

        if (memo.containsKey(j)){
            return memo.get(j);
        }

        if (j == s.length()){
            memo.put(j, true);
            return true;
        }

        TrieNode iterator = root;

        for (int k = j; k < i; k++){
            if (iterator.childrens.containsKey(s.charAt(k)) == false){
                break;
            }

            iterator = iterator.childrens.get(s.charAt(k));

            if (iterator.isWord == true){
                if (wordBreakRecursiveChecker(s, k+1, root, memo) == true){
                    memo.put(j, true);
                    return true;
                }
            }
        }

        memo.put(j, false);
        return false;
    }
}



class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        List<String> wordDict1 = new ArrayList<>();
        wordDict1.add("leet");
        wordDict1.add("code");
        System.out.println(solution.wordBreak("leetcode", wordDict1)); // true

        List<String> wordDict2 = new ArrayList<>();
        wordDict2.add("apple");
        wordDict2.add("pen");
        System.out.println(solution.wordBreak("applepenapple", wordDict2)); // true

        List<String> wordDict3 = new ArrayList<>();
        wordDict3.add("cats");
        wordDict3.add("dog");
        wordDict3.add("sand");
        wordDict3.add("and");
        wordDict3.add("cat");
        System.out.println(solution.wordBreak("catsandog", wordDict3)); // false
    }
}
