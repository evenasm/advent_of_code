file = open('day3.txt')
first_line = file.readline()
sum_array = [int(num) for num in first_line.strip()]

def add_arrays(a1, a2):
    if len(a1) != len(a2):
        return False
    else:
        for i in range(len(a2)):
            a1[i] += a2[i]
        return True
file_length = 1
for line in file:
    file_length +=1
    if add_arrays(sum_array, [int(num) for num in line.strip()]) == False:
        print("abort mission")
        exit()
    #print(sum_array)

gamma_rate = 0
epsilon_rate = 0
len_array = len(sum_array)

def translate_bin_array_to_decimal(sum_array):
    binary_number = sum_array[0]
    length = len(binary_number)
    decimal = 0
    for i in range(length):
        if int(binary_number[i]) != 0: decimal += pow(2,length-1-i)
    return decimal

for i in range(len_array):
    if sum_array[i] - file_length/2 > 0:
        gamma_rate += pow(2,len_array -i -1)
    else:
        epsilon_rate += pow(2,len_array -i -1)

with open('day3.txt') as file:
    numbers = [line.strip() for line in file]

def most_common(array, index):
    sum_i = 0
    for item in array:
        sum_i+= int(item[index])
    if sum_i - len(array) / 2.0 >=0:
        return '1'
    return '0'

def least_common(array, index):
    sum_i = 0
    for item in array:
        sum_i+= int(item[index])
    if sum_i - len(array) / 2.0 <0:
        return '1'
    return '0'

def determine_bit_criteria(i, oxygen_array, co2_array):

    print(len(oxygen_array), len(co2_array))
    if len(oxygen_array) > 1 : oxygen_array = [line for line in oxygen_array if line[i] == most_common(oxygen_array, i)]
    print(oxygen_array)
    if len(co2_array) > 1 : co2_array = [line for line in co2_array if line[i] == least_common(co2_array, i)]
    print(co2_array)
    return oxygen_array, co2_array


oxygen_array = numbers
co2_array = numbers
bit_index = 0
while len(oxygen_array) + len(co2_array) > 2:
    oxygen_array, co2_array = determine_bit_criteria(bit_index,  oxygen_array, co2_array)
    bit_index +=1
print(oxygen_array, co2_array)
    
print(file_length)
print(gamma_rate*epsilon_rate)
print(translate_bin_array_to_decimal(oxygen_array)*translate_bin_array_to_decimal(co2_array))