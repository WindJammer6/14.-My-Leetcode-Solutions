class Solution:
    def minCostToMoveChips(self, position):
        
        cost = 0
        
        number_of_even_numbers = 0
        number_of_odd_numbers = 0
        
        for i in position:
            if i % 2 == 0:
                number_of_even_numbers += 1
            else:
                number_of_odd_numbers += 1
        
        if number_of_even_numbers > number_of_odd_numbers:
            cost = number_of_odd_numbers
        else:
            cost = number_of_even_numbers

        return cost

solution = Solution()
print(solution.minCostToMoveChips([1,2,3]))             # 1
print(solution.minCostToMoveChips([2,2,2,3,3]))         # 2
print(solution.minCostToMoveChips([1,1000000000]))      # 1