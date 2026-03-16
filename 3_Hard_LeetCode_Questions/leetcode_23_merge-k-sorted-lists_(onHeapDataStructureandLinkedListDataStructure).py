# My solution 1 (works, but got Time Limit Exceeded error):
# 1. Treat the lists of Linked List as a max heap where the Linked Lists are 
#    already sorted in ascending order.
# 2. Add the first element of the first Linked List into the new Linked List
# 3. Remove that first element from the first Linked List
# 4. Now the first Linked List might no longer already be in the correct
#    place. Execute heap sort with max-heapify operation to bring the Linked 
#    List where the first element is the maximum to the front the list/root of 
#    the max heap.
# 5. Repeat steps 2 and 3 until the list of Linked List/max heap is empty.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists):
#         # Remove any None in 'lists' the list of linked lists
#         lists = [node for node in lists if node is not None]

#         if len(lists) == 0:
#             return None

#         mergedLinkedList = ListNode()
#         iterator = mergedLinkedList

#         while len(lists) != 0:
#             self.heap_sort_with_max_heap(lists)

#             # print(lists)
#             # print(f"Lists length: {len(lists)}")
#             # Add first element of first linked list to the mergedLinkedList
#             iterator.next = lists[0]
#             iterator = iterator.next

#             # Remove that first element of first linked list
#             if lists[0].next is not None:
#                 lists[0] = lists[0].next
#             else:
#                 lists = lists[1:]       # If that linked list is done, then remove it from 'lists' the list of linked lists
            
#             # Heap Sort the remaining linked-lists since they are now out of order
#             self.heap_sort_with_max_heap(lists)
        
#         return mergedLinkedList.next

#     def heap_sort_with_max_heap(self, list):
#         heap_size = len(list)
#         # print(f"Heap size: {heap_size}")

#         # Build max heap
#         for index in range(heap_size // 2 - 1, -1, -1):
#             self.max_heapify(list, heap_size, index)

#         # One by one extract an element from max heap
#         for last_element_index in range(heap_size - 1, 0, -1):
#             # Move current root to end
#             list[0], list[last_element_index] = list[last_element_index], list[0]

#             # Reduce heap
#             heap_size -= 1

#             # Call max heapify on the reduced heap
#             self.max_heapify(list, heap_size, 0)

#     def max_heapify(self, list, heap_size, index):
#         left_child_index = 2 * index + 1
#         right_child_index = 2 * index + 2
#         largest_index = index
#         # print(left_child_index)
#         # print(right_child_index)
#         # print(largest_index)

#         # Checking if there is a left child node, and if its larger than the parent node
#         if (left_child_index < heap_size):
#             # print(list[left_child_index].val)
#             if list[left_child_index].val is not None:
#                 if (list[left_child_index].val > list[largest_index].val):
#                     largest_index = left_child_index

#         # Checking if there is a right child node, and if its larger than the parent node
#         if (right_child_index < heap_size):
#             if list[right_child_index].val is not None:
#                 if (list[right_child_index].val > list[largest_index].val):
#                     largest_index = right_child_index

#         # If either of the child nodes is larger than the parent node
#         if largest_index != index:
#             list[index], list[largest_index] = list[largest_index], list[index]
#             self.max_heapify(list, heap_size, largest_index)


# ////////////////////////////////////////////////////////


# My solution 2 (works), optimised from solution 1
# - This does not do heap sort for the entire 'lists' when adding a new node 
#   to the 'mergedLinkedList', as there is no need to. I just need to do 1 heapify
#   operation
# - I should do Min Heapify operation instead of Max Heapify operation to bring
#   the LinkedList with the minimum first element to the front the list/root
#   instead of the LinkedList with the maximum first element to the front the list/root

