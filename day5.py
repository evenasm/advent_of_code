import os
import re

def get_lines(vent_line):
    x1 = vent_line[0]
    x2 = vent_line[2]
    y1 = vent_line[1]
    y2 = vent_line[3]
    if x1 == x2:
        if y2 > y1:
            y = y1 
        else:
            y = y2
        return [(x1, y + i) for i in range(abs(y1 - y2) +1)]
    elif y1 == y2:
        x = x2  if x2 < x1 else  x1
        return [(x+i, y1) for i in range(abs(x2-x1) +1)]
    else:
        iterations = abs(x1 - x2)
        x_step = (x2-x1) /iterations
        y_step = (y2-y1) / iterations
        #print(x_step, y_step)
        return [(int(x1 + x_step*i ),int( y1 + y_step*i)) for i in range(iterations+1)]


with open(os.path.join('inputs', 'day5.txt')) as file:
    vents = []
    for line in file:
        split_line = line.strip().replace('->', '')
        split_list = re.split('[, ]', split_line)
        vents.append([int(item.strip()) for item in split_list if item != ''])
    #print(vents)
    array = [[0 for i in range(1000)] for j in range(1000)] 
    for line in vents:
        for vent in get_lines(line):
            #print(vent)
            array[vent[0]][vent[1]] += 1
    sum = 0
    for row in array:
        for item in row:
            if item >= 2:
                sum += 1
    print(sum)