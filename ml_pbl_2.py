# 필요한 라이브러리 호출
import pandas as pd # csv 불러오기
from sklearn.model_selection import train_test_split # 학습 및 테스트 데이터 분리
import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score # mae계산
from sklearn.tree import DecisionTreeRegressor

# 데이터 불러오기
data = pd.read_csv('house.csv')
#print(data)

# 데이터 정보 확인
print(data.info())

# 결측치 처리
# 결측치가 1460개의 20%이상인 292개 이상인 컬럼은 drop
data = data.dropna(axis=1, thresh=292)
#print(data.info())

# LotFrontage는 평균값으로 대체
data['LotFrontage'] = data['LotFrontage'].fillna(data['LotFrontage'].mean())
#print(data.info())

# 범주형 데이터 처리
# pd.get_dummies를 이용하여 범주형 데이터를 숫자로 변환
data2 = pd.get_dummies(data = data)
#print(data)
#print(data2)
#print(data2.info())

# 불필요한 ID 열 제거
data2 = data2.drop(['Id'], axis=1)
#print(data2)
#print(data)

# 학습데이터와 테스트 데이터 나누기 (8:2)
# 마지막 컬럼인 SalePrice를 분리
x = data2.drop(['SalePrice'], axis=1)
y = data2['SalePrice']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# DecisionTreeRegressor 사용하여 모델 학습 및 예측
model = DecisionTreeRegressor()
model.fit(x_train, y_train) # 학습데이터로 훈련
# 테스트 데이터 예측
y_pred = model.predict(x_test)

# 성능평가 - MAE 계산
mae = mean_absolute_error(y_test, y_pred)
#r2 = r2_score(y_test, y_pred)
print(f'mae : {mae}')
#print(f'R^2 : {r2}')