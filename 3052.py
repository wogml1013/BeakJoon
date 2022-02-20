list1 = []
for i in range(10):
    list1.append(int(input()))

for j in range(len(list1)):
    list1[j] = list1[j] % 42

S = set(list1)

print(S)
print(len(S))