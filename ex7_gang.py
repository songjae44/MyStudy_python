import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트를 맑은 고딕으로 설정
mpl.rc('font', family='Malgun Gothic')

# 1. 데이터 로드
# Kaggle에서 다운로드한 Credit Card Fraud Detection 데이터를 로드합니다.
data = pd.read_csv('creditcard.csv')

# 2. 데이터 탐색
print("데이터 요약 정보:")
#print(data.info())
print("\n결측치 확인:")
#print(data.isnull().sum())

# 'Time'과 'Amount'는 전처리가 필요하므로 스케일링 전용으로 분리
features = data.drop(columns=['Class'])  # 예측 변수인 'Class'는 제외
labels = data['Class']  # 'Class'는 실제 레이블로 활용

# 3. 데이터 스케일링
# 'Amount'와 'Time' 컬럼은 분포가 다르기 때문에 표준화 진행
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# 4. Isolation Forest 모델 학습
# Isolation Forest를 사용하여 이상치 탐지
model = IsolationForest(n_estimators=100, contamination=0.002, random_state=42)
model.fit(features_scaled)

# 이상치 탐지 결과
# `-1`은 이상치, `1`은 정상치를 의미
predictions = model.predict(features_scaled)
data['Anomaly'] = predictions

# 5. 이상치 탐지 결과 분석
# 이상치로 판별된 데이터를 확인
outliers = data[data['Anomaly'] == -1]
normal = data[data['Anomaly'] == 1]
print(f"이상치 수: {len(outliers)}")
print(f"정상치 수: {len(normal)}")

# 이상치 범주 출력
print("\n이상치 데이터의 주요 통계:")
print(outliers.describe())

# Class 특성과 Anomaly 특성 비교
print("\nClass와 Anomaly의 관계 분석:")
comparison = data.groupby(['Class', 'Anomaly']).size().unstack(fill_value=0)
print(comparison)

# 6. 시각화를 통한 이상치 확인
# Amount와 Time을 기준으로 이상치와 정상치를 시각화
plt.figure(figsize=(10, 6))
plt.scatter(normal['Time'], normal['Amount'], label='정상 데이터', s=1, alpha=0.5)
plt.scatter(outliers['Time'], outliers['Amount'], label='이상치', color='red', s=1,  alpha=0.7)
plt.xlabel('Time')
plt.ylabel('Amount')
plt.title('Isolation Forest를 사용한 이상치 탐지')
plt.legend()
plt.show()

# 7. 결과 저장
# 이상치 탐지 결과를 CSV 파일로 저장
outliers.to_csv('outliers_detected.csv', index=False)

# 코드 실행 완료 메시지
print("이상치 탐지가 완료되었습니다. 결과는 'outliers_detected.csv'에 저장되었습니다.")

# 8. 추가 분석
# 이상치 데이터의 Class 분포 확인
# 분류 report 출력
from sklearn.metrics import classification_report
print(classification_report(data['Class'], data['Anomaly'], zero_division=0))