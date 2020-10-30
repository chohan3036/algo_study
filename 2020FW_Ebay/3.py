from itertools import combinations_with_replacement
from copy import deepcopy


def solution(n, products):
    # 중복조합을 사용해 이벤트 케이스 생성
    event = combinations_with_replacement([i for i in range(n)], n)

    # 모든 매출 케이스를 담을 배열
    sales = []

    for e in event:
        # 이벤트 케이스마다 목록과 매출 갱신
        cur_products = deepcopy(products)
        cur_sales = 0

        # 각 날짜별로 상품목록을 순회하며 매출 계산
        for i in range(n):
            for j in range(n):

                # 이벤트 매대에 올릴 상품이면
                if e[i] == j:
                    # 이벤트 품목에 대해
                    # 재고량 확인한 뒤, 재고 충분하면 그만큼 판매하고 매출 올림
                    if cur_products[j][0] >= cur_products[j][2] * 2:
                        cur_sales += cur_products[j][1] * cur_products[j][2] * 2
                        cur_products[j][0] -= cur_products[j][2] * 2

                    # 재고 부족하면 재고만큼만 판매
                    else:
                        cur_sales += cur_products[j][1] * cur_products[j][0]
                        cur_products[j][0] = 0

                # 일반 상품이면
                else:
                    # 재고량 확인한 뒤, 재고 충분하면 그만큼 판매하고 매출 올림
                    if cur_products[j][0] >= cur_products[j][2]:
                        cur_sales += cur_products[j][1] * cur_products[j][2]
                        cur_products[j][0] -= cur_products[j][2]

                    # 재고 부족하면 재고만큼만 판매
                    else:
                        cur_sales += cur_products[j][1] * cur_products[j][0]
                        cur_products[j][0] = 0

        sales.append(cur_sales)

    return max(sales)


print(solution(3, [[6, 5, 1], [11, 3, 2], [7, 10, 3]]))
