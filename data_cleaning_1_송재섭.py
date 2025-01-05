# 문제 1: 결측치 처리
# 결측치(Missing Value)는 데이터 분석 과정에서 처리해야 할 중요한 이슈 중 하나입니다.
# 결측치를 처리하는 방법은 여러 가지가 있습니다.
# 가장 간단한 방법은 결측치를 모두 제거하는 것입니다.
# 하지만, 결측치가 너무 많은 경우 데이터의 손실이 크기 때문에 다른 방법을 사용해야 합니다.
# 대표적인 방법으로 결측치를 대체하는 방법이 있습니다.
# 결측치를 대체하는 방법은 다양한 방법이 있습니다.
# 가장 간단한 방법은 평균값, 중앙값, 최빈값 등으로 대체하는 것입니다.
# 이번 문제에서는 평균값, 최빈값으로 결측치를 대체하는 방법을 사용합니다.
 
# Kaggle의 "Titanic - Machine Learning from Disaster" 데이터셋을 사용하여 결측치를 처리하세요.
# Titanic - Machine Learning from Disaster  데이터셋 링크: https://www.kaggle.com/competitions/titanic
# Kaggle Titanic 데이터셋 링크로 이동 -> Data 탭 -> train.csv 다운로드
# train.csv 파일을 다운로드 -> train.csv 파일을 작업 디렉터리에 저장

# 데이터셋을 불러온 후, 다음과 같이 결측치를 처리하세요.
# Age 열의 결측치는 평균값으로 대체합니다.
# Embarked 열의 결측치는 최빈값(Mode)으로 대체합니다.
# Cabin 열은 결측치가 너무 많아서 삭제합니다.
# 결측치 처리 후, 결측치가 모두 제거되었는지 확인하는 코드를 작성하세요.

# 필요한 라이브러리 호출
import pandas as pd

# 데이터 불러오기
data = pd.read_csv('train.csv')

# 불러온 데이터로 데이터프레임생성
df = pd.DataFrame(data)

# Age열의 결측치는 평균값으로 대체
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Embarked 열의 결측치는 최빈값으로 대체
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Cabin 열의 결측치는 너무 많아서 삭제
# 결측치가 있는 열 제거
df = df.drop(['Cabin'], axis=1)

# 결측치가 모두 제거되었는지 확인
print(df.isnull().sum())

print(df)