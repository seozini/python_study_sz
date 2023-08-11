### 파이썬 외부 모듈 - pandas ###

# pandas
 # : Python Data Analysis Library의 약자
 # : 파이썬에서 데이터 분석을 위해 사용되는 라이브러리

# pandas DataFrame 생성
 # : 여러 개의 컬럼으로 구성된 2차원의 데이터 구조

import pandas as pd

# DataFrame 생성

df = pd.DataFrame({
    'A' : [1, 2, 3],
    'B' : ['a', 'b', 'c']
})

# 데이터 엑세스 : 특정 데이터에 접근

# column에 접근 (세로)
print(df['A'])
 # A값을 인덱스 번호로 나누어서 출력

# rom에 접근 (가로)
print(df.loc[1])
 # 인덱스 번호의 데이터를 출력
