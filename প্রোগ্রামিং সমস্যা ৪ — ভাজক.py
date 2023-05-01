from math import ceil, sqrt
tCase = int(input())

for test in range(tCase):
    userInput = int(input())
    div = []
    for i in range(1, int(sqrt(userInput) + 1)):
        if userInput % i == 0:
            if userInput // i == i:
                div.append(i)
            else:
                div.extend([userInput//i, i])
    print("Case %i:"%(test+1), *sorted(div))