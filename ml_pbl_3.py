# 필요한 라이브러리 호출
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 데이터 불러오기
data = pd.read_csv('Mall_Customers.csv')

# 데이터 전처리
# CustomerID는 순서일 뿐이므로 삭제
data = data.drop(columns=['CustomerID'])

# 주요 특성 (Annual Income, Spending Score)으로 이루어진 데이터 추출
features = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# 데이터 표준화할 스케일러 생성 및 스케일링
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# 훈련용 데이터와 테스트 데이터로 분리
x_train, x_test = train_test_split(scaled_features, test_size=0.2, random_state=42)

# 엘보우 방법을 통해 관성값 계산 후 최적의 k값 찾기
wcss = []
K_range = range(1, 10)
for k in K_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42)
    kmeans_temp.fit(x_train)
    wcss.append(kmeans_temp.inertia_)

# 엘보우 그래프 그리기
plt.plot(K_range, wcss, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS (Within-Cluster Sum of Squares)")
plt.show()

# 최적의 k값 = 5
# k-means 모델 학습 및 테스트
kmeans = KMeans(n_clusters=5, random_state=42)
km_train = kmeans.fit(x_train) # 모델 학습
km_pred = kmeans.predict(x_test) # 테스트 데이터에 모델 적용

# 학습 데이터에 클러스터 정보 추가 후 데이터프레임으로 변환
fin_train = pd.DataFrame(x_train)
fin_train['Cluster'] = km_train.labels_

# 테스트 데이터에 클러스터 정보 추가 후 데이터프레임으로 변환
fin_test = pd.DataFrame(x_test)
fin_test['Cluster'] = km_pred

# silhoutte Score로 테스트 데이터의 클러스터링 결과 평가
# 학습 데이터와 테스트 데이터 각각 시각화

silhouette_avg = silhouette_score(x_test, km_pred)
print(f"Overall Silhouette Score: {silhouette_avg:.2f}")

# 4. 실루엣 점수 시각화 - 각 데이터 포인트의 실루엣 점수를 계산
silhouette_values = silhouette_samples(x_test, km_pred)

# 시각화 준비
y_lower = 10
for i in range(5): # 각 클러스터에 대해 반복
    ith_cluster_silhouette_values = silhouette_values[km_pred == i]
    ith_cluster_silhouette_values.sort()
    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i
    # 클러스터별 막대 그리기
    plt.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values)
    plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i)) # 클러스터 번호
    y_lower = y_upper + 10 # 다음 클러스터로 이동

# 그래프 설정
plt.axvline(x=silhouette_avg, color="red", linestyle="--") # 평균 실루엣 점수
plt.title("Silhouette Plot for K-Means Clustering")
plt.xlabel("Silhouette Score")
plt.ylabel("Cluster")
plt.show()

# 학습 데이터 시각화
for i in sorted(fin_train['Cluster'].unique()):
    tmp = fin_train.loc[fin_train['Cluster'] == i] #해당하는 클러스터 번호일 때 그림을 그리고, for문 실행하며 위에 덧그림 
    plt.scatter(tmp[0], tmp[1])
    plt.legend(sorted(fin_train['Cluster'].unique()))
plt.title("K-Means Clustering Results(train)")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()

# 테스트 데이터 시각화
for i in sorted(fin_test['Cluster'].unique()):
    tmp = fin_test.loc[fin_test['Cluster'] == i] #해당하는 클러스터 번호일 때 그림을 그리고, for문 실행하며 위에 덧그림 
    plt.scatter(tmp[0], tmp[1])
    plt.legend(sorted(fin_test['Cluster'].unique()))
plt.title("K-Means Clustering Results(test)")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()

# 0번 클러스터 : 소득과 소비 모두 전체 데이터 중 중앙에 분포함, 소득과 소비가 균형을 이루고 있음
# 1번 클러스터 : 소득과 소비 모두 전체 데이터 중 적은 군집, 소득과 소비가 균형을 이루고 있음
# 2번 클러스터 : 소득이 적지만 소비 점수는 높은 군집, 소득에 맞춰 소비를 줄일 필요가 있음
# 3번 클러스터 : 소득과 소비 모두 전체 데이터 중 많은 군집, 소득과 소비가 균형을 이루고 있음
# 4번 클러스터 : 소득이 많지만 소비 점수가 낮은 군집, 시장 경제의 활성화를 위해 소비를 더 늘려도 괜찮아 보임
print('0번 클러스터 : 소득과 소비 모두 전체 데이터 중 중앙에 분포함, 소득과 소비가 균형을 이루고 있음')
print('1번 클러스터 : 소득과 소비 모두 전체 데이터 중 적은 군집, 소득과 소비가 균형을 이루고 있음')
print('2번 클러스터 : 소득이 적지만 소비 점수는 높은 군집, 소득에 맞춰 소비를 줄일 필요가 있음')
print('3번 클러스터 : 소득과 소비 모두 전체 데이터 중 많은 군집, 소득과 소비가 균형을 이루고 있음')
print('4번 클러스터 : 소득이 많지만 소비 점수가 낮은 군집, 시장 경제의 활성화를 위해 소비를 더 늘려도 괜찮아 보임')