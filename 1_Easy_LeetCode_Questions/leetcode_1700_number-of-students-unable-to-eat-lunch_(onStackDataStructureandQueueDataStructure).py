#'Stack' and 'Queue' class taken from elsewhere to create the Stack and Queue Data Structures
#to solve the Leetcode's problem code on. Had to modify them, reimplementing them using Python's
#Lists since the 'Stack' and 'Queue' classes initially used the Python library's 'collections'
#special Data Structure 'deque', but Leetcode dosen't allow importing of libraries

#The Stack Data Structure
class Stack:
    def __init__(self):
        self.container = []

    def push(self, val):
        return self.container.insert(0, val)

    def pop(self):
        if self.container != []:
            return self.container.pop(0)

    def top(self):
        if self.container != []:
            return self.container[0]
        
    def size(self):
        return len(self.container)
    
    def __repr__(self):
        return '{}'.format(self.container)
        

#The Queue Data Structure
class Queue:
    def __init__(self):
        self.buffer = []

    def enqueue(self,value):
        self.buffer.insert(0, value)

    def dequeue(self):
        return self.buffer.pop()
    
    def front_element(self):
        return self.buffer[-1]
    
    def last_element(self):
        return self.buffer[0]
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def __repr__(self):
        return '{}'.format(self.buffer)


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_queue = Queue()
        sandwiches_stack = Stack()

        for i in students:
            students_queue.enqueue(i)

        for i in reversed(sandwiches):
            sandwiches_stack.push(i)

        print(students_queue)
        print(sandwiches_stack)

        counter = 0

        while True:

            if counter == len(students_queue.buffer):
                break

            if sandwiches_stack.top() == students_queue.front_element():
                sandwiches_stack.pop()
                students_queue.dequeue()
                counter = 0

            else:
                dequeued_front_student = students_queue.dequeue()
                students_queue.enqueue(dequeued_front_student)
                counter += 1

            print(students_queue)
            print(sandwiches_stack)
            print(counter)

        return len(students_queue.buffer)


student_list = [1,1,1,0,0,1]
sandwiches_list = [1,0,0,0,1,1]

solution = Solution()

print(solution.countStudents(student_list, sandwiches_list))