class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x : x[0])

        # Flatten the sorted intervals
        flatten_intervals = []
        for i in intervals:
            flatten_intervals.append(i[0])
            flatten_intervals.append(i[1])

        # print(flatten_intervals)

        # Number of conflicts = number of intervals to remove
        conflict = 0
        for i in range(2, len(flatten_intervals), 2):
            # print(i)
            if flatten_intervals[i] < flatten_intervals[i - 1]:
                conflict += 1
                # print("Before")
                # print(f"i: {i}")
                # print(f"FI: {flatten_intervals[i]}")
                # print(f"FI: {flatten_intervals[i + 1]}")
                # print(f"FI: {flatten_intervals[i - 1]}")

                # How do we decide if there is an overlap, which interval to remove? So the important point is here, among the 2 overlapping intervals, we should always remove the interval with a later end time. Why? Because it leaves more room for future intervals to not overlap, which hence will keep the number of intervals to be removed to a minimum that will make the rest of the intervals non-overlapping.
                if flatten_intervals[i + 1] < flatten_intervals[i - 1]:
                    flatten_intervals[i - 2] = flatten_intervals[i]
                    flatten_intervals[i - 1] = flatten_intervals[i]
                else:
                    flatten_intervals[i] = flatten_intervals[i - 1]
                    flatten_intervals[i + 1] = flatten_intervals[i - 1]
                # print("After")
                # print(f"i: {i}")
                # print(f"FI: {flatten_intervals[i]}")
                # print(f"FI: {flatten_intervals[i + 1]}")
                # print(f"FI: {flatten_intervals[i - 1]}")

        # print(flatten_intervals)
        
        return conflict


solution = Solution()
print(solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))    # 1
print(solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))          # 2
print(solution.eraseOverlapIntervals([[1,2],[2,3]]))                # 0