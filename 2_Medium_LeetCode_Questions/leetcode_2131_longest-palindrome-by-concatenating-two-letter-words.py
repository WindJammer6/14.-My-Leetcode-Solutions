class Solution:
    
    # Approach:
    # So there are 2 types of element in 'words'. Either:
    # - both are same character
    # - both are different character

    # If both are same character,
    # -> If there is an even number of that this word, then the 2 to output, by the number of even number pairs
    # -> BUT, we can only add such a 'both are same character' element once into the output! If there are more 
    #    than 1 both are same character' element, then the rest will not be added into the output.

    # If both are different character 
    # -> we need to be able to find a mirroring pair of the same characters. If mirroring pair is found, add
    #    2 to output, else, don't do anything

    def longestPalindrome(self, words) -> int:
        output = 0

        memory_diff = {}
        memory_same = {}

        # First, add all the elements in a memory dictionary. Elements that are both are same character
        # will be added into the 'memory_same' dictionary, while elements that are both are different character
        # will be added into the 'memory_diff' dictionary.
        for word in words:
            # If both are the same character
            if word[0] == word[1]:
                if word in memory_same:
                    memory_same[word] += 1
                else:
                    memory_same[word] = 1

            # If both are different character
            else:
                if word in memory_diff:
                    memory_diff[word] += 1
                else:
                    memory_diff[word] = 1

        print(memory_diff)
        print(memory_same)


        # Handling both are different character elements
        for key, value in memory_diff.items():
            mirror = ""
            mirror = key[1] + key[0]

            if mirror in memory_diff:
                # To handle the case if there are multiple pairs
                for i in range(min(memory_diff[key], memory_diff[mirror])):
                    output += 2
            else:
                pass


        # Handling both are same character elements
        if len(memory_same) == 1:
            for key, value in memory_same.items():
                output += value * 2

        elif len(set(memory_same.values())) == 1:
            output += 2

        else:
            first_odd_done = False
            for i in memory_same.values():

                if (first_odd_done == False) and (i % 2 != 0):
                    output += 2
                    first_odd_done = True

                output += (i // 2) * 2 * 2

        return output



solution = Solution()
print(solution.longestPalindrome(["lc","cl","gg"]))                 # 6
print(solution.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))  # 8
print(solution.longestPalindrome(["cc","ll","xx"]))                 # 2
print(solution.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))                 # 22
print(solution.longestPalindrome(["bb","bb"]))                      # 4
