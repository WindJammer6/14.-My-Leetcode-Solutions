import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

//Definition for a binary tree node.
class TreeNode2 {
    int val;
    TreeNode2 left;
    TreeNode2 right;
    TreeNode2() {}
    TreeNode2(int val) { this.val = val; }
    TreeNode2(int val, TreeNode2 left, TreeNode2 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


// Approach 1: Solving by converting the Binary Search Tree into an AVL Tree (dosen't work)
// It dosen't work because this Leetcode question wants a height-balanced BST, constructed using the
// midpoint approach. It compares the output tree’s structure and values, not just the values alone.

// Hence, while the AVL tree does work and is correct in algorithmic terms. It failed the Leetcode’s
// auto-grader since it expects a specific serialized structure.


// This question is effectively asking us to implement AVL Tree Data Structure, which is essentially
// a Binary Search Tree, but with an additional property on top of having the left child node being smaller
// than the current node and the right child node being larger than the current node, of being height-balanced

// To construct an AVL Tree, we need to modify the insert node to Binary Search Tree method, for it to also
// be able to re-balance the AVL Tree if the insertion causes it to become unbalanced for it to maintain its
// AVL Tree property of being height-balanced

// Essentially we are converting a regular insert Binary Search Tree node method, to an insert AVL Tree node
// method. Here is how its done, taking the approach from GeekforGeeks:
// Source:
// - https://www.geeksforgeeks.org/insertion-in-an-avl-tree/ (GeekforGeeks)

// 1. Perform the normal BST insertion.
// 2. The current node must be one of the ancestors of the newly inserted node. Update the height of the
//    current node.
// 3. Get the balance factor (left subtree height – right subtree height) of the current node.
// 4. If the balance factor is greater than 1, then the current node is unbalanced and we are either in
//    the Left Left case or left Right case. To check whether it is left left case or not, compare the
//    newly inserted key with the key in the left subtree root.
// 5. If the balance factor is less than -1, then the current node is unbalanced and we are either in the
//    Right Right case or Right-Left case. To check whether it is the Right Right case or not, compare
//    the newly inserted key with the key in the right subtree root.

// I decided to ignore the given definition for a binary tree node code, and implement my own AVL tree
// node code
// Definition for a AVL tree node.
class TreeNode1 {
    int val;
    TreeNode1 left;
    TreeNode1 right;
    int height;
    TreeNode1() {}
    TreeNode1(int val) { this.val = val; }
    TreeNode1(int val, TreeNode1 left, TreeNode1 right, int height) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.height = height;
    }
}

class Solution {

    //////////////////////////////////////////////////////
    // All these code taken from the GeekforGeeks source //
    //////////////////////////////////////////////////////
    // A utility function to get the
    // height of the tree
    static int height(TreeNode1 N) {
        if (N == null)
            return 0;
        return N.height;
    }

    // A utility function to right rotate
    // subtree rooted with y
    static TreeNode1 rightRotate(TreeNode1 y) {
        TreeNode1 x = y.left;
        TreeNode1 T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update heights
        y.height = 1 + Math.max(height(y.left),
                height(y.right));
        x.height = 1 + Math.max(height(x.left),
                height(x.right));

        // Return new root
        return x;
    }

    // A utility function to left rotate
    // subtree rooted with x
    static TreeNode1 leftRotate(TreeNode1 x) {
        TreeNode1 y = x.right;
        TreeNode1 T2 = y.left;

        // Perform rotation
        y.left = x;
        x.right = T2;

        // Update heights
        x.height = 1 + Math.max(height(x.left),
                height(x.right));
        y.height = 1 + Math.max(height(y.left),
                height(y.right));

        // Return new root
        return y;
    }

    // Get balance factor of node N
    static int getBalance(TreeNode1 N) {
        if (N == null)
            return 0;
        return height(N.left) - height(N.right);
    }

