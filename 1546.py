N = int(input())
score = list(map(int, input().split()))

M = max(score)

aver = 0

for i in score:
    aver += i/M*100
print(aver/N)