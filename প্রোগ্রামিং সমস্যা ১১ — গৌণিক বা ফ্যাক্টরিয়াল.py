def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


tCase = int(input())  # take testcaase limit

while tCase:
    facNum = factorial(int(input()))  # take number and pass as argument.
    print(facNum)
    tCase -= 1  # decrease by 1