    // Recursive function to insert a val in
    // the subtree rooted with node
    static TreeNode1 insert(TreeNode1 node, int val) {

        // Perform the normal BST insertion
        if (node == null)
            return new TreeNode1(val);

        if (val < node.val)
            node.left = insert(node.left, val);
        else if (val > node.val)
            node.right = insert(node.right, val);
        else // Equal vals are not allowed in BST
            return node;

        // Update height of this ancestor node
        node.height = 1 + Math.max(height(node.left),
                height(node.right));

        // Get the balance factor of this ancestor node
        int balance = getBalance(node);

        // If this node becomes unbalanced,
        // then there are 4 cases

        // Left Left Case
        if (balance > 1 && val < node.left.val)
            return rightRotate(node);

        // Right Right Case
        if (balance < -1 && val > node.right.val)
            return leftRotate(node);

        // Left Right Case
        if (balance > 1 && val > node.left.val) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && val < node.right.val) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        // Return the (unchanged) node pointer
        return node;
    }

    // A utility function to print pre order
    // traversal of the tree
    static void preOrder(TreeNode1 root) {
        if (root != null) {
            preOrder(root.left);
            System.out.print(root.val + " ");
            preOrder(root.right);
        }
    }

    // A utility function to print Breadth First Search
    // traversal of the tree (Generated by ChatGPT)
    public List<Integer> flatLevelOrder1(TreeNode1 root) {
        List<Integer> result = new ArrayList<>();
        Queue<TreeNode1> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode1 node = queue.poll();

            if (node != null) {
                result.add(node.val);
                queue.add(node.left);
                queue.add(node.right);
            } else {
                result.add(null);
            }
        }

        // Optional: remove trailing nulls (to match Leetcode output)
        while (result.size() > 0 && result.get(result.size() - 1) == null) {
            result.remove(result.size() - 1);
        }

        return result;
    }

    public TreeNode1 sortedArrayToBST1(int[] nums) {
        TreeNode1 root = null;
        for (int val : nums) {
            root = insert(root, val);
        }
        return root;
    }


    //////////////////////////////////////////////////////////////////


    // Approach 2: With reference to a Leetcode solution (works)
    // Source:
    // https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/solutions/6025974/0-ms-runtime-beats-100-user-step-by-steps-solution-easy-to-understand/
    // (Leetcode)

    // Approach:
    // 1. Start with the whole array and calculate the middle index.
    // 2. Create a new tree node with the middle element as the value.
    // 3. Recursively apply the same approach to the left and right halves of the array.
    // 4. Attach the recursively created left and right nodes to the root node.
    // 5. Return the root of the tree.

    // Because you always set the middle index as the current node for each of the left and right
    // subtrees throughout the recursive loops, you ensure that the built Binary Search Tree stay
    // beight-balanced throughout the recursive loops
    public TreeNode2 sortedArrayToBST2(int[] nums) {
        return helper(nums, 0, nums.length - 1);
    }

    public TreeNode2 helper(int[] nums, int leftIndex, int rightIndex) {
        if (leftIndex > rightIndex) {
            return null;
        }

        int midIndex = (rightIndex + leftIndex) / 2;
        TreeNode2 root = new TreeNode2(nums[midIndex]);

        root.left = helper(nums, leftIndex, midIndex - 1);
        root.right = helper(nums, midIndex + 1, rightIndex);


        return root;
    }


    // A utility function to print Breadth First Search
    // traversal of the tree (Generated by ChatGPT)
    public List<Integer> flatLevelOrder2(TreeNode2 root) {
        List<Integer> result = new ArrayList<>();
        Queue<TreeNode2> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode2 node = queue.poll();

            if (node != null) {
                result.add(node.val);
                queue.add(node.left);
                queue.add(node.right);
            } else {
                result.add(null);
            }
        }

        // Optional: remove trailing nulls (to match Leetcode output)
        while (result.size() > 0 && result.get(result.size() - 1) == null) {
            result.remove(result.size() - 1);
        }

        return result;
    }


}

class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        int[] nums1 = {-10,-3,0,5,9};
        System.out.println(solution.flatLevelOrder1(solution.sortedArrayToBST1(nums1)));      // [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]

        int[] nums2 = {1,3};
        System.out.println(solution.flatLevelOrder1(solution.sortedArrayToBST1(nums2)));      // [1,null,3] or [3,1]


        int[] nums3 = {-10,-3,0,5,9};
        System.out.println(solution.flatLevelOrder2(solution.sortedArrayToBST2(nums3)));      // [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]

        int[] nums4 = {1,3};
        System.out.println(solution.flatLevelOrder2(solution.sortedArrayToBST2(nums4)));      // [1,null,3] or [3,1]
    }
}
