### 파이썬 데이터 시각화 - 엑셀 파일 시각화 ###

# xlsx -> 엑셀 파일
# 엑셀 문서 작성 후 - 파일명 : python0803으로 변경 (확장자 : .xlsx)
# 필요한 패키지 (pandas, numpy / openpyxl : 엑셀 )

# cmd(명령 프롬프트) & vsc 터미널(ctrl + shift + `) 모두 설치
# pip install pandas
# pip install numpy
# pip install openpyxl

# 프로그램 구현에 필요한 모듈 가져오기
import pandas as pd
import numpy as np

# pd.read_excel() 함수를 사용하여 Excel 파일 불러오기
# './python0803.xlsx': Excel 파일의 경로
# sheet_name="Sheet1"은 불러올 시트의 이름
# header=None은 파일의 첫 번째 행을 컬럼명으로 사용하지 않겠다는 의미
# index_col=None은 파일의 첫 번째 열을 인덱스로 사용하지 않겠다는 의미
dataframe = pd.read_excel('C:\\python-bt0720-sz\\0816\\python0803.xlsx', sheet_name='Sheet1', header=None, index_col=None)

# 데이터 추출 및 변환
# dataframe.iloc[0, 1:13]는 데이터프레임의 첫 번째 행과 2번째부터 13번째 열까지의 데이터를 선택
x축 = dataframe.iloc[0, 1:13].to_numpy # 선택한 행렬 데이터를 array로 변환
y축2020 = dataframe.iloc[1, 1:13].to_numpy
y축2021 = dataframe.iloc[2, 1:13].to_numpy
y축2022 = dataframe.iloc[3, 1:13].to_numpy

소비카테고리 = dataframe.iloc[5, 1:5].to_numpy
이번달소비금액 = dataframe.iloc[6, 1:5].to_numpy
이번달소비금액금액합계 = np.nansum(이번달소비금액, dtype='float16')

평균2020 = np.nansum(y축2020, dtype='float16')
평균2021 = np.nansum(y축2021, dtype='float16')
평균2022 = np.nansum(y축2022, dtype='float16')

import matplotlib.pyplot as plt
import platform

figure = plt.figure()

# 현재 사용중인 PC의 OS에 따라서 matplotlib의 폰트를 다르게 설정해주는 코드
if platform.system() == 'Darwin' : # Mac OS
    print.rc('font', family='AppleGothic')
else : 
    plt.rc('font', family='Malgun Gothic')

axes = figure.subplot(3, 1, 1)

axes.plot(x축, y축2020, marker='o', label='2020년')
axes.plot(x축, y축2021, marker='^', label='2021년')
axes.plot(x축, y축2022, marker='s', label='2022년')

plt.legend()
plt.xlabel('월')
plt.ylabel('카드사용금액')