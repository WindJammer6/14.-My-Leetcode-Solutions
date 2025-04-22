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
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return null;
        }

        while ((head != null) && (head.val == val)) {
            if (head.val == val) {
                head = head.next;
            }
        }

        ListNode iterator = head;

        while (iterator != null){
            // System.out.println(iterator.val);

            if (iterator.next != null){
                // System.out.println(iterator.val);
                if (iterator.next.val == val){
                    iterator.next = iterator.next.next;

                    if (iterator.next == null){
                        break;
                    }
                }
                else{
                    if (iterator.next == null){
                        break;
                    }

                    iterator = iterator.next;
                }

            } else{
                break;
            }
        }

        return head;
    }
}


class TestSolution {
    public static void main (String args[]){
        Solution solution = new Solution();

        // Test Case 1: [1,2,6,3,4,5,6], val = 6
        ListNode head1 = new ListNode(1);
        head1.next = new ListNode(2);
        head1.next.next = new ListNode(6);
        head1.next.next.next = new ListNode(3);
        head1.next.next.next.next = new ListNode(4);
        head1.next.next.next.next.next = new ListNode(5);
        head1.next.next.next.next.next.next = new ListNode(6);

        ListNode result1 = solution.removeElements(head1, 6);
        System.out.print("Test Case 1 Output: ");
        printList(result1); // Expected: 1 -> 2 -> 3 -> 4 -> 5

        // Test Case 2: [], val = 1
        ListNode head2 = null;

        ListNode result2 = solution.removeElements(head2, 1);
        System.out.print("Test Case 2 Output: ");
        printList(result2); // Expected: []

        // Test Case 3: [7,7,7,7], val = 7
        ListNode head3 = new ListNode(7);
        head3.next = new ListNode(7);
        head3.next.next = new ListNode(7);
        head3.next.next.next = new ListNode(7);

        ListNode result3 = solution.removeElements(head3, 7);
        System.out.print("Test Case 3 Output: ");
        printList(result3); // Expected: []
    }


    // Helper method to print the Linked List Data Structure
    public static void printList(ListNode head) {
        if (head == null) {
            System.out.println("[]");
            return;
        }

        while (head != null) {
            System.out.print(head.val);
            if (head.next != null) System.out.print(" -> ");
            head = head.next;
        }
        System.out.println();
    }
}