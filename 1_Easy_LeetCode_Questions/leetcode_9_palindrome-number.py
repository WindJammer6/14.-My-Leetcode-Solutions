#Solving this Leetcode question using Two Pointers approach
class Solution:
    def isPalindrome(self, x: int) -> bool:

        x_list = []

        for i in str(x):
            x_list.append(i)

        #Taking care of the case if the input has only 2 characters
        if len(x_list) == 2:
            if x_list[0] == x_list[1]:
                return True
            else:
                return False
            
        #Taking care of the case if the input has only 1 character
        if len(x_list) == 1:
            return True

        #Taking care of cases if the input has > 2 characters
        front_index = 0
        back_index = len(x_list) - 1

        while True:
            
            #The Two Pointers
            front = x_list[front_index]
            back = x_list[back_index]

            if front != back:
                return False

            else:
                if front_index == back_index or front_index + 1 == back_index:
                    break
                else:
                    front_index += 1
                    back_index -= 1

        return True

number = 1000030001

solution = Solution()

print(solution.isPalindrome(number))