#prob 1568 from https://www.acmicpc.net/problem/1568

Birds= int(input())
cntTime = 0

while(Birds > 0):
    for Sing in range(1, Birds+1):
        # print("%d %d %d" %(Birds, Sing, Birds-Sing))
        if Birds < Sing:
            break
        else:
            Birds -= Sing
            cntTime += 1
        
print(cntTime)    