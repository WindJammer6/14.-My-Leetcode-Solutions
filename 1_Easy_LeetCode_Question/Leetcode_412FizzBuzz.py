class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        number_list = []
        for i in range(1, n+1):
            number_list.append(str(i))
        
        for i in range(len(number_list)):
            if int(number_list[i]) % 3 == 0 and int(number_list[i]) % 5 != 0:
                number_list[i] = "Fizz"
            elif int(number_list[i]) % 5 == 0 and int(number_list[i]) % 3 != 0:
                number_list[i] = "Buzz"
            elif int(number_list[i]) % 3 == 0 and int(number_list[i]) % 5 == 0:
                number_list[i] = "Fizz" + "Buzz"
            else:
                pass

        return number_list  

solution = Solution()

print(solution.fizzBuzz(15))