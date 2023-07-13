import os, re

start_of_readme = '''
# List of Kattis Questions Solved
![Auto Update](https://github.com/WindJammer6/14.-My-Leetcode-Solutions/actions/workflows/update_readme.yml/badge.svg)
| Index | Question Title | Solution |
| ----- | -------------- | -------- |'''

print(start_of_readme)

file_types_dictionary = {'C++': 'cpp', 'Python': 'py', 'Haskell': 'hs', 'C': 'c'}

#Getting the Leetcode Solutions
stream = os.popen('find | grep leetcode')
lines = stream.readlines()

things_to_write = []
for line in lines:
    line = line.strip()

    # Matches kattis_xxxx.py or kattis_xxxx.cpp or kattis_xxxx.hs
    m = re.search(r'\/.*leetcode_(\w*)\.(?:py|cpp|hs|c)', line)

    if m:
        things_to_write.append([str(m.group(1)), "https://github.com/WindJammer6/14.-My-Leetcode-Solutions/blob/main" +
                                line[1:], "https://leetcode.com/problems/" + str(m.group(1))])
    
def print_table():
    things_to_write.sort()
    solution_types = []
    for index, (q_name, sol, task) in enumerate(things_to_write):
        for k, v in file_types_dictionary.items():
            if (sol.endswith(v)):
                solution_types.append((k, sol))
                break
        
        if (index != len(things_to_write) - 1):
            if (things_to_write[index+1][2] == task):
                continue
        
        line = f"| {index+1} | [{q_name}]({task}) | "
        for solution_type, solution in solution_types:
            line += f"[{solution_type}]({solution}), " 
        
        line = line[:-2] + " |"
        print(line)
        
        solution_types.clear()
print_table()
