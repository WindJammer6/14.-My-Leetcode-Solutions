# This 'WordDictionary' Data Structure is essentially a Trie Data Structure

# I was able to handle cases without dots '.', but when it came to dots '.', I had to refer to this solution: https://www.youtube.com/watch?v=BTf05gs_8iU (Neetcode) 
# (YouTube video by Neetcode titled, "Design Add and Search Words Data Structure - Leetcode 211 - Python")

# Essentially, to handle the dots '.', we will need to do an additional Depth First Search Algorithm (see the video for a more detailed explanation as to why)

class TrieNode:
    def __init__(self, character):
        self.children = {}
        self.character = character
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word):
        iterator = self.root

        for i in range(len(word)):
            # print(iterator.children)
            if word[i] not in iterator.children:
                iterator.children.update({word[i] : TrieNode(word[i])})

            iterator = iterator.children[word[i]]

        iterator.is_word = True

    def search(self, word):
        iterator = self.root

        for i in range(len(word)):
            if word[i] == '.':
                return self.dfsHelper(word[i:], iterator)

            if word[i] not in iterator.children:
                return False

            iterator = iterator.children[word[i]]
        
        return iterator.is_word

    # Used to handle dot '.' cases
    def dfsHelper(self, word, current_node):
        if len(word) == 0:
            return current_node.is_word
        
        # Handling dot '.' cases
        if word[0] == '.':
            for i in current_node.children.values():
                if self.dfsHelper(word[1:], i) == True:
                    return True
            return False
        # Handling non-dot '.' cases
        else:
            if word[0] in current_node.children:
                return self.dfsHelper(word[1:], current_node.children[word[0]])
            else:
                return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

obj1 = WordDictionary()
output1 = ["null"]
input_commands1 = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
input_words1 = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]] 
for i in range(1, len(input_commands1)):
    if input_commands1[i] == "addWord":
        obj1.addWord(input_words1[i][0])
        output1.append("null")
    else:       # if input_commands1[i] == "search"
        output1.append(obj1.search(input_words1[i][0]))
print(output1)                                              # [null,null,null,null,false,true,true,true]


obj2 = WordDictionary()
output2 = ["null"]
input_commands2 = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
input_words2 = [[],["bad"],["dad"],["mad"],["pad"],["bad"],["pad"],["bat"]]
for i in range(1, len(input_commands2)):
    if input_commands2[i] == "addWord":
        obj2.addWord(input_words2[i][0])
        output2.append("null")
    else:       # if input_commands2[i] == "search"
        output2.append(obj2.search(input_words2[i][0]))
print(output2)                                              # [null,null,null,null,false,true,false,false]


obj3 = WordDictionary()
output3 = ["null"]
input_commands3 = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
input_words3 = [[],["bad"],["dad"],["mad"],["pad"],["bad"],["dad"],["mad"]]
for i in range(1, len(input_commands3)):
    if input_commands3[i] == "addWord":
        obj3.addWord(input_words3[i][0])
        output3.append("null")
    else:       # if input_commands3[i] == "search"
        output3.append(obj3.search(input_words3[i][0]))
print(output3)                                              # [null,null,null,null,false,true,true,true]


obj4 = WordDictionary()
output4 = ["null"]
input_commands4 = ["WordDictionary","search"]
input_words4 = [[],["a"]]
for i in range(1, len(input_commands4)):
    if input_commands4[i] == "addWord":
        obj4.addWord(input_words4[i][0])
        output4.append("null")
    else:       # if input_commands4[i] == "search"
        output4.append(obj4.search(input_words4[i][0]))
print(output4)                                              # [null,false]


obj5 = WordDictionary()
output5 = ["null"]
input_commands5 = ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
input_words5 = [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
for i in range(1, len(input_commands5)):
    if input_commands5[i] == "addWord":
        obj5.addWord(input_words5[i][0])
        output5.append("null")
    else:       # if input_commands5[i] == "search"
        output5.append(obj5.search(input_words5[i][0]))
print(output5)                                              # [null,null,null,true,true,false,true,false,false]
