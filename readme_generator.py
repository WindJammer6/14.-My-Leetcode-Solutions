import os
import re

start_of_readme = '''# 14.-My-Leetcode-Solutions :dart:
Here are some of my accepted attempts at some Leetcode questions. And hey, I managed to learn how to automate the process of updating my README.md file whenever I solved and 
upload a new solution to a Leetcode question in this repository!

My Leetcode account: https://leetcode.com/WindJammer6/

<ins>Disclaimer</ins>: I am a student programmer, these solutions that I have attached in this repository are not perfect answers to the Leetcode questions (in terms of design 
and Time and Space Big O Notation Complexity), but are just merely my sharing of my own approach to the questions.
They do answer the Leetcode questions, but there are definitely better answer codes out there.

# List of Leetcode Questions Solved
![Auto Update](https://github.com/WindJammer6/14.-My-Leetcode-Solutions/actions/workflows/update_readme.yml/badge.svg)
| No. | Leetcode Question Index | Leetcode Question Title | Solution | Tags | Difficulty |
| --- | ----------------------- | ----------------------- | -------- | ---- | ---------- |'''

print(start_of_readme)

file_types_dictionary = {'C++': 'cpp', 'Python': 'py', 'Haskell': 'hs', 'C': 'c', 'Java': 'java', 'C#': 'cs', 'JavaScript': 'js', 'SQL': 'sql'}

# Define the folders and their corresponding difficulties
folders_difficulty = {
    '1_Easy_LeetCode_Questions': 'Easy',
    '2_Medium_LeetCode_Questions': 'Medium',
    '3_Hard_LeetCode_Questions': 'Hard'
}

def camel_to_words(s: str) -> str:
    # Insert spaces before capital letters: InOrder -> In Order
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    # Also handle sequences like "XMLParser" -> "XML Parser" (optional)
    s = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', s)
    return s.strip()

def parse_tags(optional_paren_group: str | None) -> str:
    """
    optional_paren_group is something like "(onInOrderTraversalAlgorithmandPreOrderTraversalAlgorithm)"
    or None if not present.
    Returns a string like "In Order Traversal Algorithm<br>Pre Order Traversal Algorithm"
    """
    if not optional_paren_group:
        return ""

    raw = optional_paren_group.strip()[1:-1]  # remove surrounding parentheses
    if raw.startswith("on"):
        raw = raw[2:]  # drop leading 'on'

    raw = raw.strip()
    if not raw:
        return ""

    # Split on connector "and" only when followed by a capital letter:
    # "...AlgorithmandPre..." -> ["...Algorithm", "Pre..."]
    parts = re.split(r'and(?=[A-Z])', raw)

    # Convert each CamelCase chunk to words
    parts = [camel_to_words(p) for p in parts if p.strip()]

    # Use <br> so multiple paradigms show nicely inside a single markdown cell
    return "<br>".join(parts)

# Getting the LeetCode Solutions
stream = os.popen(
    'find . -type f '
    '-iname "leetcode_*.py" '
    '-o -iname "leetcode_*.java" '
    '-o -iname "leetcode_*.cpp" '
    '-o -iname "leetcode_*.c" '
    '-o -iname "leetcode_*.hs" '
    '-o -iname "leetcode_*.cs" '
    '-o -iname "leetcode_*.js" '
    '-o -iname "leetcode_*.sql" '
)
lines = stream.readlines()

things_to_write = []
for line in lines:
    line = line.strip()
    folder = line.split("/")[1]  # Get the folder name

    # Matches leetcode_123_question-title_(optional-info).(programming-language-file-type)
    m = re.search(r'\/.*leetcode_(\d+)_(.*?)_?(\(.*\))?\.(cpp|py|hs|c|java|cs|js|sql)', line)

    if m:
        q_number = m.group(1)
        q_title = m.group(2).replace('-', ' ')
        extra = m.group(3)  # "(onSomething...)" or None
        tags = parse_tags(extra)

        sol = "https://github.com/WindJammer6/14.-My-Leetcode-Solutions/blob/main" + line[1:]
        task = f"https://leetcode.com/problems/{q_title.lower().replace(' ', '-')}"
        difficulty = folders_difficulty.get(folder, 'Unknown')

        # Store tags as a new field
        things_to_write.append([q_number, q_title, sol, tags, difficulty, task])

def print_table():
    things_to_write.sort(key=lambda x: int(x[0]))

    solution_types = []
    tags_set = set()

    for index, (q_number, q_title, sol, tags, difficulty, task) in enumerate(things_to_write):
        # Collect solution link type
        for k, v in file_types_dictionary.items():
            if sol.endswith(v):
                solution_types.append((k, sol))
                break

        # Collect tags across multiple solutions for the same problem
        if tags:
            tags_set.add(tags)

        # If next entry is the same LeetCode problem, keep accumulating
        if index != len(things_to_write) - 1 and things_to_write[index + 1][5] == task:
            continue

        # Build output row (print once per problem)
        line = f"| {index + 1} | {q_number} | [{q_title}]({task}) | "

        for solution_type, solution in solution_types:
            line += f"[{solution_type}]({solution})"

        # Decide final tags for the grouped row
        final_tags = ""
        if tags_set:
            # If multiple tag strings exist, join them (rare but safe)
            final_tags = "<br>".join(sorted(tags_set))

        line += f" | {final_tags} | {difficulty} |"
        print(line)

        solution_types.clear()
        tags_set.clear()

print_table()
