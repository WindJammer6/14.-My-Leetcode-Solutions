import java.util.ArrayList;
import java.util.Collections;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {

    public ArrayList<Integer> preOrderTraversalModified(TreeNode node, int level, ArrayList<Integer> leafNodeDepths){
        if (node == null){
            return leafNodeDepths;
        }
        System.out.println("Node value: " + node.val + ", Level: " + level);
        leafNodeDepths.add(level);
        preOrderTraversalModified(node.left, level+1, leafNodeDepths);
        preOrderTraversalModified(node.right, level+1, leafNodeDepths);

        System.out.println(leafNodeDepths);
        return leafNodeDepths;
    }

    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }

        ArrayList<Integer> leafNodeDepths = new ArrayList<>();
        leafNodeDepths = preOrderTraversalModified(root, 1, leafNodeDepths);
        int maxDepth = Collections.max(leafNodeDepths);
        return maxDepth;
    }
}


class TestSolution {
    public static void main (String args[]){
        TreeNode Tree1 = new TreeNode(3);

        TreeNode TreeNode1 = new TreeNode(9);
        Tree1.left = TreeNode1;
        TreeNode TreeNode2 = new TreeNode(20);
        Tree1.right = TreeNode2;
        TreeNode TreeNode3 = new TreeNode(15);
        TreeNode2.left = TreeNode3;
        TreeNode TreeNode4 = new TreeNode(7);
        TreeNode2.right = TreeNode4;

        TreeNode Tree2 = new TreeNode(1);

        TreeNode TreeNode5 = new TreeNode(2);
        Tree2.right = TreeNode5;

        Solution solution = new Solution();
        System.out.println(solution.maxDepth(Tree1));    // 3

        System.out.println(solution.maxDepth(Tree2));    // 2
    }
}