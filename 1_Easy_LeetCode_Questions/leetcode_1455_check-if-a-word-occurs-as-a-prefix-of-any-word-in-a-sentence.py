class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list = sentence.split(" ")

        print(sentence_list)

        a = b = 0
        counter = 0

        for i in sentence_list:
            if len(i) < len(searchWord):
                pass

            else:
                while counter < len(searchWord):
                    if searchWord[a] != i[b]:
                        break
                    else:
                        counter += 1
                        a += 1
                        b += 1
                
                if counter == len(searchWord):
                    return sentence_list.index(i) + 1

        return -1


sentence = "hellohello hellohellohello"
searchWord = "ello"
solution = Solution()

print(solution.isPrefixOfWord(sentence, searchWord))