class Solution:
    def characterReplacement(self, s, k):

        n = len(s)

        if n == 1:
            return 1
        
        fp = 0
        sp = 1

        most_same_letter = s[fp]
        most_same_letter_count = 1
        longest_valid_count = 0

        counter_dict = {s[fp] : 1}

        while sp < n:
            if s[sp] == most_same_letter:
                most_same_letter_count += 1

            if s[sp] not in counter_dict:
                counter_dict.update({s[sp] : 1})
            else:
                counter_dict[s[sp]] += 1
            

            # Finding the newest most common letter, and its respective count
            most_same_new_letter = ""
            most_same_new_letter_count = 0
            for key, value in counter_dict.items():
                if value > most_same_new_letter_count:
                    most_same_new_letter_count = value
                    most_same_new_letter = key
            if most_same_new_letter != most_same_letter:
                most_same_letter = most_same_new_letter
            most_same_letter_count = counter_dict[most_same_letter]
            # print(f"most_same_letter: {most_same_letter}")
            # print(f"most_same_letter_count: {most_same_letter_count}")
            # print(f"sp: {sp}")
            # print(f"fp: {fp}")
            # print(f"not_most_same_letter_count: {sp - fp - most_same_letter_count + 1}")
    

            # If the number of not most same letter count exceeds k, then we shift the window up by 1
            if (sp - fp - most_same_letter_count + 1 > k):
                counter_dict[s[fp]] -= 1
                fp += 1


            # Update longest valid count
            if (most_same_letter_count + k > longest_valid_count):
                if (sp - fp - most_same_letter_count + 1 < k):
                    longest_valid_count = most_same_letter_count + sp - fp - most_same_letter_count + 1
                else:
                    longest_valid_count = most_same_letter_count + k
                # print(f"Updated longest valid count: {longest_valid_count}")

            sp += 1

        return longest_valid_count


solution = Solution()
print(solution.characterReplacement("ABAB", 2))             # 4
print(solution.characterReplacement("AABABBA", 1))          # 4
print(solution.characterReplacement("ABCCCBCBABAC", 3))     # 7