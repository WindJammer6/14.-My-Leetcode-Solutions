# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # Need three pointers: 
        # - One pointer that iterates through the Linked List in steps of 2
        # - One pointer that always points at the second last element
        # - One pointer that always points at the last element

        # If no elements in the Linked List
        if head is None:
            return

        # If one element in the Linked List
        if head.next is None:
            return

        # If two elements in the Linked List
        if head.next.next is None:
            return

        iterator2 = head
        while iterator2.next.next is not None:
            iterator2 = iterator2.next

        iterator3 = iterator2.next
        iterator1 = head

        while iterator1.next.next is not None:
            iterator3.next = iterator1.next
            iterator1.next = iterator3
            iterator2.next = None

            if iterator1.next is None:
                break
            else:
                iterator1 = iterator3.next

            if iterator1 == iterator2:
                break

            while iterator3.next.next is not None:
                iterator3 = iterator3.next

            temp = iterator3
            iterator3 = iterator2
            iterator2 = temp

# Linked List 1 ('1-->2-->3-->4-->')
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

# Linked List 2 ('1-->2-->3-->4-->5-->')
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)

solution = Solution()
solution.reorderList(head1)      # '1-->4-->2-->3-->'
iterator1 = head1
list1 = []
while iterator1 is not None:
    list1.append(iterator1.val)
    iterator1 = iterator1.next
print(list1)

solution.reorderList(head2)      # '1-->5-->2-->4-->3-->'
iterator2 = head2
list2 = []
while iterator2 is not None:
    list2.append(iterator2.val)
    iterator2 = iterator2.next
print(list2)