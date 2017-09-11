# 任意输入N个数

List = [1, -1, 4, 3,5, 8]
length = len(List)
summ = 0
for i in range(length - 1):
    summ += abs(List[i + 1] - List[i])

Temp = []
for i in range(length - 2):
    temp_distance = summ - abs(List[i + 1] - List[i]) - abs(List[i + 2] - List[i + 1 ]) + abs(List[i + 2] - List[i])
    Temp.append(temp_distance)

print(min(Temp))
