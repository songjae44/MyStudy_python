# 필요한 라이브러리 호출
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 데이터 로드
data = pd.read_csv('winequality-red.csv')

# 주요 특성(와인의 화학적 특성)선택
# quality를 제외한 모든 컬럼
features = data.drop('quality', axis=1)

# 데이터 정규화
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# k = 3 으로 클러스터링
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_features)

# 클러스터 레이블 데이터프레임에 추가
data['Cluster'] = kmeans.labels_

# 클러스터 품질 해석
# quality에 따른 클러스터 별 평균값 비교
cluster_means = data.groupby('Cluster').mean()
quality_clu_means = data.groupby('Cluster')['quality'].mean()
print('클러스터 별 평균')
print(cluster_means)
print('quality에 따른 cluster별 평균값')
print(quality_clu_means)

#PCA를 사용해 데이터 축소
pca = PCA(n_components=2)
features_pca = pca.fit_transform(scaled_features)

# PCA시각화
# 클러스터링 결과 시각화
plt.figure(figsize=(10, 6))
for cluster in range(3):
    cluster_data = features_pca[data['Cluster'] == cluster]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {cluster}')


# 클러스터 중심 시각화
centroids = kmeans.cluster_centers_
pca_centroids = pca.transform(centroids)
plt.scatter(pca_centroids[:, 0], pca_centroids[:, 1], s=200, c='red', marker='X', label='Centroids')

plt.title('K-Means Clustering of Wine Quality')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()