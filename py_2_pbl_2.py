#문제 주제

#학생의 과목별 성적 분석 및 시각화 프로그램 개발

#문제 내용

#20명의 학생의 수학, 영어, 과학 점수를 분석하여 다음 작업을 수행합니다.

#학생 성적 분석 프로그램을 StudentScoreAnalysis 클래스로 개발합니다.

#분석 요구사항

#- 과목별 평균 점수를 계산하고 막대 그래프로 시각화 합니다.
#- 평균 성적 상위 5명의 학생을 막대 그래프로 시각화 합니다.
#- 학생 데이터 생성 ( __init__ )
#    - 학생의 이름, 수학, 영어, 과학 성적을 포함하는 데이터프레임을 생성합니다.
#    - 이름: '학생1'부터 '학생20'까지의 이름을 생성합니다.
#    - 예: ['학생1', '학생2', ..., '학생20']

#수학, 영어, 과학: 50부터 100 사이의 정수 난수를 20개 생성하여 각 과목의 점수를 할당합니다.

# 필요한 라이브러리 호출
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 클래스 생성
class StudentScoreAnalysis:
    def __init__(self):
        name= []
        for i in range(1, 21):
            name.append(f'학생{i}')
        math = np.random.randint(50, 100, len(name))
        eng = np.random.randint(50, 100, len(name))
        sci = np.random.randint(50, 100, len(name))