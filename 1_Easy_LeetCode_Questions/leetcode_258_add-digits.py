class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num_string = f"{num}"
            temp = 0

            for i in num_string:
                temp += int(i)

            num = temp

        return num

solution = Solution()
print(solution.addDigits(38))       # 2
print(solution.addDigits(0))        # 0