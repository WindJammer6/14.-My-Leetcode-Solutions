# With HEAVY reference to this solution: https://www.youtube.com/watch?v=7ABFKPK2hD4 (Neetcode) (YouTube video by Neetcode titled, 
# 'LRU Cache - Twitch Interview Question - Leetcode 146')

class Node:
    def __init__(self, data, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.data = data

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}                      # hash table to map to nodes (values are the nodes)
        self.cache_lru = Node(0)             # most left of doubly linked list (dummy node)
        self.cache_mru = Node(0)             # most right of doubly linked list (dummy node)
        self.cache_lru.next = self.cache_mru
        self.cache_mru.prev = self.cache_lru

    # Helper function: remove node from anywhere in the doubly linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    # Helper function: insert node at end/most right of the doubly linked list
    def insert(self, node):
        self.cache_mru.prev.next = node
        node.prev = self.cache_mru.prev
        node.next = self.cache_mru
        self.cache_mru.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # After a get operation, update the node to become most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].data[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Consider the case where the key-value pair we want to add is 
        # already in the cache, then we remove it, so that we later add it
        # as the most recently used
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        
        # Add the new node at the most recently used
        node = Node((key, value))
        self.insert(node)
        self.cache[key] = node

        # If exceed capacity, need envict least recently used
        if len(self.cache) > self.capacity:
            lru = self.cache_lru.next
            self.remove(lru)
            del self.cache[lru.data[0]]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
print(obj.put(1,1))
print(obj.put(2,2))
param_1 = obj.get(1)
print(param_1)
print(obj.put(3,3))
param_2 = obj.get(2)
print(param_2)
print(obj.put(4,4))
param_3 = obj.get(1)
print(param_3)
param_4 = obj.get(3)
print(param_4)
param_5 = obj.get(4)
print(param_5)

# Input:
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# [null,null,null,1,null,-1,null,-1,3,4]