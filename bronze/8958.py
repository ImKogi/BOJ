T = int(input())

for _ in range(T):
    ox = input()
    score = {"O":0,
             "X":0}
    k=0
    for a in list(ox):
        if a == "O":
            score[a] = score.get(a, 0) +k+1
            k+=1
        else:
            k=0
    print(score.get("O",0))