# With HEAVY reference to this solution: https://www.youtube.com/watch?v=g9YQyYi4IQQ (Neetcode) (YouTube video by Neetcode titled, 
# 'Pow(x, n) - X to the power of N - Leetcode 50 - Python')


# Purpose of this leetcode question (by ChatGPT): 
# The problem can be easily solved by doing something like, x^n = x * x ... * x by n times. But the issue
# with this, and is what the question is testing, is that this is very inefficient as it has a 
# time complexity of O(n) (as you are multiplying x by itself n times) (see approach 1).

# Note this question isn't about the whole integer overflow thing...

# Is there a better solution for this, that has a better time complexity?
# According to Neetcode solution, yes there is, which is via a divide-and-conquer approach (via recursion)
# that can give us a time complexity of O(logn) (see approach 2).


# //////////////////////////////////////////////////////////////////////////////


# Approach 1: Brute Force (Time Limit Exceeded)
# Time complexity of O(n)
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         output = x
#         if n > 0:
#             for i in range(n-1):
#                 output *= x
#         elif n < 0:
#             denominator = x
#             for i in range(abs(n)-1):
#                 denominator *= x
#             output = 1 / denominator
#         else:
#             return 1

#         return output


# //////////////////////////////////////////////////////////////////////////////////


# Approach 2: Divide-and-Conquer
# Time complexity of O(logn)


# Pseudocode:
# 1. We can break down the problem into smaller problems. Lets say we use an example of 2^10, where
#    x = 2 and n = 10
#    - 2^10 can be broken down to 2^10 = 2^5 * 2^5
#    - Now here is the tricky part, when n becomes a odd number like 5, we can divide it to become
#      2^5 = 2^2 * 2^2 * 2 (with an additional constant 2) 
#    - 2^2 can be broken down to 2^2 = 2^1 * 2^1

# 2. Since this solution is Divide-and-Conquer, we can naturally do recursion, which means we need to
#    identify the base case and recurrence
#    - Base cases:
#      => When n = 0, x^n = 1
#      => When n = 1, x^n = x
#      => When x = 0, x^n = 0 (to handle edge cases where x = 0, and avoiding the need to do any recursion
#         at all, we can immediately return 0)
#    - Recurrence:
#      => If n is odd number, x^n = x^n//2 * x^n//2 * x
#      => If n is even number, x^n = x^n//2 * x^n//2

# 3. If n is a negative number, since for example 2^-2 is basically 2^-2 = 1 / 2^2, where 2^2 is what
#    we already calculating using the Divide-and-Conquer (denominator), we simply need to return 1 / result
# 4. Else if n is 0 or a positive number, we simply return result


class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.helper(x, abs(n))
        # print(result)

        if n < 0:       # If n is a negative number
            return 1 / result
        else:           # else if n is 0 or a postive number
            return result


    def helper(self, x, n):
        # Base cases
        if x == 0:
            return 0
        
        if n == 0:
            return 1

        if n == 1:
            return x


        # Recurrence
        result = self.myPow(x, n//2)
        if n % 2 == 1:
            return result * result * x
        else:
            return result * result



solution = Solution()
print(solution.myPow(2.00000, 10))           # 1024.00000
print(solution.myPow(2.10000, 3))            # 9.26100
print(solution.myPow(2.00000, -2))           # 0.25000
print(solution.myPow(2.00, -200000000))      # 0.00000
print(solution.myPow(0.44528, 0))            # 1