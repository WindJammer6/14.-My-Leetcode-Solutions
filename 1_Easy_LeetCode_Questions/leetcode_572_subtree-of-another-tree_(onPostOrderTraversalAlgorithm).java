import java.util.ArrayList;

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

    // Approach:
    // Do DFS on both binary tress, and get the array output that shows the traversal. If array
    // of smaller tree is exactly part of the array of larger main tree (i.e. the elements in the
    // array of smaller tree appears in succession pattern in the array of larger main tree),
    // then it is a subtree of the larger main tree
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        StringBuilder mainBuilder = new StringBuilder();

        postOrderTraversal(root, mainBuilder);
        String mainStr = mainBuilder.toString();
        System.out.println(mainStr);

        StringBuilder subBuilder = new StringBuilder();
        postOrderTraversal(subRoot, subBuilder);
        String subStr = subBuilder.toString();
        System.out.println(subStr);

        // Check if the elements in the array of smaller tree appears in succession pattern
        // in the array of larger main tree
        if (mainStr.contains(subStr)){
            return true;
        } else{
            return false;
        }
    }

    public void postOrderTraversal(TreeNode treeNode, StringBuilder sb){
        if (treeNode == null){
            sb.append("#,");        // represents null
            return;
        }

        postOrderTraversal(treeNode.left, sb);
        postOrderTraversal(treeNode.right, sb);
        sb.append(treeNode.val).append(",");
    }
}


class TestSolution {
    public static void main (String args[]){
        TreeNode Tree1 = new TreeNode(3);

        TreeNode TreeNode1 = new TreeNode(4);
        Tree1.left = TreeNode1;
        TreeNode TreeNode2 = new TreeNode(5);
        Tree1.right = TreeNode2;

        TreeNode TreeNode3 = new TreeNode(1);
        TreeNode1.left = TreeNode3;
        TreeNode TreeNode4 = new TreeNode(2);
        TreeNode1.right = TreeNode4;

        TreeNode Tree2 = new TreeNode(4);

        TreeNode TreeNode5 = new TreeNode(1);
        Tree2.left = TreeNode5;

        TreeNode TreeNode6 = new TreeNode(2);
        Tree2.right = TreeNode6;


        TreeNode Tree3 = new TreeNode(3);

        TreeNode TreeNode7 = new TreeNode(4);
        Tree3.left = TreeNode7;
        TreeNode TreeNode8 = new TreeNode(5);
        Tree3.right = TreeNode8;

        TreeNode TreeNode9 = new TreeNode(1);
        TreeNode7.left = TreeNode9;
        TreeNode TreeNode10 = new TreeNode(2);
        TreeNode7.right = TreeNode10;

        TreeNode TreeNode11 = new TreeNode(0);
        TreeNode10.left = TreeNode11;

        TreeNode Tree4 = new TreeNode(4);

        TreeNode TreeNode12 = new TreeNode(1);
        Tree4.left = TreeNode12;

        TreeNode TreeNode13 = new TreeNode(2);
        Tree4.right = TreeNode13;


        TreeNode Tree5 = new TreeNode(4);


        Solution solution = new Solution();
        System.out.println(solution.isSubtree(Tree1, Tree2));    // true
        System.out.println(solution.isSubtree(Tree3, Tree4));    // false
        System.out.println(solution.isSubtree(Tree1, Tree5));    // false
    }
}