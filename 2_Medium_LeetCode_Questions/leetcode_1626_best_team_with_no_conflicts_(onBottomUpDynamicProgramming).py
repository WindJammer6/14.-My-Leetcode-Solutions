# The bottom-up dynamic programming (with tabulation) code is partially taken from my school's
# lecture notes, but I identified the recurrence that relates the sub-problems, the sub-problems
# and base cases for this question and modified the top-down dynamic programming (with tabulation)
# code to this context to answer this question

# Using an example:
# players1 = [(1, 1), (3, 2), (5, 3), (10, 4), (15, 5)] (this will be a sorted list in terms of age (the second argument in each tuple))

# Let:
# - j be indexing in players1
# - yj be player's age in players1 
# - Each cell contains the maximum score that can be obtained at that player's index in players1

#             j →      0     1     2     3     4    
#                    (yj=1)(yj=2)(yj=3)(yj=4)(yj=5)   
#          Player      1     4     9     19     34        


# Using another example:
# players2 = [(5, 1), (1, 8), (2, 9), (3, 10)] (this will be a sorted list in terms of age (the second argument in each tuple))

# Let:
# - j be indexing in players2
# - yj be player's age in players2 
# - Each cell contains the maximum score that can be obtained at that player's index in players2

#             j →      0     1     2     3   
#                    (yj=1)(yj=8)(yj=9)(yj=10)   
#          Player      5     5     5     6      

# Recurrence:
# dp[i] = max(players[i][1], max{ dp[j] + players[i][1] for all j < i where players[j][1] <= players[i][1] })

# Subproblems:
# Compute dp[i]: Maximum team score that ends with the i-th player (after sorting)

# Base cases:
# - dp[i] = players[i][1] for each player i (each player can form a team by themselves)


class Solution:
    def bestTeamScore(self, scores, ages):
        players = []
        for i in range(len(scores)):
            players.append((scores[i], ages[i]))

        # Code referenced from: 
        # - https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value (Stack Overflow)
        # - https://blog.finxter.com/5-best-ways-to-sort-a-list-of-tuples-by-first-and-second-element-in-python/ (finxter)
        players = sorted(players, key=lambda x: (x[1], x[0]))
        print(players)


        # Bottom-up dynamic programming approach
        dp = []

        for i in range(len(scores)):
            dp.append(players[i][0])

        for j in range(len(dp)):
            for k in range(j):
                if players[k][0] <= players[j][0]:
                    dp[j] = max(dp[j], dp[k] + players[j][0])
        
        print(dp)

        return max(dp)


solution = Solution()
print(solution.bestTeamScore([1,3,5,10,15], [1,2,3,4,5]))   # 34
print(solution.bestTeamScore([4,5,6,5], [2,1,2,1]))         # 16
print(solution.bestTeamScore([1,2,3,5], [8,9,10,1]))        # 6
print(solution.bestTeamScore([319776,611683,835240,602298,430007,574,142444,858606,734364,896074], [1,1,1,1,1,1,1,1,1,1]))      # 5431066