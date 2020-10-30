## 백트랙킹 - 연산자 끼워넣기
import sys

num = int(input())
num_list = list(map(int, input().split(' ')))
print(num_list)
op_list = list(map(int, input().split(' ')))
print(op_list)

if (num - 1) != sum(op_list): # 예외 처리,,
    sys.exit()