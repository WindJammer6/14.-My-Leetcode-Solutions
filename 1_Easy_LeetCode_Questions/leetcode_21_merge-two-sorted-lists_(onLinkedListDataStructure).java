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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode iterator1 = list1;
        ListNode iterator2 = list2;

        // Create dummy head ListNode
        ListNode mergedLinkedList = new ListNode(-1);
        ListNode iterator3 = mergedLinkedList;

        if ((iterator1 != null) && (iterator2 != null)) {
            if (iterator1.val < iterator2.val) {
                iterator3.next = iterator1;
                iterator3 = iterator3.next;
                iterator1 = iterator1.next;
            } else{
                iterator3.next = iterator2;
                iterator3 = iterator3.next;
                iterator2 = iterator2.next;
            }
        }

        System.out.println(iterator1.val);
        System.out.println(iterator2.val);

        while ((iterator1 != null) || (iterator2 != null)){
            if ((iterator1 == null) || (iterator2 == null)) {
                break;
            }

            if ((iterator1.val < iterator2.val)) {
                iterator3.next = iterator1;
                iterator3 = iterator3.next;
                iterator1 = iterator1.next;
            } else {
                iterator3.next = iterator2;
                iterator3 = iterator3.next;
                iterator2 = iterator2.next;
            }

        }


        if (iterator1 == null) {
            while (iterator2 != null) {
                iterator3.next = iterator2;
                iterator3 = iterator3.next;
                iterator2 = iterator2.next;
            }
        }

        if (iterator2 == null) {
            while (iterator1 != null) {
                iterator3.next = iterator1;
                iterator3 = iterator3.next;
                iterator1 = iterator1.next;
            }
        }

        // Remove dummy head ListNode
        ListNode withoutDummyHeadMergedLinkedList = mergedLinkedList.next;

        // Print out the mergedLinkedLIst
        ArrayList<Integer> arrayList = new ArrayList<>();
        ListNode iterator4 = withoutDummyHeadMergedLinkedList;
        while (iterator4 != null) {
            if (iterator4 == null) {
                break;
            }

            arrayList.add(iterator4.val);
            iterator4 = iterator4.next;
        }

        System.out.println(arrayList.toString());

        return withoutDummyHeadMergedLinkedList;
    }
}


class TestSolution {
    public static void main (String args[]){
        ListNode LinkedList1 = new ListNode(1);

        ListNode LinkedListNode1 = new ListNode(2);
        LinkedList1.next = LinkedListNode1;
        ListNode LinkedListNode2 = new ListNode(4);
        LinkedListNode1.next = LinkedListNode2;

        ListNode LinkedList2 = new ListNode(1);

        ListNode LinkedListNode3 = new ListNode(3);
        LinkedList2.next = LinkedListNode3;

        ListNode LinkedListNode4 = new ListNode(4);
        LinkedListNode3.next = LinkedListNode4;

        Solution solution = new Solution();
        System.out.println(solution.mergeTwoLists(LinkedList1, LinkedList2));    // [1,1,2,3,4,4]
    }
}