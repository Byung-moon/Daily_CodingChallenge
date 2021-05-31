N = int(input())   
a = list(map(int, input().split()))
M = int(input())   
b = list(map(int, input().split()))

def FindEnd(cnt):   # cnt : target index
    # print('Hi')
    while(True):
        if cnt == len(a)-1:
            return cnt
        elif a[cnt] != a[cnt+1]:
            # print('Hi', cnt)
            return cnt 
        else:
            cnt += 1

def FindStart(cnt):
    # print('Hello')
    while(True):
        if cnt == 0:
            return 0
        elif a[cnt] != a[cnt-1]:
            # print('Hello', cnt)
            return cnt
        else:
            cnt -= 1

for x in range(0, M):
    start = 0
    end = len(a)-1
    # cnt = 0
    
    while(True):
        mid = (int)((start + end) / 2)
        if start > end:
            print(0, end=' ')
            break
        
        if a[mid] == b[x]:
            print(FindEnd(mid) - FindStart(mid) + 1, end=' ')
            break
        elif a[mid] > b[x]:
            end = mid-1
        else:
            start = mid+1
        # cnt += 1
        # print(cnt)