from pyrsistent import b


H, M = map(int, input().split())
T = int(input())

B = M + T
if B < 60:
    pass

elif B >= 60:
    H = H + B//60
    B = B%60
    if H > 23:
        H = H%24

print(H, B)
