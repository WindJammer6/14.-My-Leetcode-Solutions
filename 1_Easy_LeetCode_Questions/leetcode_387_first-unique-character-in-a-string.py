class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_dictionary = {}

        for i in s:
            if i not in string_dictionary:
                string_dictionary.update({i : 1})
            else:
                string_dictionary[i] += 1

        print(string_dictionary)

        for key, value in string_dictionary.items():
            if value == 1:
                return s.index(key)
        return -1


string = "loveleetcode"

solution = Solution()

print(solution.firstUniqChar(string))