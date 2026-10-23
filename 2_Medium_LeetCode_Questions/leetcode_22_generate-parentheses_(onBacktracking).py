# Using backtracking, with inspiration to the '17. Letter Combinations of a Phone Number' leetcode 
# question (their codes are very similar as both uses backtracking)

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = []
        open_close = ["(", ")"]

        self.backtracking(n, "", output, open_close, 0, 0)

        return output

    def backtracking(self, n, current_parentheses, output, open_close, open_count, close_count):
        # Base case occurs when length of 'current_parentheses' is equal to 2*n
        if len(current_parentheses) == 2*n:
            output.append(current_parentheses)
            return

        # Recursive case
        for i in range(2):
            # Open parentheses
            if i == 0:
                if open_count < n:
                    self.backtracking(n, current_parentheses + open_close[i], output, open_close, open_count + 1, close_count)

            # Closed parentheses
            else:   # i == 1:
                if close_count < n and open_count > close_count:
                    self.backtracking(n, current_parentheses + open_close[i], output, open_close, open_count, close_count + 1)


solution = Solution()
print(solution.generateParenthesis(3))        # ["((()))","(()())","(())()","()(())","()()()"]
print(solution.generateParenthesis(1))        # ["()"]