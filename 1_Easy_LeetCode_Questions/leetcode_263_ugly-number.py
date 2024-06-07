# With reference from this article: https://www.pythonforbeginners.com/basics/find-prime-factors-of-a-number-in-python 
# (Python for Beginners, titled: 'Find Prime Factors Of A Number in Python', which provided the pseudocode for the
# algorithm to find the prime factors of a number)

# What are Prime Factors?
# Prime Factors of any given number are those numbers that divide the given number completely leaving no remainder.
# In the context of prime factorization, the goal is to break down a number into a product of prime numbers such as,
#       '315 = 3 x 3 x 5 x 7'. 

# Since prime numbers are defined as numbers greater than 1 that have no positive divisors other than 1 and themselves, 
# doing, 
#       '315 = 1 x 315'
# does not align with the concept of prime factorization.

# /////////////////////////////////////////////////////////////////////////////////////////


class Solution:
    def isUgly(self, n: int) -> bool:

        limited_prime_factors_list = [2,3,5]

        if n == 1:
            return True 
        
        if n < 0 or n == 0:
            return False
        


        # This section of the code is referenced from the pseudocode for the algorithm to find the prime factors of a number 
        # provided in the reference article mentioned above
        dividing_number = 2
        list_of_unique_prime_factors_of_a_number = []

        while n != 1:
            
            while n % dividing_number == 0:    
                n = n / dividing_number 
                print(n)

                if dividing_number not in list_of_unique_prime_factors_of_a_number:
                    list_of_unique_prime_factors_of_a_number.append(dividing_number)
            
            # For cases where if the prime factor 5 is not the last largest possible prime factor, and there are larger prime 
            # factors than 5 of the number
            if (dividing_number >= 5) and (n != 1):
                return False
            # For cases where if the prime factor 5 is the last possible prime factor, and there are no other larger prime 
            # factors than 5 
            elif (dividing_number >= 5) and (n == 1):
                break
            else:
                pass

            dividing_number += 1



        if set(list_of_unique_prime_factors_of_a_number).issubset(set(limited_prime_factors_list)):
            return True
        else:
            return False
    

solution = Solution()
number = 5
print(solution.isUgly(number))