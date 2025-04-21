import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ArrayList<ListNode> arrayListOfListNodesInA = new ArrayList<>();

        ListNode iteratorA = headA;
        ListNode iteratorB = headB;

        while (iteratorA != null){
            arrayListOfListNodesInA.add(iteratorA);
            iteratorA = iteratorA.next;
        }

        Set<ListNode> setOfListNodesInA = new HashSet<ListNode>(arrayListOfListNodesInA);

        while (iteratorB != null){
//            System.out.println(iteratorB.val);

            if (setOfListNodesInA.contains(iteratorB)){
                return iteratorB;
            } else {
                iteratorB = iteratorB.next;
            }
        }

        return null;
    }
}


class TestSolution {
    public static void main (String args[]){
        // Shared part
        ListNode c1 = new ListNode(8);
        ListNode c2 = new ListNode(4);
        ListNode c3 = new ListNode(5);
        c1.next = c2;
        c2.next = c3;

        // List A: a1 -> a2 -> c1
        ListNode a1 = new ListNode(4);
        ListNode a2 = new ListNode(1);
        a1.next = a2;
        a2.next = c1;

        // List B: b1 -> b2 -> b3 -> c1
        ListNode b1 = new ListNode(5);
        ListNode b2 = new ListNode(6);
        ListNode b3 = new ListNode(1);
        b1.next = b2;
        b2.next = b3;
        b3.next = c1;

        // Now call the solution
        Solution solution = new Solution();
        ListNode intersectionNode = solution.getIntersectionNode(a1, b1);
        System.out.println(intersectionNode.val);       // 8

        //       a1 -> a2 \
        //                 -> c1 -> c2 -> c3
        // b1 -> b2 -> b3 /
    }
}