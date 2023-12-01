import fileinput
import re

answer = 0

with fileinput.input(files=('/Users/phillipcarman/projects/AOC2023/day01/input1.txt')) as f:
    for line in f:
        mysample = re.findall(r'\d+', line)       
        test0 = ("".join(mysample))    
        test1 = (test0[0],test0[-1])
        myjoin = ''.join(test1)
        answer += int(myjoin)                   

print(answer)
