# 문제 4: 범주형 데이터 인코딩
# 범주형 데이터(Categorical Data)는 문자열 형태로 표현되는 데이터를 의미합니다.
# 머신러닝 알고리즘은 문자열 데이터를 바로 사용할 수 없기 때문에 숫자 형태로 변환해야 합니다.
# 범주형 데이터를 숫자 형태로 변환하는 방법에는 여러 가지가 있습니다.
# 대표적인 방법으로 Label Encoding과 One-Hot Encoding이 있습니다.
# Label Encoding은 각 범주(Category)를 숫자로 매핑하는 방식입니다.
# One-Hot Encoding은 각 범주를 이진 벡터로 표현하는 방식입니다.


# Kaggle의 "Adult Income" 데이터셋을 사용하여 범주형 데이터를 인코딩하세요.
# workclass, education, marital-status, occupation, relationship, race, gender, native-country 열을 Label Encoding으로 변환하세요.

# 데이터셋 다운로드
# Kaggle Adult Income 데이터셋 링크: https://www.kaggle.com/wenruliu/adult-income-dataset
# Kaggle Adult Income 데이터셋 링크로 이동 -> Data 탭 -> adult.csv 다운로드 -> adult.csv 파일을 작업 디렉터리에 저장

# 데이터셋을 불러온 후, 범주형 데이터를 인코딩하는 코드를 작성하세요.

# sklean 설치
# !pip install scikit-learn

# 필요한 라이브러리 호출
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 데이터 불러오고 데이터프레임 생성
data = pd.read_csv('adult.csv')
df = pd.DataFrame(data)
#print(df)
#print(df.dtypes)

# 레이블 인코딩
# workclass, education, marital-status, occupation, relationship, race, gender, native-country 열을 Label Encoding으로 변환
# 정해진 컬럼만 모아놓은 리스트 생성
features = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender','native-country']
# 반복문을 통해 정해진 컬럼 모두 인코딩 실행
for feature in features:
    label_encoder = LabelEncoder()
    df[feature] = label_encoder.fit_transform(df[feature])
print(df)



