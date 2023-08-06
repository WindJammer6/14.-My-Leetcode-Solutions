class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        list_rank = score.copy()
        print(score)

        #Creating 'list_rank' (arranging the List in descending order)
        list_rank.sort(reverse=True)

        #Creating 'list_rank_sorted'
        list_rank_sorted = list_rank.copy()
        if len(list_rank_sorted) > 0:
            list_rank_sorted[0] = "Gold Medal"
        if len(list_rank_sorted) > 1:
            list_rank_sorted[1] = "Silver Medal"
        if len(list_rank_sorted) > 2:
            list_rank_sorted[2] = "Bronze Medal"

        if len(list_rank_sorted) > 3:
            for i in range(3, len(list_rank_sorted)):
                print(i)
                list_rank_sorted[i] = str(i + 1)
            
        print(list_rank_sorted)
        print(list_rank)

        #Changing the initial 'score' List to get each athlete's ranking
        for i in range(len(score)):
            score[i] = list_rank_sorted[list_rank.index(score[i])]
        print(score)

        return score
        
list = [5,4,3,2,1]
solution = Solution()
print(solution.findRelativeRanks(list))