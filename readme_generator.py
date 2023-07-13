# Prints out a README.md file for the project
import re, os
start_of_readme = '''# 14.-My-Leetcode-Solutions :dart:
Here are some of my accepted attempts at some Leetcode questions.

My Leetcode account: https://leetcode.com/WindJammer6/

<ins>Disclaimer</ins>: I am a student programmer, these solutions that I have attached in this repository are not perfect answers to the Leetcode questions (in terms of design 
and Time and Space Big O Notation Complexity), but are just merely my sharing of my own approach to the questions (in terms of design and Time and Space Big O Notation Complexity).
They do answer the Leetcode questions, but there are definitely better answer codes out there. '''

print(start_of_readme)
m_file_types = {'C++': 'cpp', 'Python': 'py', 'Haskell': 'hs', 'C': 'c'}

# Get the Kattis Solutions
stream = os.popen('find | grep Leetcode')
lines = stream.readlines()

things_to_write = []
for line in lines:
    line = line.strip()

    # Matches kattis_xxxx.py or kattis_xxxx.cpp or kattis_xxxx.hs
    m = re.search(r'\/Leetcode_(\w*)\.(?:py|cpp|hs|c)', line)

    # First capturing group is the problem name
    things_to_write.append([str(m.group(1)), "https://github.com/WindJammer6/14.-My-Leetcode-Solutions/blob/main/" + line[1:]])
    

def print_table():
    things_to_write.sort()
    solution_types = []
    for index, (q_name, sol, task) in enumerate(things_to_write):
        for k, v in m_file_types.items():
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


print('''# List of Virtual Judge Questions Solved
| Index | Question Title | Solution |
| ----- | -------------- | -------- |''')

print_table()