# 문제 5: 데이터 스케일링
# 데이터 스케일링은 데이터의 범위를 조정하는 작업을 의미합니다.
# 데이터 스케일링을 통해 데이터의 분포를 조정하고, 모델의 성능을 향상시킬 수 있습니다.
# 대표적인 데이터 스케일링 방법으로는 StandardScaler, MinMaxScaler, RobustScaler 등이 있습니다.
# 이번 문제에서는 StandardScaler를 사용하여 데이터를 표준화하는 방법을 실습합니다.

# Kaggle의 "Wine Quality" 데이터셋을 사용하여 데이터를 스케일링하세요.
# fixed acidity, volatile acidity, citric acid, residual sugar, chlorides 열의 값을 StandardScaler로 표준화하세요.
# 표준화된 결과를 출력하세요.

# 데이터셋 다운로드
# Kaggle Wine Quality 데이터셋 링크: https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009
# Kaggle Wine Quality 데이터셋 링크로 이동 -> Data 탭 -> winequality-red.csv 다운로드 -> winequality-red.csv 파일을 작업 디렉터리에 저장

# 데이터셋을 불러온 후, 데이터 스케일링을 수행하는 코드를 작성하세요.

# 필요한 라이브러리 호출
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 데이터 불러와서 데이터프레임으로 변환
data = pd.read_csv('winequality-red.csv')
df = pd.DataFrame(data)

# 표준화
# fixed acidity, volatile acidity, citric acid, residual sugar, chlorides 열의 값을 모아놓은 리스트 생성
features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides']
# 반복문을 통해 각 컬럼을 표준화
for feature in features:
    scaler_standard = StandardScaler()
    df[f'{feature}_standard'] = scaler_standard.fit_transform(df[[feature]])

# 데이터 확인
print(df)

# 데이터 시각화
# 입력받은 컬럼의 표준화 시각화
fig = input('시각화할 컬럼명을 입력하세요 : ')
plt.figure(figsize=(10, 5))
plt.plot(df[fig], label=f'Original {fig}', marker='o')
plt.plot(df[f'{fig}_standard'], label=f'Standardized {fig}', marker='o')
plt.legend()
plt.title('original vs standard')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()