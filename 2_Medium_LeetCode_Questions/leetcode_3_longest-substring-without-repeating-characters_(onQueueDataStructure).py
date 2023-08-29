#Attempt 2 (after looking at some hints from the 'discussion' section where people mentioned they used
#Queue Data Structures to solve this question)
#Via Queue Data Structure:
class Queue:
    def __init__(self):
        self.buffer = []

    def enqueue(self,value):
        self.buffer.insert(0, value)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

    def __repr__(self):
        return '{}'.format(self.buffer)
    

def get_length_of_subarray(list):
    return len(list)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = Queue()

        string_list = []

        for i in s:
            string_list.append(i)


        longest_subarray = 0

        for i in string_list:

            queue.enqueue(i)

            #To tell the program if the queue only has one element or less, then there is no need to 
            #check if there is any duplicates of the element you just enqueued into the queue
            if len(queue.buffer) > 1:
                #Checking if the element you just enqueued already exists in the queue
                if i in queue.buffer[1:]:
                    #Dequeing all the elements up until the previous duplicate of the element you just
                    #enqueued into the queue
                    while i != queue.buffer[-1]:
                        queue.dequeue()
                    #Dequeuing the previous duplicate as well
                    queue.dequeue()

            #Checking every single time after an element is enqueued into the queue, the length of that 
            #subarray, and updating the 'longest_subarray' variable if this subarray is the longest so far
            if get_length_of_subarray(queue.buffer) > longest_subarray:
                longest_subarray = get_length_of_subarray(queue.buffer)

        return longest_subarray
            

string = "dvdf"

solution = Solution()

print(solution.lengthOfLongestSubstring(string))


#///////////////////////////////////////////////////////////////


#Attempt 1 (but realised there was a flaw in this logic after looking at multiple testcases)
#Via sliding window technique:
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        # #To deal with the edgecase where an empty string is passed into this function
        # if len(s) < 1:
        #     return 0
        
        # if len(s) == 1:
        #     return 1

        # left_window_pointer = 0
        # right_window_pointer = 1
        
        # #To remember the elements seen so far in the string in a hashtable
        # seen_dict = {0 : s[0]}

        # string_list = []

        # for i in s:
        #     string_list.append(i)


        # #//////////////////////Main algorithm starts here/////////////////////////
        # longest_subarray = 0

        # while right_window_pointer < len(string_list):
            
        #     if string_list[right_window_pointer] not in list(seen_dict.values()):
        #         #Updating elements seen into the hashtable:
        #         seen_dict.update({right_window_pointer : string_list[right_window_pointer]})
        #         print(string_list[right_window_pointer])
        #         print(list(seen_dict.values()))

        #     #if string_list[right_window_pointer] == string_list[right_window_pointer-1]
        #     else:
        #         if longest_subarray < right_window_pointer - left_window_pointer:
        #             longest_subarray = right_window_pointer - left_window_pointer
        #         left_window_pointer = right_window_pointer
        #         seen_dict = {right_window_pointer : string_list[right_window_pointer]}
                        
        #     right_window_pointer += 1

        
        # #For edge cases if the longest substring coincidentally reaches the end of the list
        # if longest_subarray < right_window_pointer - left_window_pointer:
        #     longest_subarray = right_window_pointer - left_window_pointer

        
        # return longest_subarray