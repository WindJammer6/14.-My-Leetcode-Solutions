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

file_types_dictionary = {
    'C++': 'cpp',
    'Python': 'py',
    'Haskell': 'hs',
    'C': 'c',
    'Java': 'java',
    'C#': 'cs',
    'JavaScript': 'js',
    'SQL': 'sql'
}

# Define the folders and their corresponding difficulties
folders_difficulty = {
    '1_Easy_LeetCode_Questions': 'Easy',
    '2_Medium_LeetCode_Questions': 'Medium',
    '3_Hard_LeetCode_Questions': 'Hard'
}

def camel_to_words(s: str) -> str:
    # Insert spaces before capitals: InOrder -> In Order
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    # Handle acronyms: XMLParser -> XML Parser
    s = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', s)
    return s.strip()

def parse_tags(optional_paren_group: str | None) -> list[str]:
    """
    "(onInOrderTraversalAlgorithmandPreOrderTraversalAlgorithm)"
    -> ["In Order Traversal Algorithm", "Pre Order Traversal Algorithm"]

    "(onTwoPointers)"
    -> ["Two Pointers"]

    None -> []
    """
    if not optional_paren_group:
        return []

    raw = optional_paren_group.strip()[1:-1]  # remove '(' and ')'
    if raw.startswith("on"):
        raw = raw[2:]  # remove leading "on"

    raw = raw.strip()
    if not raw:
        return []

    # Split on 'and' only when next char is uppercase: "...AlgorithmandPre..." -> ["...Algorithm", "Pre..."]
    parts = re.split(r'and(?=[A-Z])', raw)
    tags = [camel_to_words(p) for p in parts if p.strip()]
    return tags

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
    if not line:
        continue

    parts = line.split("/")
    folder = parts[1] if len(parts) > 1 else ""

    # Matches: leetcode_123_question-title_(optional-info).ext
    m = re.search(r'\/.*leetcode_(\d+)_(.*?)_?(\(.*\))?\.(cpp|py|hs|c|java|cs|js|sql)$', line)

    if m:
        q_number = m.group(1)
        q_title = m.group(2).replace('-', ' ')
        extra = m.group(3)  # "(on...)" or None
        tags = parse_tags(extra)

        sol = "https://github.com/WindJammer6/14.-My-Leetcode-Solutions/blob/main" + line[1:]
        task = f"https://leetcode.com/problems/{q_title.lower().replace(' ', '-')}"
        difficulty = folders_difficulty.get(folder, 'Unknown')

        # [index, title, sol_url, tags_list, difficulty, task_url]
        things_to_write.append([q_number, q_title, sol, tags, difficulty, task])

def print_table():
    things_to_write.sort(key=lambda x: int(x[0]))  # Sort by question index

    solution_types = []
    tags_set = set()

    for index, (q_number, q_title, sol, tags, difficulty, task) in enumerate(things_to_write):
        # Detect solution language by file extension
        for lang, ext in file_types_dictionary.items():
            if sol.endswith(ext):
                solution_types.append((lang, sol))
                break

        # Accumulate tags (each paradigm becomes an individual tag)
        if tags:
            tags_set.update(tags)

        # If next row is same LeetCode problem, keep accumulating links/tags
        if index != len(things_to_write) - 1 and things_to_write[index + 1][5] == task:
            continue

        # Build row
        line = f"| {index + 1} | {q_number} | [{q_title}]({task}) | "

        # Multiple solution links in the same cell
        for lang, url in solution_types:
            line += f"[{lang}]({url})"

        # Render each paradigm as a tag
        final_tags = ""
        if tags_set:
            # Use <br> so tags wrap nicely in GitHub tables
            final_tags = "<br>".join(f"`{t}`" for t in sorted(tags_set))

        line += f" | {final_tags} | {difficulty} |"
        print(line)

        solution_types.clear()
        tags_set.clear()

print_table()
