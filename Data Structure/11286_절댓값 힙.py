import sys
N = int(sys.stdin.readline())
hip = []
for i in range(N):
    cin = int(sys.stdin.readline())
    if cin == 0:
        print(hip.pop(0))
    else:
        if not hip:
            hip.append(cin)
            print(hip)
        else:
            print(cin, len(hip))
            for j in range(len(hip)):
                if cin < 0:
                    if cin*-1 <= hip[j]:
                        hip.insert(cin*-1,j-1)
                        print(hip)
                        break
                else:
                    if cin <= hip[j]:
                        hip.insert(cin, j+1)
                        print(hip)
                        break