s = "abcabcabcabcdededededede"
len_s = len(s)
len_list = []
for i in range(1, len_s):
    tmp_list = []
    for j in range(0, len_s, i):
        tmp_list.append(s[j: j + i])

    tmp_len = [1 for _ in range(len(tmp_list))]
    for k in range(len(tmp_list) - 1):
        if tmp_list[k] == tmp_list[k + 1]:
            tmp_len[k] += 1

    tmp_str = ''
    idx = 0
    while 1:
        if idx > len(tmp_list) - 1:
            break
        if tmp_len[idx] > 1:
            tmp_str += str(tmp_len[idx]) + str(tmp_list[idx])
            idx += tmp_len[idx]
        else:
            tmp_str += str(tmp_list[idx])
            idx += 1
    print(tmp_str)

    len_list.append(len(tmp_str))

print(min(len_list))
