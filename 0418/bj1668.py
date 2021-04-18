# prob 1668 from https://www.acmicpc.net/problem/1668

# # case1 - Fail
# N = int(input())
# array = []

# # value array
# for x in range(N):
#     array.append(int(input()))

# top = max(array)
# top_index = array.index(top) + 1
# # print(top)

# print(top_index) #print left side

# for x in range(len(array)-1, -1, -1):
#     if top == array[x]:
#         top_index = x
#         # print('max index = %d' %top_index)
#         break

# top_index = top_index + 1
# print(len(array) - top_index + 1)

#case2 
N = int(input())
array = []

for x in range(N):
    array.append(int(input()))

cnt_Num = 0
cnt_height = 0

# counting on left side
for y in range(len(array)):
    if y == 0:
        starting_height = array[0]
        cnt_Num += 1

    if array[y] > starting_height:
        starting_height = array[y] 
        cnt_Num += 1
    
print(cnt_Num)

# counting on right side
cnt_Num = 0
cnt_height = 0


for z in range(len(array)-1, -1, -1):
    if z == len(array) - 1:
        starting_height = array[z]
        cnt_Num += 1

    if array[z] > starting_height:
        starting_height = array[z] 
        cnt_Num += 1

print(cnt_Num)