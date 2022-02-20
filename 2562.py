list1 = []
for j in range(9):
    list1.append(int(input()))

Max = list1[0]
index = 0
for i in range(len(list1)):
    if list1[i] >= Max:
        Max = list1[i]
        index = i
print(Max)
print(index+1)
    