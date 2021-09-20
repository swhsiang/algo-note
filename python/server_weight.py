#!/usr/bin/python3

"""
Question: DocuSign has different sized servers that process documents in its data centers. To load balance jobs across the
servers, each job is assigned to a random server such that if server X is three times as big as server Y, then server
X gets assigned three times as often as server Y. So server X would be assigned approximately 75% of the time and
server Y would be assigned 25% of the time.

Write a program in any programming language that takes server names and sizes as arguments and outputs the
name of a random server based on the algorithm described above. For instance:

$ program X:3 Y:1
X


------
Uncomment the code if you want to test the program.
change the value of REMAINING_TEST variable to determine the number of tests you would like to run

How to run the code:

python server_weight.py X:4 Y:1

or
chmod +x server_weight.py 
./server_weight.py X:4 Y:1


Binary search approach
Runtime complexity: O(lg N), N is the number of servers

Three steps to tackle the problem:
1. parse the command line arguments (servers and weights)
2. init variables
3. In order to achieve memory efficiency, we generate a list of cumulative sum (integer) to represent the weights of severs.
Use binary search to find the smallest element which is just bigger than the randomly chosen number (goal).

"""

# program X:3 Y:1

import random
import sys

# parse input arguments 
input_args = sys.argv[1:]
pairs = {}
task_arr = []
weight_arr = []

for i in input_args:
    line = i.split(':')
    pairs[line[0]] = line[1]

    weight_arr.append(int(line[1]))
    task_arr.append(line[0])

# NOTE temp array for testing purpose
# t_arr = []

def run():
    # init variables
    temp_sum = 0
    sum_arr = []

    for weight in weight_arr:
        temp_sum += weight
        sum_arr.append(temp_sum)
    sum_all = temp_sum

    # binary search
    goal = random.random() * sum_all

    right = len(sum_arr)
    left = 0

    while left < right:
        mid = left + (right - left) // 2
        if goal > sum_arr[mid]:
            left = mid + 1
        else:
            right = mid

    sys.stdout.write(f'{task_arr[left]}\n')

    # NOTE array for testing case
    # t_arr.append(left)

run()

# REMAINING_TEST = 999
# from collections import defaultdict
# temp_dict = defaultdict(int)
# for _ in range(REMAINING_TEST):
#     run()

# for g in t_arr:
#     temp_dict[task_arr[g]] += 1 

# print(temp_dict)