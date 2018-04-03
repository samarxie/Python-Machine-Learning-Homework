def output(m, j, x, nums, hashnum):
    for i in range(j, m):
        if(i in hashnum):
            continue
        else:
            hashnum.append(i)
            if(x > 1):
                output(m, i + 1, x - 1, nums, hashnum)
            else:
                print(" ".join(str(nums[x]) for x in hashnum))
            hashnum.pop()
    return

m = input().split(" ")
m = [int(x) for x in m]
n = int(m[1])
m = int(m[0])
nums = input().split(" ")
nums = [int(x) for x in nums]

output(m, 0, n, nums, [])