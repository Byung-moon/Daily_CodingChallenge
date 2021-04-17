# # case 1 - Time Over
# import sys

# integer_num = int(input())

# array = []

# for i in range(integer_num):
#     array.append(input())

# for i in range(0,len(array)): 
#     minValue = min(array)   
#     sys.stdout.write(minValue + '\n')
#     array.remove(minValue)
    

# case 2 - Python3 : Time Over (Counting sort)
#        - PyPy3 : Pass 
import sys
integer_num = int(input())

array_1 = [0 for i in range(1000001)]
array_2 = [0 for i in range(1000001)]

# minusNum = 0
# plusNum = 0
for y in range(integer_num):
    tmp = int(input())
    if tmp < 0:
        array_2[-tmp] = 1
        # minusNum += 1 
    else: 
        array_1[tmp] = 1
        # plusNum += 1

for y in range(len(array_2)-1, 0, -1):
    if array_2[y] != 0:
        sys.stdout.write(str(-y) + '\n')

for x in range(0, len(array_1)):
    if array_1[x] != 0:
        sys.stdout.write(str(x) + '\n')

