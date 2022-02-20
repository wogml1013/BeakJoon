C = int(input())

for i in range(C):
    list1 = list(map(int, input().split()))
    N = list1.pop(0)
    Average = sum(list1)/N
    s = 0
    for j in list1:
        if j > Average:
            s += 1
    print("{:.3f}%".format(s/N*100))