# 1. Treat the lists of Linked List as a min heap where the Linked Lists are 
#    already sorted in ascending order.
# 2. Add the first element of the first Linked List into the new Linked List
#    from the head of the Linked List
# 3. Remove that first element from the first Linked List
# 4. Now the first Linked List might no longer already be in the correct
#    place. Execute min-heapify operation to bring the Linked List where the
#    first element is the minimum to the front the list/root of the min heap.
# 5. Repeat steps 2 and 3 until the list of Linked List/min heap is empty.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Remove any None in 'lists' the list of linked lists
        lists = [node for node in lists if node is not None]

        if len(lists) == 0:
            return None

        mergedLinkedList = ListNode()
        iterator = mergedLinkedList
        self.build_min_heap(lists)

        while len(lists) != 0:
            self.min_heapify(lists, len(lists), 0)

            # print(lists)
            # print(f"Lists length: {len(lists)}")
            # Add first element of first linked list to the mergedLinkedList
            smallest_node = lists[0]

            # Remove that first element of first linked list
            if lists[0].next is not None:
                lists[0] = lists[0].next
            else:                           # If that linked list is done, then remove it from 'lists' the list of linked lists
                lists[0] = lists[-1]
                lists.pop()

            smallest_node.next = None
            iterator.next = smallest_node
            iterator = iterator.next
            
            # Heap Sort the remaining linked-lists since they are now out of order
            self.min_heapify(lists, len(lists), 0)
        
        return mergedLinkedList.next

    def build_min_heap(self, list):
        heap_size = len(list)

        # Build min heap
        for index in range(heap_size // 2 - 1, -1, -1):
            self.min_heapify(list, heap_size, index)

    def min_heapify(self, list, heap_size, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_index = index
        # print(left_child_index)
        # print(right_child_index)
        # print(smallest_index)

        # Checking if there is a left child node, and if its smaller than the parent node
        if (left_child_index < heap_size):
            # print(list[left_child_index].val)
            if list[left_child_index].val is not None:
                if (list[left_child_index].val < list[smallest_index].val):
                    smallest_index = left_child_index

        # Checking if there is a right child node, and if its smaller than the parent node
        if (right_child_index < heap_size):
            if list[right_child_index].val is not None:
                if (list[right_child_index].val < list[smallest_index].val):
                    smallest_index = right_child_index

        # If either of the child nodes is smaller than the parent node
        if smallest_index != index:
            list[index], list[smallest_index] = list[smallest_index], list[index]
            self.min_heapify(list, heap_size, smallest_index)


def build_linked_list(values):
    if len(values) == 0:
        return None

    head = ListNode(values[0])
    iterator = head

    for i in range(1, len(values)):
        iterator.next = ListNode(values[i])
        iterator = iterator.next

    return head

def linked_list_to_list(head):
    values = []
    iterator = head

    while iterator is not None:
        values.append(iterator.val)
        iterator = iterator.next

    return values


solution = Solution()

# Test case 1: [[1,4,5],[1,3,4],[2,6]]
head1_1 = build_linked_list([1, 4, 5])
head1_2 = build_linked_list([1, 3, 4])
head1_3 = build_linked_list([2, 6])

result1 = solution.mergeKLists([head1_1, head1_2, head1_3])
print(linked_list_to_list(result1))      # [1,1,2,3,4,4,5,6]

# Test case 2: []
result2 = solution.mergeKLists([])
print(linked_list_to_list(result2))      # []

# Test case 3: [[]]
head3_1 = build_linked_list([])

result3 = solution.mergeKLists([head3_1])
print(linked_list_to_list(result3))      # []

# Test case 4: [[1,4,5],[1,3,4],[2,6],[]]
head4_1 = build_linked_list([1, 4, 5])
head4_2 = build_linked_list([1, 3, 4])
head4_3 = build_linked_list([2, 6])
head4_4 = build_linked_list([])

result4 = solution.mergeKLists([head4_1, head4_2, head4_3, head4_4])
print(linked_list_to_list(result4))      # [1,1,2,3,4,4,5,6]

# Test case 5: [[],[]]
head5_1 = build_linked_list([])
head5_2 = build_linked_list([])

result5 = solution.mergeKLists([head5_1, head5_2])
print(linked_list_to_list(result5))      # []

# Test case 6: [[1],[0]]
head6_1 = build_linked_list([1])
head6_2 = build_linked_list([0])

result6 = solution.mergeKLists([head6_1, head6_2])
print(linked_list_to_list(result6))      # [0,1]

# Test case 7:
# [[-6,-3,-1,1,2,2,2],[-10,-8,-6,-2,4],[-2],[-8,-4,-3,-3,-2,-1,1,2,3],[-8,-6,-5,-4,-2,-2,2,4]]
head7_1 = build_linked_list([-6, -3, -1, 1, 2, 2, 2])
head7_2 = build_linked_list([-10, -8, -6, -2, 4])
head7_3 = build_linked_list([-2])
head7_4 = build_linked_list([-8, -4, -3, -3, -2, -1, 1, 2, 3])
head7_5 = build_linked_list([-8, -6, -5, -4, -2, -2, 2, 4])

result7 = solution.mergeKLists([head7_1, head7_2, head7_3, head7_4, head7_5])
print(linked_list_to_list(result7))      # [-10,-8,-8,-8,-6,-6,-6,-5,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-1,-1,1,1,2,2,2,2,2,3,4,4]