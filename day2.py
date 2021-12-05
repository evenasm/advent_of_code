file = open("day2.txt")
dictionary = {
    'forward' : 0,
    'backward' :0,
    'down' : 0,
    'up' : 0
} 
depth = 0
aim = 0
for line in file:
    line = line.strip()
    arr = line.split(" ")

    codeword = arr[0]

    if codeword == 'forward':
        dictionary['forward'] += int(arr[1])
        depth += aim*int(arr[1])
    elif codeword == 'backward':
            dictionary['backward'] -= int(arr[1])
    elif codeword == 'down':
        aim += int(arr[1])
    elif codeword == 'up':
        aim -= int(arr[1])
    #dictionary[arr[0]] += int(arr[1])
horizontal_pos = dictionary['forward'] -  dictionary['backward']
# vertical_pos = dictionary['down'] - dictionary['up']
print(horizontal_pos*depth)