# prob 1543 from https://www.acmicpc.net/problem/1543

originWords = input()
word = input()

cnt = 0
index = 0
# for x in range(0, len(originWords)-len(word) + 1):
while(index < len(originWords) - len(word) + 1):
    if word == originWords[index : index + len(word)]:
        cnt += 1
        index += len(word)
        # originWords.remove(word)
    else:
        index += 1
    # print(index)

print(cnt)

