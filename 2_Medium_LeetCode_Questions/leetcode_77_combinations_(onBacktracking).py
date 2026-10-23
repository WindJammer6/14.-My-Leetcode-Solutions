# Using backtracking, with inspiration to the '17. Letter Combinations of a Phone Number' leetcode 
# question (their codes are very similar as both uses backtracking)

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        output = []

        self.backtracking(1, [], output, n, k)

        return output


    def backtracking(self, index, current_combination, output, n, k):
        # Base case occurs when length of 'current_combination' is equal to k
        if len(current_combination) == k:
            output.append(current_combination)
            return

        # Recursive case
        for i in range(index, n+1):
            self.backtracking(i + 1, current_combination + [i], output, n, k)


solution = Solution()
print(solution.combine(4, 2))        # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(solution.combine(1, 1))        # [[1]]