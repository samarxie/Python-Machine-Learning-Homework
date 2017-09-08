n = input().split(" ")
n = [int(x) for x in n]
m = n[1]
n = n[0]
w = input().split(" ")
w = [int(x) for x in w]
time = [w[x] for x in range(m)]
t = m
while(t < n):
    time[time.index(min(time))] += w[t]
    t += 1
print(max(time))  