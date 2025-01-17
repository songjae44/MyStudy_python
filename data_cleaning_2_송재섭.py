# 문제 2: 중복 데이터 제거
# 중복 데이터(Duplicate Data)는 데이터 분석 과정에서 중요한 이슈 중 하나입니다.
# 데이터셋에 중복된 데이터가 포함되어 있는 경우, 분석 결과가 왜곡될 수 있습니다.
# 따라서 중복 데이터를 식별하고 제거하는 작업은 데이터 전처리 과정에서 중요한 단계입니다.
# 이번 문제에서는 중복 데이터를 제거하는 방법을 실습합니다.

# 임의의 데이터셋을 사용하여 중복 데이터를 제거하는 작업을 수행하세요.

# 다음은 인공지능 수업에서 사용할 전처리 문제입니다. 
# 중복 데이터를 포함하는 생성된 파일 데이터셋을 사용하여 중복 데이터를 제거하는 작업을 수행하세요.

# 문제 요구 사항
# sales.csv 파일을 불러옵니다. 이 파일에는 중복된 행이 일부 포함되어 있습니다.
# 중복된 행을 모두 제거한 후, 남은 데이터의 개수를 확인하세요.
# 중복된 데이터의 개수를 출력하세요.

# 필요한 라이브러리 호출
import pandas as pd

# csv파일 불러오기
data = pd.read_csv('sales.csv')

# 불러온 데이터 데이터프레임으로 변환
df = pd.DataFrame(data)

#print(df)

# 중복된 값이 어느 것인지 출력
print('아래 데이터프레임은 중복된 값을 모아놓은 것')
print(df[df.duplicated()])
#print(type(df[df.duplicated()]))

# 중복된 데이터의 개수 출력
print(f'중복된 데이터의 개수 :\n{len(df[df.duplicated()])}')

# 중복된 행 모두 제거 후 남은 데이터 확인
df = df.drop_duplicates()
print('아래 데이터프레임은 중복된 행을 제거 한 것')
print(df)

# 중복된 행 제거 후 남은 데이터 개수
print(f'중복된 데이터 제거 후 남은 개수 :\n{len(df)}')