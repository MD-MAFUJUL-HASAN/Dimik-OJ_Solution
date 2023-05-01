mx = 1000
counter = 0
d = []
while mx:
    print(mx, end='\t')
    counter += 1
    if counter == 5:
        counter = 0
        print()
    mx -= 1