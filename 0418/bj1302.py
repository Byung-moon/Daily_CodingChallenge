# prob 1302 from https://www.acmicpc.net/problem/1302

# if 'top' > 'toz':
#     print('top')
# else:
#     print('toz')

# dic = {'top':4, 'kimtop':2}

# if 'toz' in dic:
#     print(dic['top'])
# else:
#     print('fault')

N = int(input())

dic = {}
tilteList = []
for x in range(N):
    tmp = input()
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
        tilteList.append(tmp)

# print(tilteList)
# print(dic)

maxTitle = ''
for y in range(len(tilteList)):
    if y==0:
        maxTitle = tilteList[y]
    else:
        tmp1 = tilteList[y-1]
        tmp2 = tilteList[y]
        num1 = dic[maxTitle]
        num2 = dic[tmp2]

        if (num1 < num2):
            maxTitle = tmp2

        elif num1 == num2:
            if maxTitle > tilteList[y]:
                maxTitle = tilteList[y]
            # else: 
            #     maxTitle = tilteList[y-1]
    # print(maxTitle)

print(maxTitle)
