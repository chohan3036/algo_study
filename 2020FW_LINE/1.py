from collections import Counter


def solution(boxes):
    box_cnt = len(boxes)

    # 상자를 풀어서 상품을 하나씩 담기
    unpacked_boxes = []
    for box in boxes:
        unpacked_boxes.append(box[0])
        unpacked_boxes.append(box[1])

    # 각 상품의 개수를 카운터를 사용해 저장
    goods_cnt = Counter(unpacked_boxes)

    # 그 결과를 순회하며, 상품 개수가 짝수이면 box 에 짝지어 포장, box 개수 소모
    # 그럴 수 없을 경우는 box 소모하지 않음
    for goods in goods_cnt.items():
        if goods[1] % 2 == 0:
            box_cnt -= goods[1] // 2

    return box_cnt


print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8],
                [5, 6], [5, 8], [7, 8], [8, 9]]))
