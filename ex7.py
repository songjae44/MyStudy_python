# 필요한 라이브러리 임포트
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report # 평가 지표

# 데이터 불러오기
data = pd.read_csv('creditcard.csv')

# 기존 데이터 분리
x_data = data.drop('Class', axis=1)
y_data = data['Class']

# 데이터 표준화
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_data)

# PCA로 차원 축소
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scaled)

# 스케일링 된 x데이터프레임으로 변형
ori_df = pd.DataFrame(x_pca, columns=['F1', 'F2'])

# y를 합치기
df = pd.concat([ori_df, y_data], axis=1)

# 기존 데이터 시각화
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(10, 6))
plt.scatter(
df["F1"], df["F2"],
c=df['Class'].map({0: "blue", 1: "red"}), # 색상 매핑
label='Traffic'
)
plt.title("Traffic Data with Isolation Forest Anomaly Detection")
plt.xlabel("F1")
plt.ylabel("F2")
plt.legend(['Normal', 'Anormal'])
plt.grid()
plt.show()

#Isolated Forest 모델 학습
model = IsolationForest(n_estimators=100, contamination=0.017, random_state=42)

ori_df['Anomaly Score'] = model.fit_predict(ori_df)
ori_df['Anomaly'] = ori_df['Anomaly Score'].apply(lambda x: 0 if x == 1 else 1)

# 학습된 이상치 데이터 시각화
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(10, 6))
plt.scatter(
ori_df["F1"], ori_df["F2"],
c=ori_df['Anomaly'].map({0: "blue", 1: "red"}), # 색상 매핑
label='Traffic'
)
plt.title("Traffic Data with Isolation Forest Anomaly Detection")
plt.xlabel("F1")
plt.ylabel("F2")
plt.legend(['Normal', 'Anomaly'])
plt.grid()
plt.show()

# 평가지표 출력
print(classification_report(y_data, ori_df['Anomaly']))