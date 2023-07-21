#I have made much reference from the Stack Data Structure created in my Data Structure and
#Algorithms Journey. Here is the code from the Stack Data Structure I implemented when learning 
#about Stack Data Structures. The only difference is the Leetcode dosen't allow importing of
#Libraries so I had to re-implement the Stack using Python's List instead of using the Python's 
#library 'collections''s special Data Structure, 'deque'
# from collections import deque

# class Stack:
#     def __init__(self):
#         self.container = deque()

#     def push(self,value):
#         self.container.append(value)

#     def pop(self):
#         return self.container.pop()
    
#     def peek(self):
#         return self.container[-1]
    
#     def is_empty(self):
#         return len(self.container) == 0
    
#     def size(self):
#         return len(self.container)
    
#     #So I can use the 'print()' function on my 'Stack' class to look at my 'Stack' object
#     def __repr__(self):
#         return '{}'.format(self.container)


class MinStack:

    def __init__(self):
        self.container = []

    def push(self, val: int) -> None:
        return self.container.insert(0, val)

    def pop(self) -> None:
        if self.container != []:
            return self.container.pop(0)

    def top(self) -> int:
        if self.container != []:
            return self.container[0]

    def getMin(self) -> int:
        if self.container != []:
            min_val = self.container[0]

            for val in self.container:
                if val < min_val:
                    min_val = val

            return min_val


# Your MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(-2)

print(obj.container)

obj.pop()

param_3 = obj.top()

param_4 = obj.getMin()