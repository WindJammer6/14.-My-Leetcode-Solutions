# Pseudocode:
# 1. Find the substring before the asterisk and substring after the asterisk from pattern string p
# 2. Find the first instance of the 'substring before the asterisk', then for the remainder of the 
#    string s, see if the substring after the asterisk exists. If yes, return true, else return false


# What does Python's '.find()' do? (By ChatGPT)
# The Python find() method locates the starting index of the first occurrence of a substring 
# within a string. If the substring is found, it returns the numeric index position (starting at 
# 0); if the substring is not found, it returns -1


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        before_asterisk, after_asterisk = p.split("*")
        # print(before_asterisk)
        # print(after_asterisk)

        if before_asterisk not in s:
            return False

        if after_asterisk not in s[s.find(before_asterisk) + len(before_asterisk):]:
            return False

        if before_asterisk == "":
            if s.find(after_asterisk) != -1:
                return True

        if after_asterisk == "":
            if s.find(before_asterisk) != -1:
                return True
        
        # print(s.find(before_asterisk))
        # print(s[s.find(before_asterisk) + len(before_asterisk):].find(after_asterisk) + s.find(before_asterisk) + len(before_asterisk))
        # print(s[s.find(before_asterisk) + len(before_asterisk):])
        if s.find(before_asterisk) + len(before_asterisk)-1 < s[s.find(before_asterisk) + len(before_asterisk):].find(after_asterisk) + s.find(before_asterisk) + len(before_asterisk):
            return True
        else:
            return False



solution = Solution()
print(solution.hasMatch("leetcode", "ee*e"))    # true
print(solution.hasMatch("car", "c*v"))          # false
print(solution.hasMatch("luck", "u*"))          # true
print(solution.hasMatch("kvb", "k*v"))          # true