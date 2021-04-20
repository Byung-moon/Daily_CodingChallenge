#prob.1236 from https://www.acmicpc.net/problem/1236
N, M = map(int, input().split(" "))

array = []

for x in range(N):
    array.append(input())

# Row Search
NeedRow = len(array)
for x in range(len(array)):
    for y in range(len(array[0])):
        if array[x][y] == 'X':
            NeedRow -= 1
            break
# Column Search
NeedColumn = len(array[0])
for x in range(len(array[0])):
    for y in range(len(array)):
        if array[y][x] == 'X':
            NeedColumn -= 1
            break

# print('NeedRow : %d' %NeedRow)
# print('NeedColumn : %d' %NeedColumn)

# print answer
if (NeedRow >= NeedColumn):
    print(NeedRow)
else:
    print(NeedColumn)
