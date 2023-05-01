tCase = int(input())

while tCase:
    n, m = map(int, input().split())
    values = []
    for i in range(1, n+1):
        strVal = " ".join(list(str(m) * i))
        values.append(strVal)
    deepCopy = values[0:-1]
    deepCopy.reverse()
    values.extend(deepCopy)
    print(*values, sep="\n")
    print()
    tCase -= 1