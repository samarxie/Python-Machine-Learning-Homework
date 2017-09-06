from math import sqrt

def isPrime(x):
    if(x == 2):
        return True
    else:
        for i in range(2, int(sqrt(x)) + 1):
            if(x % i == 0):
                return False
    return True

num = int(input())
res = []
for i in range(2, num):
    if(isPrime(i)):
        res.append(i)
print(" ".join(str(x) for x in res))