num = int(input())
length = input().split(" ")
length = [int(x) for x in length]

total = 0
for i in range(num - 1):
    total += abs(length[i + 1] - length[i])
min = total
for i in range(1, num - 1):
    temp_length = total - abs(length[i - 1] - length[i]) - abs(length[i + 1] - length[i]) + abs(length[i + 1] - length[i - 1])
    if(temp_length < min):
        min = temp_length
print(min)