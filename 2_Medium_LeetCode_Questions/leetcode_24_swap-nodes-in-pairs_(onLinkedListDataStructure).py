#Had much help from ChatGPT to solve bugs in my code for this Medium Difficulty Leetcode question

#'Node' and 'LinkedList' class taken from elsewhere to simulate the Linked List Data Structure 
#to test the Leetcode's problem code on
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_beginning(self, new_data):
        node = Node(new_data, self.head)
        self.head = node

    def insert_at_end(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        
        else:
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next
            
        iterator.next = Node(new_data, None)

    def get_length_of_linked_list(self):
        count = 0
        iterating_nodes = self.head
        while iterating_nodes:
            count += 1
            iterating_nodes = iterating_nodes.next
        return count

    def print_linked_list(self):
        if self.head == None:
            print("Linked List is empty!")
            return
        else:
            iterating_nodes = self.head
            linked_list_string = ""

            while iterating_nodes:
                linked_list_string += str(iterating_nodes.data) + '-->'
                iterating_nodes = iterating_nodes.next

        print(linked_list_string)

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length_of_linked_list():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.head = self.head.next
            return
        
        else:
            count = 0
            iterator = self.head
            while iterator is not None:
                if count == index - 1:
                    iterator.next = iterator.next.next
                    break
                iterator = iterator.next
                count += 1
                
    def insert_at_index(self, index, new_data):
        if index < 0 or index >= self.get_length_of_linked_list():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_node_at_beginning(new_data)
        
        else:
            count = 0
            iterator = self.head
            while iterator.next is not None:
                if count == index - 1:
                    iterator.next = Node(new_data, iterator.next)
                    break
                iterator = iterator.next
                count += 1

    def insert_multiple_values_at_index(self, index, data_list):
        if index < 0 or index >= self.get_length_of_linked_list():
            raise Exception("Invalid Index")
        
        if index == 0:
            #This is how to traverse a list in reverse order so that the elements in 'data_list'
            #will be appended in the desired order 
            for data in reversed(data_list):
                self.insert_node_at_beginning(data)

        else:
            count = 0
            iterator = self.head
            while iterator.next is not None:
                if count == index - 1:
                    for data in reversed(data_list):
                        iterator.next = Node(data, iterator.next)
                    break
                iterator = iterator.next
                count += 1

def merge_linked_list_at_end(linkedlist1, linkedlist2):
    dummylinkedlist = LinkedList()

    dummylinkedlist.head = linkedlist1.head

    iterator = dummylinkedlist.head
    while iterator.next is not None:
        iterator = iterator.next

    iterator.next = linkedlist2.head
    
    return dummylinkedlist

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, linkedlist):
        #To check for the cases if the linked list is empty or only contains only one node, no swaps needed
        if linkedlist.head is None or linkedlist.head.next is None:
            return linkedlist

        #Dealing with swapping the head node and its next node
        headnode = linkedlist.head
        headnextnode = linkedlist.head.next

        #Swapping proccess between the head node and its next node
        headnode.next = headnode.next.next
        headnextnode.next = headnode

        linkedlist.head = headnextnode

        linkedlist.print_linked_list()


        #Thought process for the Automating the process part of swapping the pairs down the Linked List
        # #Ver 1.
        # # Dealing with swapping the third and fourth nodes
        # thirdnode = headnode.next
        # fourthnode = headnextnode.next.next.next

        # #Swapping proccess between the third and fourth nodes
        # thirdnode.next = thirdnode.next.next
        # fourthnode.next = thirdnode

        # headnode.next = fourthnode

        # linkedlist.print_linked_list()

        # #Dealing with swapping the fifth and sixth nodes
        # fifthnode = thirdnode.next
        # sixthnode = fourthnode.next.next.next

        # #Swapping proccess between the fifth and sixth nodes
        # fifthnode.next = fifthnode.next.next
        # sixthnode.next = fifthnode

        # thirdnode.next = sixthnode

        # linkedlist.print_linked_list()


        # #Ver 2.
        # # Dealing with swapping the third and fourth nodes
        # thirdnode = linkedlist.head.next.next
        # fourthnode = linkedlist.head.next.next.next

        # #Swapping proccess between the third and fourth nodes
        # thirdnode.next = thirdnode.next.next
        # fourthnode.next = thirdnode

        # linkedlist.head.next.next = fourthnode

        # linkedlist.print_linked_list()


        # #Dealing with swapping the fifth and sixth nodes
        # fifthnode = linkedlist.head.next.next.next.next
        # sixthnode = linkedlist.head.next.next.next.next.next

        # #Swapping proccess between the fifth and sixth nodes
        # fifthnode.next = fifthnode.next.next
        # sixthnode.next = fifthnode

        # linkedlist.head.next.next.next.next = sixthnode

        # linkedlist.print_linked_list()
        


        #Automating the process
        #'iterator2' and 'iterator3' represents 2 individual nodes, which will be the node pair that will be swapped as we traverse down the
        #Linked List

        #To deal with the case if the Linked List only has 2 nodes and 'headnextnode.next.next' and
        #'headnextnode.next.next.next' dosen't exist
        if headnextnode.next.next is not None and headnextnode.next.next.next is not None:  
            iterator2 = headnextnode.next.next
            iterator3 = headnextnode.next.next.next
        else:
            return linkedlist

        iteratorhead = headnode

        #To check if we have reached the end of the Linked List, or if there is only one more node remaining without any pair to swap with

        #For some unknown reason these code cant work, but I have a feeling that it is due to the many assignment of variables in the
        #while loop which may cause wrong allocation of memory leading to unintended outputs:
        # while iterator2 is not None and iterator3 is not None:
        #     iterator2.next = iterator2.next.next
        #     iterator3.next = iterator2

        #     iteratorhead.next = iterator3

              #Error might have been here, but difficult to pin point where exactly is when there is false allocation of the nodes in memory
              #due to the assignement of so many variables between 'iteratorhead', 'iterator2' and 'iterator3'
        #     iteratorhead = headnode.next.next
        #     iterator2 = iterator2.next.next
        #     iterator3 = iterator3.next.next

        #With some help with ChatGPT's reference answers, it helped to untangle the many assigning of variables to prevent any false
        #allocation of memory of the nodes in the Linked Lists that works to provide the desired ouput:
        while iterator2 is not None and iterator3 is not None:
            iterator2.next = iterator3.next
            iterator3.next = iterator2
            iteratorhead.next = iterator3

            # Move to the next pair
            iteratorhead = iterator2

            if iteratorhead.next is not None and iterator2.next is not None:
                iterator2 = iteratorhead.next
                iterator3 = iterator2.next
            else:
                iterator2 = None
                iterator3 = None

            linkedlist.print_linked_list()

        linkedlist.print_linked_list()

        return linkedlist
    

        #Correct answers provided by ChatGPT that works as well
        # Correct ans 1:
        # if not linkedlist.head or not linkedlist.head.next:
        #     # The linked list is empty or contains only one node, no swaps needed
        #     return linkedlist

        # # Dealing with swapping the head node and its next node
        # headnode = linkedlist.head
        # headnextnode = linkedlist.head.next
        # headnode.next = headnextnode.next
        # headnextnode.next = headnode
        # linkedlist.head = headnextnode

        # # Automate the process
        # iterator2 = headnextnode.next.next
        # iterator3 = headnextnode.next.next.next
        # iteratorhead = headnode

        # while iteratorhead and iterator2 and iterator3:
        #     # Swap nodes
        #     iterator2.next = iterator3.next
        #     iterator3.next = iterator2
        #     iteratorhead.next = iterator3

        #     # Move to the next pair
        #     iteratorhead = iterator2
        #     iterator2 = iteratorhead.next if iteratorhead.next else None
        #     iterator3 = iterator2.next if iterator2 else None

        # linkedlist.print_linked_list()

        # return linkedlist


        #Correct ans 2:
        # if not linkedlist.head or not linkedlist.head.next:
        #     # The linked list is empty or contains only one node, no swaps needed
        #     return linkedlist

        # # Dealing with swapping the head node and its next node
        # headnode = linkedlist.head
        # headnextnode = linkedlist.head.next
        # headnode.next = headnextnode.next
        # headnextnode.next = headnode
        # linkedlist.head = headnextnode

        # current = headnode
        # while current.next and current.next.next:
        #     first_node = current.next
        #     second_node = current.next.next

        #     first_node.next = second_node.next
        #     current.next = second_node
        #     second_node.next = first_node

        #     current = first_node

        # linkedlist.print_linked_list()

        # return linkedlist


samplelinkedlist = LinkedList()

#To create a Linked List that looks like this:
#'1-->2-->3-->4-->5-->6-->7-->8-->9-->10-->11-->12-->'
samplelinkedlist.insert_node_at_beginning(12)
samplelinkedlist.insert_node_at_beginning(11)
samplelinkedlist.insert_node_at_beginning(10)
samplelinkedlist.insert_node_at_beginning(9)
samplelinkedlist.insert_node_at_beginning(8)
samplelinkedlist.insert_node_at_beginning(7)
samplelinkedlist.insert_node_at_beginning(6)
samplelinkedlist.insert_node_at_beginning(5)
samplelinkedlist.insert_node_at_beginning(4)
samplelinkedlist.insert_node_at_beginning(3)
samplelinkedlist.insert_node_at_beginning(2)
samplelinkedlist.insert_node_at_beginning(1)

samplelinkedlist.print_linked_list()

solution = Solution()

solution.swapPairs(samplelinkedlist).print_linked_list()