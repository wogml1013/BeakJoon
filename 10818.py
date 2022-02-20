N = int(input())
list1 = list(map(int, input().split()))
min = list1[0]
MAX = list1[0]
for i in list1:
    if i <= min:
        min = i
    elif i >= MAX:
        MAX = i
print(min, MAX)
    