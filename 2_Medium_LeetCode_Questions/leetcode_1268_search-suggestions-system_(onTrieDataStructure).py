# Approach:
# With reference to this Leetcode solution's pseudocode and logic: 
# https://leetcode.com/problems/search-suggestions-system/solutions/508775/python-trie-sort-trie-heap/ (ztonege on Leetcode)

# Visual representation of the slightly modified Trie Data Structure that was used to solve this Leetcode question:
#       #####
#       #   #
#       #####
#         |
#        \ /
#       #####
#       # m #  --> [mobile, moneypot, monitor]
#       #####
#         |
#        \ /
#       #####
#       # o # --> [mobile, moneypot, monitor]
#       #####
#         |
#        \ /
#       #####
#       # u # --> [mouse]
#       #####
#         |
#        \ /
#       #####
#       # s # --> [mouse]
#       #####
#         |
#        \ /
#       #####
#       # e #
#       #####

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products, searchWord):
        output = []

        products.sort()

        root = TrieNode()

        # Create the Trie-like Data Structure
        for word in products:
            iterator = root

            for char in word:
                if char in iterator.children:
                    pass
                else:
                    iterator.children.update({char : TrieNode()})

                iterator = iterator.children[char]

                if len(iterator.suggestions) < 3:
                    iterator.suggestions.append(word)


        # Retrieve the 3 suggested product names
        iterator2 = root
        for char in searchWord:
            if char in iterator2.children:
                iterator2 = iterator2.children[char]
                output.append(iterator2.suggestions)
            else:
                while len(output) < len(searchWord):
                    output.append([])
                break

        return output


solution = Solution()
print(solution.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
# [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

print(solution.suggestedProducts(["havana"], "havana"))
# [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]