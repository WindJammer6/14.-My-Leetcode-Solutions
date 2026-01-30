class Solution:
    
    # Approach 1: Straightforward way, working with strings without using divide and conquer paradigm 
    # (dosen't work)

    # Why does this not work even though the output looks correct?
    # Your terminal prints the correct result, like 964176192. But the online judge or Leetcode says 
    # "Wrong Answer".

    # ✅ Why your terminal shows the correct value:
    # You passed this string to your function:
    #       "00000010100101000001111010011100"
    # This is not an integer. It’s a string that looks like binary.

    # In your function:
    #       def reverseBits(n: int) -> int:
    #           string_n = f"{n}"
    # This converts n (already a string) to "00000010100101000001111010011100" again, and continues 
    # working on it assuming it's a binary string.

    # Your manual logic to reverse and compute decimal works on the characters, so it produces the 
    # expected result for that specific input.

    # ❌ Why the online judge rejects it:
    # Because the Leetcode system doesn't send a binary-looking string.

    # It sends:
    #       n = 43261596
    # (as an integer — not a 32-bit binary string!)

    # Then expects the output of reversing its binary (32-bit) form.

    # So your function is doing:
    #       string_n = f"{n}"  # But n is 43261596, so string_n = "43261596"
    # Then reversing the decimal digits instead of binary bits → totally wrong logic!

    # 🧨 The root problem:
    # You’re expecting a binary string as input (like "000000101...")
    # But the actual input is a regular decimal integer (like 43261596)
    # So reversing "43261596" as if it were bits will always give wrong results, unless by coincidence.
  

    # def reverseBits(self, n: int) -> int:
    #     string_n = f"{n}"

    #     # Convert binary representation to decimal number
    #     # Algorithmic approach to do this taken from the provided GeekforGeeks page, 
    #     # I used approach 1.
    #     # Source: https://www.geeksforgeeks.org/binary-to-decimal/ (GeekforGeeks)
    #     decimal_number = 0
    #     for i in range(len(string_n)):
    #         if (string_n[i] == "1"):
    #             decimal_number += pow(2, i)

    #     return decimal_number


    # /////////////////////////////////////////////////////////////////////////
     

    # Approach 2: Straightforward way, working with binary without using divide and conquer paradigm 
    # (works)

    # Source: https://www.youtube.com/watch?v=9KcyUbljAv0 (Code in Motion) (Youtube video by Code 
    # in Motion titled '[Animated] LeetCode 190 Reverse Bits | Blind 75')

    # Some pre-requisite knowledge:
    # What does the '>>' and '<<' operators do?
    # Operator	| Name	       | What it does	                        | Example
    #     <<	| Left Shift   | Shifts bits to the left, fills with 0s | 5 (101) << 1 → 1010 (which is 10)
    #     >>	| Right Shift  | Shifts bits to the right, drops LSBs   | 5 (101) >> 1 → 10 (which is 2)


    def reverseBits(self, n: int) -> int:
        result = 0      # binary is 0

        # This for loop code takes the least significant bit from n, and adding it to the left of 
        # 'result', effectively reversing the bit order of a 32-bit integer.

        # For each bit in a 32 bit s unsigned integer
        for i in range(32):
            # Shifts 'result' left by 1 bit, making room for the next bit from n.
            result = result << 1
            
            # n & 1: means "get the last bit of n".
            #   - It's a bitwise AND between n and 00000000000000000000000000000001.
            #   - Examples:
            #     If n = 13 → 1101 → n & 1 = 1
            #     If n = 4 → 0100 → n & 1 = 0

            # This line adds that last bit to 'result', now that 'result' has made space with the left shift.
            result += (n & 1)


            # n = n >> 1
            #   - Shifts n to the right by 1, essentially removing the bit we just used.
            #   - Example:
            #     n = 1101 → after >> 1 → n = 0110
            n = n >> 1

        return result

    # Visualising the whole process of approach 2:
    # Iteration |	n (before) | result (before) | n & 1 | result (after)	| n (after)
    #      1	|   1101	   | 0000	         |   1	 |    0001	        | 0110
    #      2	|   0110	   | 0001	         |   0	 |    0010	        | 0011
    #      3	|   0011	   | 0010	         |   1	 |    0101	        | 0001
    #      4	|   0001	   | 0101	         |   1	 |    1011	        | 0000



solution = Solution()
print(solution.reverseBits("00000010100101000001111010011100"))     # 964176192 (00111001011110000010100101000000)
print(solution.reverseBits("11111111111111111111111111111101"))     # 3221225471 (10111111111111111111111111111111)