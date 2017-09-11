#接受一个数字

List = [0, 1]

for i in range(20):
    if i == 0:
        print(0)
    if i == 1:
        print(1)
    else:
        temp = List[i] + List[i - 1]
        print(temp)
        List.append(temp)
