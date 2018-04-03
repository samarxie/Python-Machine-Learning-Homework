num = int(input())
res = []
for i in range(num):
    if(i <= 1):
        res.append(i)
    else:
        res.append(res[i - 1] + res[i - 2])
print(" ".join(str(x) for x in res))