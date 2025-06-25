class Solution:
    def groupAnagrams(self, strs):
        strs_sorted = []
        for string in strs:
            sorted_string = ''.join(sorted(string))
            strs_sorted.append(sorted_string)

        # print(strs_sorted)

        str_dict = {}
        for i in range(len(strs)):
            if (strs_sorted[i] in str_dict):
                str_dict[strs_sorted[i]].append(strs[i])
            else:
                str_dict[strs_sorted[i]] = [strs[i]]

        # print(str_dict)
        result = list(str_dict.values())

        return result
    

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))        # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(solution.groupAnagrams(["a"]))        # ["a"]