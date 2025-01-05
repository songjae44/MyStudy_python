"""문제 내용
Pima Indians Diabetes 데이터셋을 기반으로 다음 작업을 수행하세요:
1. 결측치 처리
    - Glucose, BloodPressure, SkinThickness, Insulin, BMI 열에서 값이 0인 경우를 결측치로 간주하고, 평균값으로 대체하세요.
2. 이상치 처리
    - SkinThickness와 Insulin 열에서 이상치(상위 1% 값)를 결측치로 간주하고 평균값으로 대체하세요.
3. 데이터 정규화
    - Age 열의 값을 MinMaxScaler를 사용하여 0~1 범위로 정규화하세요.
4. 탐색적 데이터 분석
    - 각 열의 결측치 개수를 출력하세요.
5. Outcome(당뇨병 유무)에 따른 Glucose의 평균 값을 구하세요.
    - 결과 확인
6. 처리 후 데이터프레임의 첫 5개 행을 출력하세요.

데이터셋 정보: Diabetes Dataset (diabetes.csv 파일 사용)

https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database"""

"""문제가이드

1. 결측치 처리

 - 특정 값을 결측치로 간주하고 대체

2. 이상치 처리

 - 상위 이상치(상위 1%)를 처리하고 평균값으로 대체

3. 데이터 정규화

 - MinMaxScaler를 사용하여 데이터 범위를 조정

4. 탐색적 데이터 분석

 - 데이터의 결측치를 확인하고 그룹별 통계량을 계산"""

# 필요한 라이브러리 호출
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 데이터 불러오고 데이터프레임 형태로 변환
data = pd.read_csv('diabetes.csv')
df = pd.DataFrame(data)

# 1. 결측치 처리
# Glucose, BloodPressure, SkinThickness, Insulin, BMI 열에서 값이 0인 경우를 결측치로 간주하고, 평균값으로 대체하세요.
# 목표 컬럼들의 리스트 생성
zero_features = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
# 리스트에 포함된 컬럼에서 값이 0인 데이터는 None값으로 대체
for feature in zero_features:
    df[feature] = df[feature].replace(0, None)
    # None 값을 평균 값으로 대체
    df[feature] = df[feature].fillna(df[feature].mean())

# 2. 이상치 처리
# SkinThickness와 Insulin 열에서 이상치(상위 1% 값)를 결측치로 간주하고 평균값으로 대체하세요.
# 대상 컬럼 리스트 생성
iqr_features = ['SkinThickness', 'Insulin']
# 대상 컬럼에서 상위 1%값 평균으로 대체
for feature in iqr_features:
    df.loc[df[feature] > df[feature].quantile(0.99), feature] = df[feature].mean()

# 3. 데이터 정규화
# Age 열의 값을 MinMaxScaler를 사용하여 0~1 범위로 정규화하세요.
scaler_minmax = MinMaxScaler()
df['Age'] = scaler_minmax.fit_transform(df[['Age']])

# 4. 탐색적 데이터분석
# 각 열의 결측치 개수를 출력하세요.
print(df.isna().sum())

# 5. Outcome(당뇨병 유무)에 따른 Glucose의 평균 값을 구하세요.
grouped = df.groupby('Outcome')['Glucose'].mean()
print(grouped)

# 6. 첫 5개의 행 출력
print(df.head())