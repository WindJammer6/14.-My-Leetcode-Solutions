class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_string = s.split()
        print(word_string)

        return len(word_string[-1])
    
solution = Solution()

sentence = "   fly me   to   the moon  "

print(solution.lengthOfLastWord(sentence))