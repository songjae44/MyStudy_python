# 문제 3: 이상치 제거 (IQR 이용)

# 이상치(Outlier)는 데이터의 전체적인 패턴과 동떨어진 관측치를 의미합니다.
# 이상치는 데이터 분석 결과를 왜곡하고, 모델의 성능을 떨어뜨릴 수 있습니다.
# 이상치를 탐지하고 처리하는 것은 데이터 전처리 과정에서 중요한 작업 중 하나입니다.
# 이번 문제에서는 IQR(Interquartile Range) 방식을 사용하여 이상치를 탐지하고 제거하는 방법을 실습합니다.

# IQR은 사분위 범위로, 데이터의 상위 75%와 하위 25% 사이의 범위를 의미합니다.
# IQR은 Q3(75% 분위수) - Q1(25% 분위수)로 계산합니다.
# IQR을 사용하여 이상치의 경계를 계산할 수 있습니다.
# 이상치는 Q1 - 1.5 * IQR 보다 작거나, Q3 + 1.5 * IQR 보다 큰 경우로 정의합니다.
# 이상치를 제거하는 방법은 이 경계를 벗어나는 데이터를 제거하는 것입니다.


# "Diamonds" 데이터셋을 사용하여 이상치 제거 문제를 해결하세요.
# 이 데이터셋은 다이아몬드의 가격과 관련된 다양한 특징(캐럿, 컷, 색상, 투명도 등)을 포함하고 있습니다.

# 문제 요구 사항
# carat 열에서 IQR 방식을 사용하여 이상치를 제거하세요.
# 이상치를 제거한 후 데이터의 개수를 출력하세요.
# 이상치의 경계를 계산하여 하한(lower bound)과 상한(upper bound) 값을 출력하세요.

# 데이터셋 다운로드
# 데이터셋 이름: "Diamonds"
# 출처: Kaggle Diamonds Dataset
# 파일명: diamonds.csv
# 데이터 다운로드 방법: Kaggle의 데이터셋 페이지로 이동하여 diamonds.csv 파일을 다운로드합니다.

# Download 버튼을 클릭하여 diamonds.csv 파일을 다운로드 -> diamonds.csv 파일을 작업 디렉터리에 저장

# 데이터셋을 불러온 후, 이상치를 제거하는 코드를 작성하세요.

# 필요한 라이브러리 호출
import pandas as pd
import numpy as np

# 데이터 불러오기 및 데이터프레임으로 변환
data = pd.read_csv('diamonds.csv')
df = pd.DataFrame(data)

# carat 열에서 IQR 계산
Q1 = df['carat'].quantile(0.25) # 1사분위수
Q3 = df['carat'].quantile(0.75) # 3사분위수
IQR = Q3 - Q1

# 이상치 기준
lower_bound = Q1 - 1.5 * IQR # 하한
upper_bound = Q3 + 1.5 * IQR # 상한

# 하한, 상한 이상치 경계값 출력
print(f'하한 경계값 : {lower_bound}, 상한 경계값 : {upper_bound}')

# 기존 데이터의 개수
print(f'기존 데이터의 개수 : {len(df)}')

# 이상치 확인
outliers = df[(df['carat'] < lower_bound) | (df['carat'] > upper_bound)]
print('아래 데이터프레임은 이상치들의 모음')
print(outliers)
print(f'이상치 개수 : {len(outliers)}개')

# 이상치 제거
df = df[(df['carat'] >= lower_bound) & (df['carat'] <= upper_bound)]
print('아래 데이터프레임은 이상치들을 제거한 데이터프레임')
print(df)
print(f'이상치 제거 후 데이터 개수 : {len(df)}')