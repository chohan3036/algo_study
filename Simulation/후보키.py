from itertools import combinations


def solution(relation):
    col_len = len(relation[0])
    attribute_index = range(col_len)
    check_list = []
    # 유일성 검사
    for num in range(1, col_len+1):
        comb_attribute = combinations(attribute_index, num)
        for check_comb in list(comb_attribute):
            all_attr_list = [tuple(item[index] for index in check_comb) for item in relation]
            if len(set(all_attr_list)) != len(relation):
                continue
            else:
                check_list.append(set(check_comb))
    # 최소성 검사
    for item1 in check_list[:]:
        for item2 in check_list[:]:
            if item1 != item2:
                if item1 == item1 & item2:
                    check_list.remove(item2)
    return len(check_list)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))

'''
def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)
'''