#Solving this Leetcode question using Two Pointers approach
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_list = []
        t_list = []

        for i in s:
            s_list.append(i)

        for i in t:
            t_list.append(i)

        print(s_list)
        print(t_list)

        #First pointer
        j = 0

        common_list = []

        #'Second pointer' (the pointer that is iterating through the elements in the 's_list' List)
        for i in s_list:

            while j < len(t_list):

                if t_list[j] == i:
                    common_list.append(j)
                    j += 1

                    if j == len(t_list) and len(s_list) == len(common_list):
                        return True
                    break

                else:
                    j += 1

            print(i)
            print(j)

        if s == "" and t == "":
            return True
        
        #2 scenarios, if while loop broken since 'if t_list[j] == i:' or 'while j < len(t_list):'
        if j >= len(t_list):
            return False
        
        return True
            
        
find_string = "leeeeetcode"
string = "leeeeetcode"

solution = Solution()

print(solution.isSubsequence(find_string, string))
