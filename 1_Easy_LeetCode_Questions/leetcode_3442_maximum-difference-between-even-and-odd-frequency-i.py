class Solution:
    def maxDifference(self, s: str) -> int:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        print(dict)

        max_odd_frequency = 0
        min_even_frequency = 10000000000
        for key, value in dict.items():
            if (value % 2 == 0) and (value < min_even_frequency):
                min_even_frequency = value
            elif (value % 2 != 0) and (value > max_odd_frequency):
                max_odd_frequency = value
            else:
                print("No change to the 'max_odd_frequency' and 'min_even_frequency'!")

        print(max_odd_frequency)
        print(min_even_frequency)

        return (max_odd_frequency - min_even_frequency)
        

solution = Solution()
print(solution.maxDifference("aaaaabbc"))   # 3
print(solution.maxDifference("abcabcab"))   # 1
