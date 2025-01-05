# 필요한 라이브러리 가져오기
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 클래스 생성

class SalesAnalysis:
    def __init__(self, year):
        self.year = year

    # 날짜 데이터 생성 함수
    def create_dates(self):
        y = self.year
        return pd.date_range(f'{y}-01-01', f'{y}-12-31', freq='D')
    
    # 매출 데이터 생성 함수
    def create_sales(self):
        return np.random.randint(1000,10000,len(self.create_dates()))
    
    # 날짜와 매출이 결합된 데이터 생성 후 데이터 프레임으로 변환하는 함수
    def data_to_df(self):
        data = {'Date' : self.create_dates(), 'Sale' : self.create_sales()}
        df = pd.DataFrame(data)
        return df
    
    # 데이터 프레임에서 월별로 매출 총 합을 구한 후 월 별 매출이 매칭되는 시리즈 데이터 생성
    def monthly_sale(self):
        df = self.data_to_df()
        df['월'] = df['Date'].dt.month
        df_m = df.groupby(by='월')['Sale'].sum()
        #df.set_index(df['Date'], inplace=True)
        #df_m = df.resample('M')['Sale'].agg(np.sum).fillna(0)
        return df_m
    
    # 그래프 출력 함수
    def plot_grapgh(self):
        x = self.monthly_sale().index
        y = self.monthly_sale()

        plt.rc('font', family='Malgun Gothic')
        plt.plot(x, y, marker='o', linestyle='-', color='b')

        plt.title('월별 매출 총합')
        plt.xlabel('월')
        plt.ylabel('매출')
        plt.legend()

        plt.grid(True)
        plt.show()


        
    