tCase = int(input())

while tCase:
    userInput = int(input())
    if userInput & 1:
        print("odd")
    else:
        print("even")
    tCase -= 1