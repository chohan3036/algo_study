N = int(input())
A = list(map(int, input().split(' ')))
M = int(input())
num = list(map(int, input().split(' ')))

A.sort()

def bin_search(n, start, end):
    mid = (start+end)//2
    if start > end:
        return 0
    if num[i] == A[mid]:
        return 1
    elif num[i] < A[mid]:
        return bin_search(n, start, mid-1)
    elif num[i] > A[mid]:
        return bin_search(n, mid+1, end)

for i in range(M):
    print(bin_search(num[i],0,len(A)-1))