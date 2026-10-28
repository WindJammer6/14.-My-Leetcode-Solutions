# With some reference to this solution: https://www.youtube.com/watch?v=FOyRpNUSFeA (NeetcodeIO) (YouTube 
# video by NeetcodeIO titled, 'Combination Sum II - Leetcode 40 - Python') (particularly on the trick to 
# deal with duplicate combinations via excluding the current candidate and all its duplicates)


# Using backtracking, with inspiration to the '17. Letter Combinations of a Phone Number' leetcode 
# question (their codes are very similar as both uses backtracking)


# Pseudocode:
# 1. The solution is quite similar to the '39. Combination Sum' leetcode question, by which
#    you do the decision tree branching to 2 decisions:
#    - Include current candidate
#    - Exclude current candidate
# 2. But the extra problem in this question is on how to deal with duplicates combinations in 'candidates'.
#    As if you follow the solution of the '39. Combination Sum' leetcode question, you will encounter
#    duplicate combinations in this problem.
# 3. To tackle this, you need to first sort 'candidates', the rationale for this is so that all 
#    duplicates are adjacent to one another in 'candidates'
# 4. We then do the same decision tree branching similar to the '39. Combination Sum' leetcode question,
#    but with the additional condition where the decision tree branching to 2 decisions is as follows:
#    - Include current candidate (here you can later make a decision branch to its duplicate candidates of 
#      the same value)
#    - Exclude current candidate and all its duplicates (such that in this decision branch the current 
#      candidate or any other duplicate candidate of the same value will not be used here, as doing so
#      will eliminate any duplicate combinations)


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        output = []

        self.backtracking(0, [], candidates, target, output)

        return output

    def backtracking(self, index, current_combination, candidates, target, output):
        # Base case occurs when sum of 'current_combination' is equal to target
        if sum(current_combination) == target:
            output.append(current_combination)
            return

        # There are no more candidates to choose from or the sum of the elements in the 
        # 'current_combination' aka 'total' exceeds the target 
        if sum(current_combination) > target or index >= len(candidates):
            return

        # Recursive case 
        if index < len(candidates):
            # There are 2 decisions to make:
            # - First decision is to use the current candidate (here you can later make a decision branch 
            #   to its duplicate candidates of the same value)
            self.backtracking(index + 1, current_combination + [candidates[index]], candidates, target, output)

            # - Second decision is to never use the current candidate and all its duplicates (such that in 
            #   this decision branch the current candidate or any other duplicate candidate of the same 
            #   value will not be used here, as doing so will eliminate any duplicate combinations)
            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index]:
                # print(index)
                index += 1
            self.backtracking(index + 1, current_combination, candidates, target, output)



solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))         # [[1,1,6], [1,2,5], [1,7], [2,6]]
print(solution.combinationSum2([2,5,2,1,2], 5))              # [[1,2,2], [5]]