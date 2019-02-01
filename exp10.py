Numbers = int(input())
Count = 0
while(Numbers > 0):
    Numbers = Numbers // 10
    Count = Count + 1

print(Count)
