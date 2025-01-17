# -*- coding: utf-8 -*-
"""ml_pbl_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sCFUkeP7T76h_7c6TUkxpPgcdjQZu5cW
"""

# 드라이브 마운트 후 데이터 압축해제

#from google.colab import drive
#drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/dataset

#!unzip -qq "/content/drive/MyDrive/dataset/web_server_logs_2.zip"

# 데이터 불러오고 확인

import pandas as pd

df = pd.read_csv('web_server_logs_2.csv')
df.head()

df.info()

# 데이터 전처리

# 'timestamp' 열을 datetime 형태로 변환
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 'timestamp' 열에서 시간대를 추출하여 'hour'라는 새로운 열을 생성
df['hour'] = df['timestamp'].dt.hour

# 데이터 확인
df.head()

df.info()

# pandas의 get_dummies 함수를 사용하여 원-핫 인코딩을 수행
df = pd.get_dummies(df, columns=['method'], prefix=['method'])

df.head()

import numpy as np

# size 열에 로그 변환 적용
df['size'] = np.log1p(df['size'])

df.head()

df.info()

# status_code값을 success와 error상태 값으로 나타내기

# is_success 컬럼 생성
df['is_success'] = df['status_code'].apply(lambda x: 1 if x >= 200 and x < 300 else 0)

# is_error 컬럼 생성
df['is_error'] = df['status_code'].apply(lambda x: 1 if x >= 400 else 0)

df.head()

# 모델 학습 전 최종 데이터
# timestamp, status_code 컬럼 삭제
df = df.drop(['timestamp', 'status_code'], axis=1)

# label 컬럼을 target으로 분리
target = df['label']

# 훈련용 데이터 train
train = df.drop(['label'], axis=1)

train.info()

target.info()

# ip주소를 int형으로 변경
import ipaddress

train['ip'] = train['ip'].apply(lambda x: int(ipaddress.IPv4Address(x)))

train.head()

train.info()

# ip컬럼을 표준화
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# ip컬럼을 2차원 배열로 변환
ip_int_values = train[['ip']].values.astype(float)
train['ip'] = scaler.fit_transform(ip_int_values)

train.head(10)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 특성(X)과 타겟(y) 데이터 설정
X = train  # 특성 데이터 (train)
y = target # 타겟 데이터 (target)

# 데이터를 훈련 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Logistic Regression 모델 생성
model = LogisticRegression(random_state=42)

# 모델 학습
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 정확도
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# 정밀도
precision = precision_score(y_test, y_pred)
print(f"Precision: {precision}")

# 재현율
recall = recall_score(y_test, y_pred)
print(f"Recall: {recall}")

# F1-Score
f1 = f1_score(y_test, y_pred)
print(f"F1-Score: {f1}")