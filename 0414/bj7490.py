import copy

caseNum = int(input())

# find All of Operator Combinations
def GetOperatorArray(array, N):
    if len(array) == N:
        OperatorArray.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    GetOperatorArray(array, N)
    array.pop()

    array.append('+')
    GetOperatorArray(array, N)
    array.pop()

    array.append('-')
    GetOperatorArray(array, N)
    array.pop()

for x in range(caseNum):
    N = int(input())
    array = []
    OperatorArray = []
    GetOperatorArray(array, N-1)

    #find integers list
    number_list = list(y for y in range(1, N+1))

    # operating strings
    for operators in OperatorArray:
        string = ""
        for z in range(N-1):
            string = string + str(number_list[z]) + operators[z]
        string += (str(number_list[-1]))

        if eval(string.replace(" ", "")) == 0:
            print(string)
    
    print()

    