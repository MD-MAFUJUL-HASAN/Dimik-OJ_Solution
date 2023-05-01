case = int(input())

for i in range(case):
    userInput = int(input())
    for j in range(userInput):
        print('*' * userInput)
    if i < case - 1:
        print()