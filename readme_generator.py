# Prints out a README.md file for the project
import re, os
start_of_readme = '''# Competitive Programming 4 Solutions
My solutions to some of the [Kattis](https://open.kattis.com/) problems listed in [Competitive Programming 4](https://cpbook.net/details?cp=4).
Some [UVA Online Judge](https://onlinejudge.org/) problems are also solved on [Virtual Judge](https://vjudge.net/).

The C++ code is written to be compiled using with gcc version 11.2.0 (Ubuntu 11.2.0-19ubuntu1)
<pre>g++ -std=c++17 kattis_xxx.cpp -o kattis_xxx && kattis_xxx</pre>

Python code is executed using Python 3.10.4 on my machine but will work on the 3.6 of Kattis
<pre>/bin/python3 kattis_xxx.py</pre>

## Documentation
| Category | Description |
|----------|-------------|
| Observation | A key insight into the question or our currently considered method that might be needed to come up with a correct algorithm or improve the efficiency of an algorithm. |
| Idea | A new approach to the problem. Could include viewing the problem from a different angle. |
| Debugging | Descriptions of bugs that one could encounter, possibly including edge cases. |
| Optimisations | Other micro-optimisations that are not important enough to be considered ideas or observations. |
| Design | A way we implement an idea in code to keep the code simple and easy to write. |
| Time & Space Complexity | My analysis of the algorithmic order of growth |

# List of Kattis Questions Solved
![Auto Update](https://github.com/BrandonTang89/Competitive_Programming_4_Solutions/actions/workflows/Update_README.yml/badge.svg)
| Index | Question Title | Solution |
| ----- | -------------- | -------- |'''

print(start_of_readme)
m_file_types = {'C++': 'cpp', 'Python': 'py', 'Haskell': 'hs', 'C': 'c'}

# Get the Kattis Solutions
stream = os.popen('find | grep kattis')
lines = stream.readlines()

things_to_write = []
for line in lines:
    line = line.strip()

    # Matches kattis_xxxx.py or kattis_xxxx.cpp or kattis_xxxx.hs
    m = re.search(r'\/kattis_(\w*)\.(?:py|cpp|hs|c)', line)

    # First capturing group is the problem name
    things_to_write.append([str(m.group(1)), "https://github.com/BrandonTang89/Competitive_Programming_4_Solutions/blob/main" +
                            line[1:], "https://open.kattis.com/problems/" + str(m.group(1))])
    

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


things_to_write.clear()
stream = os.popen('find | grep vjudge')
lines = stream.readlines()
for line in lines:
    line = line.strip()

    # Matches vjudge_xxxx_someothername.someext where the someothername is optional
    m = re.search(r'\/vjudge_([^_]*)(?:.*).(?:py|cpp|hs)', line)

    # First capturing group is the problem name
    things_to_write.append([str(m.group(1)), "https://github.com/BrandonTang89/Competitive_Programming_4_Solutions/blob/main" +
                            line[1:], "https://vjudge.net/problem/" + str(m.group(1))])
print('''# List of Virtual Judge Questions Solved
| Index | Question Title | Solution |
| ----- | -------------- | -------- |''')

print_table()
