class Solution:
    def merge(self, intervals):
        intervals.sort()
        print(intervals)

        output = [intervals[0]]
        print(output)

        for i in range(len(intervals) - 1):
            if (output[-1][1] >= intervals[i+1][0]): 
                if (output[-1][1] < intervals[i+1][1]):
                    output[-1][1] = intervals[i+1][1]
                else:
                    pass

            else:
                output.append(intervals[i+1])

            print(output)

        return output

                
solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))     # [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]]))                    # [[1,5]]
print(solution.merge([[4,7],[1,4]]))                    # [[1,7]]