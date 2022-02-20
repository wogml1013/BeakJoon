N = int(input())
for i in range(N):
    A = input()
    score = 0
    Fscore = 0
    for j in A:
        if j == 'O':
            score += 1
            Fscore += score
        if j == 'X':
            score = 0
    print(Fscore)