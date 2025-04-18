// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {

    public TreeNode invertTree(TreeNode root) {
        postOrderTraversal(root);
        return root;
    }

    // Approach:
    // Do DFS on the binary tres, and during the traversal, make the left child become
    // the right child, and the right child to become the left child
    public void postOrderTraversal(TreeNode treeNode){
        if (treeNode == null){
            return;
        }

        postOrderTraversal(treeNode.left);
        postOrderTraversal(treeNode.right);

        TreeNode leftCopy = treeNode.left;
        TreeNode rightCopy = treeNode.right;

        treeNode.left = rightCopy;
        treeNode.right = leftCopy;
    }
}


class TestSolution {
    public static void main (String args[]){
        TreeNode Tree1 = new TreeNode(4);

        TreeNode TreeNode1 = new TreeNode(2);
        Tree1.left = TreeNode1;
        TreeNode TreeNode2 = new TreeNode(7);
        Tree1.right = TreeNode2;

        TreeNode TreeNode3 = new TreeNode(1);
        TreeNode1.left = TreeNode3;
        TreeNode TreeNode4 = new TreeNode(3);
        TreeNode1.right = TreeNode4;

        TreeNode TreeNode5 = new TreeNode(6);
        TreeNode2.left = TreeNode3;
        TreeNode TreeNode6 = new TreeNode(9);
        TreeNode2.right = TreeNode4;


        TreeNode Tree2 = new TreeNode(2);

        TreeNode TreeNode7 = new TreeNode(1);
        Tree2.left = TreeNode7;
        TreeNode TreeNode8 = new TreeNode(3);
        Tree2.right = TreeNode8;


        Solution solution = new Solution();
        System.out.println(solution.invertTree(Tree1));    // Tree1
        System.out.println(solution.invertTree(Tree2));    // Tree2
    }
}