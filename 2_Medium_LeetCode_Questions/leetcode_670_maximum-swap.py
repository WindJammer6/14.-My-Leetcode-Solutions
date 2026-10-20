# With HEAVY reference to this solution: https://www.youtube.com/watch?v=4FZtJ8420m8 (NeetcodeIO) (YouTube 
# video by NeetcodeIO titled, 'Maximum Swaps - Leetcode 670 - Python')
    

# He suggested 2 methods, a two-pass method and a one-pass method. The one-pass method is 
# slightly more optimal but a little more complicated and I kinda don't get it so I will stick to
# to the two-pass method as it is more intuitive to me

# Pseudocode:
# 1. Store num as a list and initiate an array, which will store what is the maximum value (and its 
#    index) we have seen so far before the current value
# 2. From right to left (left pass), for the current index, find out what is the maximum value we have 
#    seen so far before the current value, and store it in the array, which will correspond to the
#    same index as the index of the current value in the num list
#    i.e. 
#                                                 integer n | 2  7  3       6
#    maximum value we have seen so far before current value | 7  6  6 NIL(dummy 0 value)   
# 3. Then from left to right (right pass), for each current value, look up the maximum value before the
#    current value. If the current value is smaller than the maximum value before the
#    current value, this will be the swap to get the maximum valued number in 1 swap

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_values_reversed = [0]            # dummy value for the last value of num list
        max_values_index_reversed = [1000000000]
        # print(num)

        max = 0
        max_index = 1000000000
        for i in range(len(num)-1, 0, -1):
            if int(num[i]) > max:
                max = int(num[i])
                max_index = i
            max_values_reversed.append(max)
            max_values_index_reversed.append(max_index)

        max_values = max_values_reversed[::-1]
        # print(max_values)
        max_values_index = max_values_index_reversed[::-1]
        # print(max_values_index)

        for i in range(len(num)):
            if int(num[i]) < max_values[i]:
                temp = num[i]
                # print(max_values_index[i])
                num[i] = str(num[max_values_index[i]])
                num[max_values_index[i]] = temp
                break

        num = "".join(num)
        return int(num)



solution = Solution()
print(solution.maximumSwap(2736))       # 7235
print(solution.maximumSwap(9973))       # 9973