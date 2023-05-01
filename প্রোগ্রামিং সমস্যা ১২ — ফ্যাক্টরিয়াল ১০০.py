def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
TestCase = int(input())
for i in range(TestCase):
    UserData = int(input())
    Temp = str(factorial(UserData))
    TempList=' '.join(Temp).split()
    Counter = 0
    for i in range(len(TempList)-1,-1,-1):
        if TempList[i] == '0':
            Counter += 1
        else:
            break
    print(Counter)