import sys

N = int(sys.stdin.readline())
S = [[i for i in list(map(int, sys.stdin.readline().strip().split()))] for _ in range(N)]
members = [0 for _ in range(N)]
diff = 4000

def team(members, start, count):
    if count == N/2:
        val1, val2 = 0, 0
        for i in range(N):
            for j in range(N):
                if i != j and i < j:
                    if members[i] == 0 and members[j] == 0:
                        val1 += S[i][j]+S[j][i]
                    elif members[i] == 1 and members[j] == 1:
                        val2 += S[i][j]+S[j][i]
        global diff
        if abs(val1-val2) < diff:
            diff = abs(val1-val2)
    else:
        for i in range(start+1, N):
            if members[i] != 1:
                members[i] = 1
                team(members, i, count+1)
                members[i] = 0

team(members, 0, 0)
print(diff)