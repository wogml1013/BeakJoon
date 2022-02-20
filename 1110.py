N = int(input())
M = N
K = -1
Try = 0

while K != N:
    Try += 1
    K = M % 10 * 10 + (M // 10 + M % 10) % 10
    M = K

print(Try)