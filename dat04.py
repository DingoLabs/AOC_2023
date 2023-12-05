import fileinput

answer = 0

with fileinput.input(files=('/Users/phillipcarman/projects/AOC2023/day04/input.txt')) as f:
    for line in f:
        matched_nums = 0
        my_nums = []
        win_nums = []
        x = line.split()
        score = 0

        # add numbers to my nums
        for i in range (1,11):
            my_nums.append(x[i+1])
        #print(my_nums)
        
        # add numbers to winning nums
        for i in range(1,26):
            win_nums.append(x[i+12])
        #print(win_nums)
        
        #check if win nums against my num
        for i in win_nums:
                if i in my_nums:
                    matched_nums += 1
        

        
        #calculate score                
        for i in range(matched_nums):
            if score == 0:
                score = 1
            else:
                score *= 2
        answer += score

        
        print(f" matched nums is {matched_nums}")
        print(f" current total is {answer}")
print(f" final score is {answer}")
