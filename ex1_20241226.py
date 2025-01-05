# 필요한 라이브러리 호출
import pandas as pd # csv불러오기
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 데이터 생성
data = pd.read_csv('Mall_Customers.csv')

# 데이터 전처리
# CustomerID 컬럼은 그저 순서이므로 삭제
data = data.drop('CustomerID', axis=1)

# 데이터 정규화
features = data[['Annual Income (k$)', 'Spending Score (1-100)']]
sclaer = StandardScaler()
scaled_features = sclaer.fit_transform(features)

# K-Means 클러스터링 모델 생성
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(scaled_features)

# 데이터프레임에 클러스터 값 추가
data['Cluster'] = kmeans.labels_

# 시각화
plt.scatter(scaled_features[:, 0], scaled_features[:, 1],
            c=data['Cluster'], cmap='viridis', s=30, label='Clustered Data')
# 클러스터 중심 시각화
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c='red', label='centroids', marker='x')
plt.title('Data after Clustering')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()

# 각 클러스터의 기초 통계값 확인
cluster_stats = data.groupby('Cluster').describe()
print(cluster_stats)