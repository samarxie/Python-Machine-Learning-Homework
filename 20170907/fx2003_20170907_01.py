import numpy as np
import sys
n = int(input())
matrix = []
for i in range(2):
    line = input().split(" ")
    line = [int(x) for x in line]
    matrix.append(line)
res = np.linalg.det(matrix)
print("%.2f" % res)