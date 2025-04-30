// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Add a dummy head Linked List node
        ListNode resultLinkedList = new ListNode(-1);

        ListNode iterator1 = l1;
        ListNode iterator2 = l2;
        ListNode iterator3 = resultLinkedList;
        int sum;

        boolean carryForwardOne = false;

        while ((iterator1 != null) && (iterator2 != null)){
            if (carryForwardOne == true){
                sum = iterator1.val + iterator2.val + 1;
            } else {
                sum = iterator1.val + iterator2.val;
            }

            if (sum >= 10){
                carryForwardOne = true;
                iterator3.next = new ListNode(sum - 10);
            } else {
                carryForwardOne = false;
                iterator3.next = new ListNode(sum);
            }

            System.out.println(iterator2.val);
            iterator1 = iterator1.next;
            iterator2 = iterator2.next;
            iterator3 = iterator3.next;
        }


        // If iterator1 Linked List is longer than iterator2 Linked List
        while (iterator1 != null){

            if (carryForwardOne == true){
                sum = iterator1.val + 0 + 1;
            } else {
                sum = iterator1.val + 0;
            }

            if (sum >= 10){
                carryForwardOne = true;
                iterator3.next = new ListNode(sum - 10);
            } else {
                carryForwardOne = false;
                iterator3.next = new ListNode(sum);
            }

            iterator1 = iterator1.next;
            iterator3 = iterator3.next;
        }

        // If iterator2 Linked List is longer than iterator1 Linked List
        while (iterator2 != null){

            if (carryForwardOne == true){
                sum = iterator2.val + 0 + 1;
            } else {
                sum = iterator2.val + 0;
            }

            if (sum >= 10){
                carryForwardOne = true;
                iterator3.next = new ListNode(sum - 10);
            } else {
                carryForwardOne = false;
                iterator3.next = new ListNode(sum);
            }

            iterator2 = iterator2.next;
            iterator3 = iterator3.next;
        }


        // Check if need add one last new Linked List node to the result Linked List
        if (carryForwardOne == true){
            iterator3.next = new ListNode(1);
        }


        // Returning 'resultLinkedList.next' instead of 'resultLinkedList' so that the returned
        // result Linked List will not have the dummy Linked List node
        return resultLinkedList.next;
    }

}


class TestSolution {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1: l1 = [2,4,3], l2 = [5,6,4]
        ListNode l1a = new ListNode(2);
        l1a.next = new ListNode(4);
        l1a.next.next = new ListNode(3);

        ListNode l2a = new ListNode(5);
        l2a.next = new ListNode(6);
        l2a.next.next = new ListNode(4);

        ListNode resultA = solution.addTwoNumbers(l1a, l2a);
        printLinkedList(resultA); // Expected: 7 -> 0 -> 8

        // Example 2: l1 = [0], l2 = [0]
        ListNode l1b = new ListNode(0);
        ListNode l2b = new ListNode(0);

        ListNode resultB = solution.addTwoNumbers(l1b, l2b);
        printLinkedList(resultB); // Expected: 0

        // Example 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9]
        ListNode l1c = new ListNode(9);
        l1c.next = new ListNode(9);
        l1c.next.next = new ListNode(9);
        l1c.next.next.next = new ListNode(9);
        l1c.next.next.next.next = new ListNode(9);
        l1c.next.next.next.next.next = new ListNode(9);
        l1c.next.next.next.next.next.next = new ListNode(9);

        ListNode l2c = new ListNode(9);
        l2c.next = new ListNode(9);
        l2c.next.next = new ListNode(9);
        l2c.next.next.next = new ListNode(9);

        ListNode resultC = solution.addTwoNumbers(l1c, l2c);
        printLinkedList(resultC); // Expected: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
    }

    // Helper function to print a Linked List visually
    public static void printLinkedList(ListNode head) {
        while (head != null) {
            System.out.print(head.val);
            if (head.next != null) System.out.print(" -> ");
            head = head.next;
        }
        System.out.println();
    }
}
