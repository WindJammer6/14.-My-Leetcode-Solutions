import os
import re

start_of_readme = '''
# List of LeetCode Questions Solved
![Auto Update](https://github.com/WindJammer6/14.-My-Leetcode-Solutions/actions/workflows/update_readme.yml/badge.svg)
| No. | Index | Question Title | Solution | Difficulty |
| --- | ----- | -------------- | -------- | ---------- |'''

print(start_of_readme)

file_types_dictionary = {'C++': 'cpp', 'Python': 'py', 'Haskell': 'hs', 'C': 'c'}

# Getting the LeetCode Solutions
stream = os.popen('find . -type f -iname "leetcode*.py"')
lines = stream.readlines()

things_to_write = []
for line in lines:
    line = line.strip()
    folder = line.split("/")[1]  # Get the folder name

    # Matches leetcode_123_question-title_(optional-info).py
    m = re.search(r'\/.*leetcode_(\d+)_(.*?)_?(\(.*\))?\.py', line)

    if m:
        q_number = m.group(1)  # Get the number from the file name
        q_title = m.group(2).replace('-', ' ')  # Get the question title and replace hyphens with spaces
        sol = "https://github.com/WindJammer6/14.-My-Leetcode-Solutions/blob/main" + line[1:]  # Construct the solution URL
        task = f"https://leetcode.com/problems/{q_title.lower().replace(' ', '-')}"  # Construct the task URL

        things_to_write.append([q_number, q_title, sol, folder, task])

def print_table():
    things_to_write.sort(key=lambda x: int(x[0]))  # Sort the entries based on the index column

    solution_types = []
    for index, (q_number, q_title, sol, folder, task) in enumerate(things_to_write):
        for k, v in file_types_dictionary.items():
            if sol.endswith(v):
                solution_types.append((k, sol))
                break

        if index != len(things_to_write) - 1:
            if things_to_write[index + 1][4] == task:
                continue

        line = f"| {index + 1} | {q_number} | [{q_title}]({task}) | "
        for solution_type, solution in solution_types:
            line += f"[{solution_type}]({solution}), "

        line += f"| {folder} |"  # Add the folder as the difficulty column
        print(line)

        solution_types.clear()

print_table()
