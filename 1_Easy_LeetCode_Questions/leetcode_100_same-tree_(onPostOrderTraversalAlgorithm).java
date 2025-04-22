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

    public boolean isSameTree(TreeNode p, TreeNode q) {
        StringBuilder sb1 = new StringBuilder("");
        postOrderTraversal(p, sb1);
        String s1 = sb1.toString();

        StringBuilder sb2 = new StringBuilder("");
        postOrderTraversal(q, sb2);
        String s2 = sb2.toString();

        System.out.println(s1);
        System.out.println(s2);

        if (s1.equals(s2)){
            return true;
        } else{
            return false;
        }
    }

    // Approach:
    // Do DFS on the binary tres, and get the array output that shows the traversal, using '#' which helps
    // to maintain structural information of the binary tree in the array output. 
    
    // If both output arrays are the same, they are the same tree.
    public void postOrderTraversal(TreeNode treeNode, StringBuilder sb){
        if (treeNode == null){
            sb.append('#');         // represents null
            return;
        }

        postOrderTraversal(treeNode.left, sb);
        postOrderTraversal(treeNode.right, sb);
        sb.append(treeNode.val).append(",");
    }
}


class TestSolution {
    public static void main (String args[]){
        TreeNode Tree1 = new TreeNode(1);

        TreeNode TreeNode1 = new TreeNode(2);
        Tree1.left = TreeNode1;
        TreeNode TreeNode2 = new TreeNode(3);
        Tree1.right = TreeNode2;

        TreeNode Tree2 = new TreeNode(1);

        TreeNode TreeNode3 = new TreeNode(2);
        Tree2.left = TreeNode3;
        TreeNode TreeNode4 = new TreeNode(3);
        Tree2.right = TreeNode4;



        TreeNode Tree3 = new TreeNode(1);

        TreeNode TreeNode5 = new TreeNode(2);
        Tree3.left = TreeNode5;

        TreeNode Tree4 = new TreeNode(1);

        TreeNode TreeNode6 = new TreeNode(3);
        Tree4.right = TreeNode6;



        TreeNode Tree5 = new TreeNode(1);

        TreeNode TreeNode7 = new TreeNode(2);
        Tree5.left = TreeNode7;
        TreeNode TreeNode8 = new TreeNode(1);
        Tree5.right = TreeNode8;

        TreeNode Tree6 = new TreeNode(1);

        TreeNode TreeNode9 = new TreeNode(1);
        Tree6.left = TreeNode9;
        TreeNode TreeNode10 = new TreeNode(2);
        Tree6.right = TreeNode10;


        Solution solution = new Solution();
        System.out.println(solution.isSameTree(Tree1, Tree2));    // true
        System.out.println(solution.isSameTree(Tree3, Tree4));    // false
        System.out.println(solution.isSameTree(Tree5, Tree6));    // false
    }
}
