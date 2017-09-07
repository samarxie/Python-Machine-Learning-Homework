def output(n, m, k, x, j, nums, hashnum, maxnum):
    if(j + k < n):
        for i in range(j, j + k):
            if(i in hashnum):
                continue
            else:
                hashnum.append(i)
                if(x > 1):
                   maxnum = output(n, m, k, x - 1, i + 1, nums, hashnum, maxnum)
                else:
                    temp = 1
                    for t in range(m):
                        temp *= nums[hashnum[t]]
                    if(temp > maxnum):
                        maxnum = temp
                hashnum.pop()
    else:
        for i in range(j, n):
            if(i in hashnum):
                continue
            else:
                hashnum.append(i)
                if(x > 1):
                    maxnum = output(n, m, k, x - 1, i + 1, nums, hashnum, maxnum)
                else:
                    temp = 1
                    for t in range(m):
                        temp *= nums[hashnum[t]]
                    if(temp > maxnum):
                        maxnum = temp
                hashnum.pop()
    return maxnum

n = input().split(" ")
n = [int(x) for x in n]
m = int(n[1])
k = int(n[2])
n = int(n[0])
nums = input().split(" ")
nums = [int(x) for x in nums]

maxnum = output(n, m, k, m, 0, nums, [], 0)
print(maxnum)