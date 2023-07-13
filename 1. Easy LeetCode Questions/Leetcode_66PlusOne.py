class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        index = -1

        for i in range(len(digits)):
            if digits[index] == 9:
                index -= 1
                print(index)
            else:
                digits[index] += 1
                break

        index = index + 1

        while True:
            if index != 0:
                digits[index] = 0
                index += 1
            if index == 0:
                break

        if digits[0] == 0:
            digits.insert(0,1)

        return digits
    
solution = Solution()

digits = [9,9,9]

print(solution.plusOne(digits))
