// Implementing the Trie Data Structure:

// What is the Trie Data Structure?
// The trie data structure, also known as a prefix tree, is a tree-like data structure used for efficient
// retrieval of key-value pairs.

// Sources:
// - https://www.youtube.com/watch?v=-urNrIAQnNo&t=1s (Lukas Vyhnalek) (Youtube video by Lukas Vyhnalek
//   titled 'Trie Data Structure (EXPLAINED)')
// - https://www.geeksforgeeks.org/introduction-to-trie-data-structure-and-algorithm-tutorials/
//   (GeekforGeeks)

// The Trie Data Structure has 4 important operations/functions,
// 1. Insert:
// Add a word to the Trie - Iterates through the characters of the word. For each character, creates a
// child node if it doesn’t exist. At the end of the word, marks the final node as a complete word
// (isWord = true).
// => O(L) where L = word length

// 2. Search:
// Check if a word exists - Traverses through the Trie following each character of the word. If any
// character is missing, returns false. At the end, returns true only if isWord = true.
// => O(L)

// 3. Starts With - Check if any word starts with a given prefix	Similar to search, but does not
// require isWord = true — it returns true as long as all prefix characters exist in the Trie.
// => O(P) where P = prefix length

// 4. Delete:
// Remove a word - Traverses the Trie like search, and removes nodes recursively only if they are
// not shared with other words. Handles cleanup carefully to avoid breaking other words.
// => O(L) in best case; might require full traversal of shared nodes

import java.util.AbstractMap;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

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

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

class TestSolution {
    public static void main (String args[]) {
        Trie trie = new Trie();

        // Insert words
        trie.insert("apple");
        trie.insert("app");
        trie.insert("bat");
        trie.insert("batch");
        trie.insert("bath");
        trie.insert("banana");

        System.out.println("Initial Trie:");
        trie.print();
        // Output:
        // Initial Trie:
        //|-- a
        //    |-- p
        //    |   |-- p (*)
        //    |       |-- l
        //    |           |-- e (*)
        //|-- b
        //    |-- a
        //        |-- t (*)
        //            |-- c
        //            |   |-- h (*)
        //            |-- h (*)
        //        |-- n
        //            |-- a
        //                |-- n
        //                    |-- a (*)


        // Basic search
        System.out.println(trie.search("apple"));   // true
        System.out.println(trie.search("app"));     // true
        System.out.println(trie.search("bat"));     // true
        System.out.println(trie.search("batch"));   // true
        System.out.println(trie.search("bath"));    // true
        System.out.println(trie.search("banana"));  // true

        // False searches
        System.out.println(trie.search("appl"));    // false (prefix but not word)
        System.out.println(trie.search("bananas")); // false
        System.out.println(trie.search("b"));       // false
        System.out.println(trie.search("batman"));  // false

        // startsWith tests
        System.out.println(trie.startsWith("app"));     // true
        System.out.println(trie.startsWith("bat"));     // true
        System.out.println(trie.startsWith("ba"));      // true
        System.out.println(trie.startsWith("cat"));     // false
        System.out.println(trie.startsWith(""));        // true (empty string is prefix of everything)

        // Edge cases
        System.out.println(trie.search(""));      // false (empty string not inserted)
        System.out.println(trie.startsWith(""));        // true

        // Delete tests
        System.out.println("\nDeleting 'apple'...");
        trie.delete("apple");
        System.out.println(trie.search("apple"));  // false
        System.out.println(trie.search("app"));    // true (should still exist)

        System.out.println("\nDeleting 'app'...");
        trie.delete("app");
        System.out.println(trie.search("app"));    // false

        System.out.println("\nDeleting 'batch'...");
        trie.delete("batch");
        System.out.println(trie.search("batch"));  // false
        System.out.println(trie.search("bat"));    // true (should still exist)

        System.out.println("\nDeleting 'bat'...");
        trie.delete("bat");
        System.out.println(trie.search("bat"));    // false

        System.out.println("\nTrie after deletions:");
        trie.print();
        // Output:
        // Trie after deletions:
        //|-- b
        //    |-- a
        //        |-- t
        //            |-- h (*)
        //        |-- n
        //            |-- a
        //                |-- n
        //                    |-- a (*)
    }
}