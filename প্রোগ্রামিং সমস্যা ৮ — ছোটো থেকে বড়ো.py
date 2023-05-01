def selecttionSort(arr):
    for min in range(len(arr)):
        minIndex = min
        for find in range(min + 1, len(arr)):
            if arr[find] < arr[minIndex]:
                minIndex = find
        if arr[min] > arr[minIndex]:
            arr[min], arr[minIndex] = arr[minIndex], arr[min]
    return arr


tCase = int(input())  # test case limit
counter = 1
while tCase:
    userInput = selecttionSort(list(map(int, input().split())))  # take input as list and pass as argument
    print("Case %i:"% counter, *userInput)
    tCase -= 1
    counter += 1