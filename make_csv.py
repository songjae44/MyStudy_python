import pandas as pd

# 1. 가짜 데이터 생성
data = {
    'ProductID': [101, 102, 103, 104, 101, 102, 103, 105, 106, 101],
    'ProductName': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'E', 'F', 'A'],
    'Price': [100, 200, 300, 400, 100, 200, 300, 500, 600, 100],
    'Quantity': [1, 2, 3, 4, 1, 2, 3, 5, 6, 1]
}

# 2. DataFrame 생성
df = pd.DataFrame(data)

# 3. 중복된 데이터를 일부 추가 (중복된 행 4개 추가)
df.loc[len(df.index)] = [101, 'A', 100, 1]  # 중복 행 추가
df.loc[len(df.index)] = [102, 'B', 200, 2]  # 중복 행 추가
df.loc[len(df.index)] = [103, 'C', 300, 3]  # 중복 행 추가
df.loc[len(df.index)] = [104, 'D', 400, 4]  # 중복 행 추가

# 4. CSV 파일로 내보내기
df.to_csv('sales.csv', index=False)

print("sales.csv 파일이 생성되었습니다.")
