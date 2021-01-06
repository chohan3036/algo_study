import datetime as dt
'''
꽃 자판기
1. 품목별로 가격, 수량, 꽃말, 설명, 유통기한
2.
'''


# 꽃 객체를 class 로 구현
class Flower(object):
    def __init__(self, name, lang, doc):
        # 이름
        self.name = name
        # 꽃말
        self.lang = lang
        # 설명
        self.doc = doc
        # 유통기한 (당일로부터 15일)
        self.exdate = dt.datetime.today() + dt.timedelta(days=15)


# 꽃 초기화
rose = Flower('장미', '열렬한 사랑', '')
chrysanthemum = Flower('국화', '짝사랑', '')
hyacinth = Flower('히아신스', '겸손한 사랑', '')
tulip = Flower('튤립', '사랑의 고백', '')
daisy = Flower('데이지', '희망과 평화', '')
carnation = Flower('카네이션', '영원한 사랑', '')
iris = Flower('붓꽃', '좋은 소식', '')
sun = Flower('해바라기', '프라이드', '')
gypsophila = Flower('안개꽃', '깨끗한 마음', '')

print('------------------------------------')
print('----\t{0}\t\t국화\t\t히아신스\t----'.format(rose.name))
print('----\t ⬛ \t\t ⬜ \t\t   ⬛ \t----')
print('------------------------------------')
print('----\t튤립\t\t데이지\t카네이션\t----')
print('----\t ⬜ \t\t ⬛ \t\t   ⬛ \t----')
print('------------------------------------')
print('----\t목화\t\t해바라기\t안개꽃\t----')
print('----\t ⬜ \t\t ⬛ \t\t   ⬛ \t----')
print('------------------------------------')
