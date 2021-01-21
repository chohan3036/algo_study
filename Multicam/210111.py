import pandas as pd

# 1차원 데이터
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

# 2차원 데이터
# 사전형식으로 입력
data = {
    'country': ['belgium', 'india', 'brazil'],
    'capital': ['brussels', 'new delhi', 'brasilia'],
    'population': [11111, 22222, 33333]
}
df = pd.DataFrame(data)
print(df)
df.to_excel('class.csv')

# 데이터/컬럼 따로 입력
data2 = {['belgium', 'brussels', 11111],
         ['india', 'new delhi', 22222],
         ['brazil', 'brasilia', 33333]}
df2 = pd.DataFrame(data2, columns=['country', 'capital', 'population'],)
