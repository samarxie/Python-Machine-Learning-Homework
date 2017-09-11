m = int(input())
people = [int(x) for x in range(1, 101)]
now = 100
t = 0
while(now >= m):
    now = now - 1
    t = (t + m - 1) % len(people)
    del people[t]
print(" ".join(str(x) for x in people))