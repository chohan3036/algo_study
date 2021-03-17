from collections import Counter


def solution(dataSources, tags):
    db = dict()
    for data in dataSources:
        cur_doc = int(data[0][3:])
        for tag in data[1:]:
            tag_num = int(tag[1:])
            if tag_num not in db:
                db[tag_num] = []
            if cur_doc not in db[tag_num]:
                db[tag_num].append(cur_doc)

    result = []
    for tag in tags:
        tag_num = int(tag[1:])
        for doc in db[tag_num]:
            result.append(doc)

    ans = []
    for doc, cnt in sorted(Counter(result).items(), key=lambda x: (-x[1], x[0])):
        doc_str = 'doc' + str(doc)
        ans.append(doc_str)

    return ans


print(solution([["doc1", "t1", "t2", "t3"],
                ['doc11', 't0', 't2', 't3'],
                ['doc3', 't1', 't6', 't7'],
                ['doc4', 't1', 't2', 't4'],
                ['doc5', 't6', 't100', 't8']],
               ['t1', 't2', 't3']))
