class Solution:
    
    # Very brute force method, get all permutations, and use a function to remove those with consecutives
    def getHappyString(self, n: int, k: int) -> str:
        
        l = self.generateallpossiblestringswithconsecutives(n)
        
        list = []
        for i in l:
            if self.haveconsecutiveelements(i) == True:
                pass
            else:
                list.append(''.join(i))    

        final_list = []      
        for i in list:
            final_list.append(self.convertnumbertocharacter(i))

        final_list.sort()

        if k > len(final_list):
            return ""
        else:
            kth_element = final_list[k-1]

        return kth_element
    

    def convertnumbertocharacter(self, string):
        alphabet_dict = {
            '0' : 'a',
            '1' : 'b',
            '2' : 'c'  
        }
        
        converted_numbers = []
        for character in string:
            converted_numbers.append(alphabet_dict[character])

        return ''.join(converted_numbers)
        
    

    def generateallpossiblestringswithconsecutives(self, n):
        bits = ['0'] * n  # Start with all zeros
        l = []

        # Doing 3-digit binary
        for _ in range(3 ** n):
            # print(bits)
            bits_copy = bits.copy()
            l.append(bits_copy)

            # Manually increment the binary number
            for i in range(n - 1, -1, -1):  # Start from the rightmost bit
                if bits[i] == '0':
                    bits[i] = '1'
                elif bits[i] == '1':
                    bits[i] = '2'
                else:
                    bits[i] = '0'  # Reset bit to 0 and continue left
                    break  # Stop once we flip a bit from 1 to 2

        return l


    def haveconsecutiveelements(self, list):
        for i in range(len(list) - 1):
            if list[i] == list[i+1]:
                return True
            else:
                pass

        return False
    

solution = Solution()
print(solution.getHappyString(1,3))
print(solution.getHappyString(1,4))
print(solution.getHappyString(3,9))



# Expected outputs:
# - Example 1:
#   Input: n = 1, k = 3
#   Output: "c"
#   Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. 
#   The third string is "c".

# - Example 2:
#   Input: n = 1, k = 4
#   Output: ""
#   Explanation: There are only 3 happy strings of length 1.

# - Example 3:
#   Input: n = 3, k = 9
#   Output: "cab"
#   Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", 
#   "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 
#   9th string = "cab"