# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        
        # Figure out the length of the Linked List
        length = 1

        iterator = head
        while iterator.next is not None:
            iterator = iterator.next
            length += 1

        if (length == 1) and (n == 1):
            return None

        if length - n - 1 == -1:
            return head.next

        # Send a pointer to the node before the node to be removed
        iterator2 = head
        for i in range(length - n - 1):
            iterator2 = iterator2.next

        # Remove the node
        iterator2.next = iterator2.next.next

        return head

# Linked List 1 ('1-->2-->3-->4-->5-->')
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

# Linked List 2 ('1-->')
head2 = ListNode(1)

# Linked List 3 ('1-->2-->')
head3 = ListNode(1)
head3.next = ListNode(2)

# Linked List 4 ('1-->2-->')
head4 = ListNode(1)
head4.next = ListNode(2)

solution = Solution()
head1 = solution.removeNthFromEnd(head1, 2)      # '1-->2-->3-->5-->'
iterator1 = head1
list1 = []
while iterator1 is not None:
    list1.append(iterator1.val)
    iterator1 = iterator1.next
print(list1)

head2 = solution.removeNthFromEnd(head2, 1)      # ''
iterator2 = head2
list2 = []
while iterator2 is not None:
    list2.append(iterator2.val)
    iterator2 = iterator2.next
print(list2)

head3 = solution.removeNthFromEnd(head3, 1)      # '1-->'
iterator3 = head3
list3 = []
while iterator3 is not None:
    list3.append(iterator3.val)
    iterator3 = iterator3.next
print(list3)

head4 = solution.removeNthFromEnd(head4, 2)      # '2-->'
iterator4 = head4
list4 = []
while iterator4 is not None:
    list4.append(iterator4.val)
    iterator4 = iterator4.next
print(list4)