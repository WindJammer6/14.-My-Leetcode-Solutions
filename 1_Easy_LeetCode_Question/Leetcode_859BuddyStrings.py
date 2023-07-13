def check_duplicate(l):
    mySet = set(l)
    if len(mySet) == len(l):
        return False
    else:
        return True

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        s_list = []
        for i in s:
            s_list.append(i)

        goal_list = []
        for i in goal:
            goal_list.append(i)

        joined_list = []
        for i in s_list:
            joined_list.append(i)
        for i in goal_list:
            joined_list.append(i)

        
        combined_dictionary = dict(zip(s_list, goal_list))
        unmatching_char_list = [] 
        for index, value in combined_dictionary.items():
            if index != value:
                unmatching_char_list.append(index)


        #Checks if length of the 2 strings, 's' and 'goal' are the same
        if len(s) != len(goal):
            return False

        #Checks if all characters in 's' and 'goal' are the same (ignoring order of the characters)
        if list(sorted(s_list)) != list(sorted(goal_list)):
            return False
                
        
        #Checks if both lists are identical
        if s_list == goal_list:
            #Checks for any duplicates in the identical lists
            if check_duplicate(s_list) is True:

                if len(unmatching_char_list) > 2:
                    return False
                else:
                    return True
                
            else:
                return False
            
        counter = 0
        for i in range(len(s_list)):
            if s_list[i] != goal_list[i]:
                counter += 1
        if counter > 2:
            return False

        combined_dictionary = dict(zip(s_list, goal_list))

        unmatching_char_list = [] 
        for index, value in combined_dictionary.items():
            if index != value:
                unmatching_char_list.append(index)


        if len(unmatching_char_list) > 2 or len(unmatching_char_list) == 0:
            return False
        
        return True
    

solution = Solution()

test_string = "ab"
goal_string = "ab"

print(solution.buddyStrings(test_string, goal_string))
