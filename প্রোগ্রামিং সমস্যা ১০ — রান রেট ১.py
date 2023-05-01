tCase = int(input())  # take test case limit

while tCase:
    opRun, myRun, leftBall = map(int, input().split())
    playedOver = (300 - leftBall) / 6
    cRunRate = myRun / playedOver
    rRunRate = ((opRun + 1 - myRun) / leftBall) * 6
    if rRunRate < 0:
        rRunRate = 0
    print("%.2f %.2f" % (cRunRate, rRunRate))
    tCase -= 1