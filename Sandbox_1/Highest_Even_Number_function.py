def Highest_Even(Num):
    Evens = []
    for i in Num:
        if i % 2 == 0:
            Evens.append(i)
    return max(Evens)

print(Highest_Even([4,3,5,6,7,11,12,25,24,30,31,38,39,40]))

