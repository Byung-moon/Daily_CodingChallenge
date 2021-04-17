# prob 11004 from https://www.acmicpc.net/problem/11004

num, K = map(int,input().split(" "))

array = []

array = map(int, input().split(' '))

array = sorted(array)

print(array[K - 1])