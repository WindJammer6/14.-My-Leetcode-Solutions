class Solution:
    def canAttendMeetings(self, intervals):
        
        intervals.sort()

        flatten_list = []

        for i in intervals:
            for j in i:
                flatten_list.append(j)

        sorted_list = sorted(flatten_list)

        if sorted_list == flatten_list:
            return True
        else:
            return False

solution = Solution()
print(solution.canAttendMeetings([[0,30],[5,10],[15,20]]))  # False
print(solution.canAttendMeetings([[7,10],[2,4]]))           # True