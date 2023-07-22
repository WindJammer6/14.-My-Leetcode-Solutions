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

    #This is how it looks like. Takes in 2 arguments (apart from the 'self' paramter), the index to add
    #the list of multiple elements, and a list of data itself
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
    def middleNode(self, linkedlist):

        if linkedlist.head is None:
            print("Linked List is empty!")
            return

        iterator = linkedlist.head

        linkedlist_data_list = [iterator.data]

        while iterator.next is not None:
            iterator = iterator.next
            linkedlist_data_list.append(iterator.data)

        print(linkedlist_data_list)
        print(len(linkedlist_data_list)/2)


        counter = 1
        iterator2 = linkedlist.head

        linkedlist_data_list2 = [iterator2.data]

        if len(linkedlist_data_list) % 2 == 0:
            while iterator2.next is not None and counter < len(linkedlist_data_list)/2:
                iterator2 = iterator2.next
                linkedlist_data_list2.append(iterator2.data)
                counter += 1

        elif len(linkedlist_data_list) == 1:
            return linkedlist

        else:
            counter += 1
            while iterator2.next is not None and counter < len(linkedlist_data_list)/2:
                iterator2 = iterator2.next
                linkedlist_data_list2.append(iterator2.data)
                counter += 1
        
        print(linkedlist_data_list2)
        print(counter)

        linkedlist.head = iterator2.next

        linkedlist.print_linked_list()

        return linkedlist


linkedlist = LinkedList()

#To create a Linked List that looks like this:
#'1-->2-->3-->4-->5-->6-->'
linkedlist.insert_node_at_beginning(6)
linkedlist.insert_node_at_beginning(5)
linkedlist.insert_node_at_beginning(4)
linkedlist.insert_node_at_beginning(3)
linkedlist.insert_node_at_beginning(2)
linkedlist.insert_node_at_beginning(1)

linkedlist.print_linked_list()

solution = Solution()

solution.middleNode(linkedlist).print_linked_list()