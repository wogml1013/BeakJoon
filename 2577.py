A = int(input())
B = int(input())
C = int(input())

N = str(A*B*C)

list1 = []
for i in range(10):
    list1.append(N.count(str(i)))

for j in list1:
    print(j)

