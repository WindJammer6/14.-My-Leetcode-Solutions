class Solution:

    # My version, but for some reason keeps failing and occasionally some test cases will give this error:

        # TypeError: unsupported operand type(s) for -: 'NoneType' and 'int' ~~~~~~~~~~~~^~~ if intervals[found_index - 1][1] >= newInterval[0]: Line 58 in insert (Solution.py) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ret = Solution().insert(param_1, param_2) Line 119 in _driver (Solution.py) _driver() Line 134 in <module> (Solution.py)

    # def binary_search_algorithm(self, intervals, startNewInterval):
    #     n = len(intervals)

    #     if 0 < n <= 3:
    #         for i in range(n):
    #             if startNewInterval < intervals[i][0]:
    #                 return i
    #         return n

    #     left_index = 0
    #     right_index = n - 1
    #     middle_index = (left_index + right_index) // 2

    #     while right_index > left_index:

    #         if (startNewInterval > intervals[middle_index][0]):
    #             if startNewInterval <= intervals[middle_index + 1][0]:
    #                 return middle_index + 1
    #             else:
    #                 left_index = middle_index
    #                 middle_index = (left_index + right_index) // 2

    #         elif (startNewInterval < intervals[middle_index][0]):
    #             if startNewInterval >= intervals[middle_index - 1][0]:
    #                 return middle_index
    #             else:
    #                 right_index = middle_index
    #                 middle_index = (left_index + right_index) // 2

    #         else:
    #             return middle_index


    # ChatGPT's version, works:
    def binary_search_algorithm(self, intervals, startNewInterval):
        n = len(intervals)
        left, right = 0, n - 1
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] >= startNewInterval:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


    def insert(self, intervals, newInterval):
        if intervals == []:
            return [newInterval]

        resultant_interval = newInterval

        # Using binary search algorithm to quickly find where to put the new interval
        found_index = self.binary_search_algorithm(intervals, newInterval[0])
        print(f"Found index: {found_index}")

    
        # After finding where to put the new interval, check if need to merge with the previous interval
        if found_index == 0:
            merged_with_previous_interval = False
            if (intervals[0][0] <= newInterval[1]):
                resultant_interval = [min(newInterval[0], intervals[0][0]),
                                    max(newInterval[1], intervals[0][1])]
            else:
                resultant_interval = newInterval
            print(resultant_interval)

        else:
            merged_with_previous_interval = False
            if intervals[found_index - 1][1] >= newInterval[0]:
                if intervals[found_index - 1][1] > newInterval[1]:
                    return intervals
                else:
                    resultant_interval = [intervals[found_index - 1][0], newInterval[1]]
                    merged_with_previous_interval = True

        # Then check if need to merge with any later intervals
        current_i = found_index
        while current_i < len(intervals) and intervals[current_i][0] <= resultant_interval[1]:
            if intervals[current_i][1] > resultant_interval[1]:
                resultant_interval = [resultant_interval[0], intervals[current_i][1]]

            current_i += 1
            print(resultant_interval)

        # Replace those affected intervals with the resultant interval
        output = []
        if merged_with_previous_interval == True:
            for i in range(found_index - 1):
                output.append(intervals[i])
        else:
            for i in range(found_index):
                output.append(intervals[i])
        
        output.append(resultant_interval)
        
        for i in range(current_i, len(intervals)):
            output.append(intervals[i])


        return output
    

solution = Solution()
print(solution.insert([[1,3],[6,9]], [2,5]))                                # [[1,5],[6,9]]
print(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))           # [[1,2],[3,10],[12,16]]