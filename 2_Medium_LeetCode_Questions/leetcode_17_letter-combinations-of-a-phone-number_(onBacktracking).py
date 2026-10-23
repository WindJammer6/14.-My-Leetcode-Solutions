# With HEAVY reference to this solution: https://www.youtube.com/watch?v=0snEunUacZY (Neetcode) (YouTube video by Neetcode titled, 
# 'Letter Combinations of a Phone Number - Backtracking - Leetcode 17')


# My initial thought:
# This question seems like finding exhaustive permutation or some sort, this should need backtracking 
# (a form of Depth First Search (DFS) algorithm over an implicitly decision tree)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        output = []

        dictionary = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        self.backtracking(0, "", digits, dictionary, output)

        return output


    def backtracking(self, index, current_string, digits, mapping, output):
        # Base case occurs when length of 'current_string' is equal to the length of 'digits'
        if len(current_string) == len(digits):
            output.append(current_string)
            return

        # Recursive case
        for character in mapping[digits[index]]:
            self.backtracking(index + 1, current_string + character, digits, mapping, output)


solution = Solution()
print(solution.letterCombinations("23"))        # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations("2"))         # ["a","b","c"]