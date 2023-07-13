class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack_list = []

        for char in s:
            if char == '(' or char == '{' or char == '[': 
                stack_list.insert(0, char)
            
            if char == ')' or char == '}' or char == ']':
                if len(stack_list) == 0:
                    return False
                else:
                    if stack_list[0] == match_dict[char]:
                        stack_list.remove(match_dict[char])
                    else:
                        return False
        
        if len(stack_list) == 0:
            return True
        else:
            return False

solution = Solution()

string = "({a+b})"                  #True      
string2 = "))((a+b}{"               #False
string3 = "((a+b))"                 #True
string4 = "))"                      #False
string5 = "[a+b]*(x+2y)*{gg+kk}"    #True
string6 = "(]"
string7 = "([)]"

print(solution.isValid(string))
print(solution.isValid(string2))
print(solution.isValid(string3))
print(solution.isValid(string4))
print(solution.isValid(string5))
print(solution.isValid(string6))
print(solution.isValid(string7))

