tCase = int(input())  # take test case limit

while tCase:
    userInput = int(input())  # takse user input
    if int(userInput ** .5) ** 2 == userInput:
        print("YES")
    else:
        print("NO")
    tCase -= 1  # decrement by 1