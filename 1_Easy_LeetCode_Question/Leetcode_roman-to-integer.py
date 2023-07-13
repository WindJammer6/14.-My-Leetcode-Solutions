class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0

        roman_dictionary = { "I" : 1,
                             "V" : 5,
                             "X" : 10,
                             "L" : 50,
                             "C" : 100,
                             "D" : 500,
                             "M" : 1000
                             }
        
        reversed_s_string = list(reversed(s))
        print(reversed_s_string)


        temp_dictionary = {}
        for index, value in enumerate(reversed_s_string):
            temp_dictionary.update({index:value})
        print(temp_dictionary)


        for index, value in temp_dictionary.items():
            if index - 1 > -1:
                if roman_dictionary[value] < roman_dictionary[temp_dictionary[index-1]]:
                    integer -= roman_dictionary[value]
                    print(integer)
                else: 
                    integer += roman_dictionary[value]
                    print(integer)
            else:
                integer += roman_dictionary[value]
                print(integer)
                
        return integer
    
solution = Solution()

print(solution.romanToInt("DCXXI"))

