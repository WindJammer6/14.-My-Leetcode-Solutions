# With HEAVY reference to this solution: https://www.youtube.com/watch?v=qB0zZpBJlh8 (Neetcode) (YouTube video by Neetcode titled, 
# 'Decode String - Leetcode 394 - Python')


class Solution:
    def decodeString(self, s):
        stack = []
        digits = ["0","1","2","3","4","5","6","7","8","9"] 

        # Iterate using a stack through the encoded string to find the outer paired/valid parenthesis 
        # (the square brackets)
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            
            else:           # if s[i] == "]"
                # Find all the alphabets/contents in the square brackets
                substring = ""
                while stack[-1] != "[":
                    popped = stack.pop()
                    substring = popped + substring
                
                # Remove the "[" itself from the stack
                stack.pop()

                # Find the digits multiplier, k
                k = ""
                while stack and stack[-1] in digits:
                    popped = stack.pop()
                    k = popped + k

                # Find the result of the multiplier, k * substring, and reappend it in to the stack
                # print(k)
                # print(substring)
                stack.append(int(k) * substring)
                # print(stack)

        decoded_string = ""
        for i in stack:
            decoded_string += i

        return decoded_string



solution = Solution()
print(solution.decodeString("3[a]2[bc]"))           # "aaabcbc"
print(solution.decodeString("3[a2[c]]"))            # "accaccacc"
print(solution.decodeString("2[abc]3[cd]ef"))       # "abcabccdcdcdef"