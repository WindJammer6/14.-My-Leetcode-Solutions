class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        first_pointer = 0
        second_pointer = 0
        counter = 0
        first_occurence_index = -1

        for i in range(len(haystack)):
            first_pointer = i


            if (haystack[first_pointer] == needle[0]):
                first_occurence_index = first_pointer
                second_pointer = 0
                
                counter = 0
                while (first_pointer < len(haystack)) and (second_pointer < len(needle)):
                    if (haystack[first_pointer] == needle[second_pointer]):
                        counter += 1
                        first_pointer += 1
                        second_pointer += 1
                    else:
                        break                       

                    print(f"Counter: {counter}")
                    print(f"First Pointer: {first_pointer}")
                    print(f"Second Pointer: {second_pointer}")
                    if counter == len(needle):
                        return first_occurence_index


        return -1
        

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))      # 0
print(solution.strStr("leetcode", "leeto"))     # -1
print(solution.strStr("mississipi", "issip"))   # 4 