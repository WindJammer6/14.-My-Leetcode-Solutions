import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public boolean hasCycle(ListNode head) {
        // Visited nodes
        Set<ListNode> visitedNodes = new HashSet<ListNode>();

        // Iterating node
        ListNode iteratingNode = head;

        if (iteratingNode == null){
            return false;
        }

        // Iterate through the linked list
        while (!(visitedNodes.contains(iteratingNode))){
            visitedNodes.add(iteratingNode);
            iteratingNode = iteratingNode.next;

            if (iteratingNode == null){
                return false;
            }
        }
        return true;
    }
}

class TestSolution {
    public static void main (String args[]){
        // Build Linked List 1
        ListNode linkedListNode1 = new ListNode(3);
        ListNode linkedListNode2 = new ListNode(2);
        ListNode linkedListNode3 = new ListNode(0);
        ListNode linkedListNode4 = new ListNode(-4);

        linkedListNode1.next = linkedListNode2;
        linkedListNode2.next = linkedListNode3;
        linkedListNode3.next = linkedListNode4;
        linkedListNode4.next = linkedListNode2;

        Solution solution = new Solution();
        System.out.println(solution.hasCycle(linkedListNode1));     // true


        // Build Linked List 2
        ListNode linkedListNode5 = new ListNode(1);
        ListNode linkedListNode6 = new ListNode(2);

        linkedListNode5.next = linkedListNode6;
        linkedListNode6.next = linkedListNode5;
        System.out.println(solution.hasCycle(linkedListNode5));     // true


        // Build Linked List 3
        ListNode linkedListNode7 = new ListNode(1);
        System.out.println(solution.hasCycle(linkedListNode7));     // false
    }
}