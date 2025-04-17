import java.util.ArrayList;

//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        ArrayList<Integer> arrayList = new ArrayList<>();

        ListNode iterator = head;
        while (iterator != null){
            arrayList.add(0, iterator.val);
            iterator = iterator.next;
        }

        // Create dummy head ListNode
        ListNode reversedLinkedList = new ListNode(-1);
        ListNode iterator2 = reversedLinkedList;
        for (Integer i : arrayList){
            iterator2.next = new ListNode(i);
            iterator2 = iterator2.next;
        }

        return reversedLinkedList.next;

    }
}


class TestSolution {
    public static void main (String args[]){
        // Build Linked List 1
        ListNode linkedListNode1 = new ListNode(1);
        ListNode linkedListNode2 = new ListNode(2);
        ListNode linkedListNode3 = new ListNode(3);
        ListNode linkedListNode4 = new ListNode(4);
        ListNode linkedListNode5 = new ListNode(5);

        linkedListNode1.next = linkedListNode2;
        linkedListNode2.next = linkedListNode3;
        linkedListNode3.next = linkedListNode4;
        linkedListNode4.next = linkedListNode5;

        Solution solution = new Solution();
        System.out.println(solution.reverseList(linkedListNode1));     // [5,4,3,2,1]


        // Build Linked List 2
        ListNode linkedListNode6 = new ListNode(1);
        ListNode linkedListNode7 = new ListNode(2);

        linkedListNode6.next = linkedListNode7;
        System.out.println(solution.reverseList(linkedListNode6));     // [2,1]


        // Build Linked List 3
        ListNode linkedListNode8 = null;
        System.out.println(solution.reverseList(linkedListNode8));     // []
    }
}