class StudentScores:
    def __init__(self, filename):
        """파일에서 데이터를 읽어 scores 속성에 저장합니다."""
        self.scores = {}  # 학생 이름과 점수를 저장할 딕셔너리
        try:
            # 주어진 파일을 읽어서 데이터를 처리
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    # 각 줄을 이름과 점수로 분리하고 딕셔너리에 저장
                    name, score = line.strip().split(",")
                    self.scores[name] = int(score)  # 점수는 정수로 변환
        except FileNotFoundError:
            # 파일이 없을 경우 오류 메시지 출력
            print(f"{filename} 파일이 존재하지 않습니다.")
        except Exception as e:
            # 다른 예외 발생 시 오류 메시지 출력
            print(f"오류가 발생했습니다: {e}")

    def calculate_average(self):
        """평균 점수를 계산하여 반환합니다."""
        total = sum(self.scores.values())  # 점수의 총합 계산
        return total / len(self.scores)  # 평균 계산

    def get_above_average(self):
        """평균 점수 이상을 받은 학생들의 이름 리스트를 반환합니다."""
        average = self.calculate_average()  # 평균 점수 계산
        # 평균 점수 이상인 학생들의 이름 리스트 생성
        return [name for name, score in self.scores.items() if score >= average]

    def save_below_average(self, output_filename):
        """평균 이하 점수를 받은 학생들의 데이터를 파일로 저장합니다."""
        average = self.calculate_average()  # 평균 점수 계산
        with open(output_filename, "w", encoding="utf-8") as file:
            # 평균 이하 학생들의 데이터를 파일에 작성
            for name, score in self.scores.items():
                if score < average:
                    file.write(f"{name},{score}\n")

    def print_summary(self):
        """평균 점수와 평균 이상 학생 리스트를 출력합니다."""
        average = self.calculate_average()  # 평균 점수 계산
        above_average = self.get_above_average()  # 평균 이상 학생 리스트 생성
        # 결과 출력
        print(f"평균 점수: {average:.1f}")
        print(f"평균 이상을 받은 학생들: {above_average}")

# 프로그램 실행
filename = "scores_korean.txt"  # 한글 이름이 포함된 입력 파일
output_filename = "below_average_korean.txt"  # 평균 이하 학생 데이터를 저장할 출력 파일

# StudentScores 객체 생성 및 처리
student_scores = StudentScores(filename)  # 파일에서 데이터를 읽어 객체 생성
student_scores.print_summary()  # 평균 점수와 평균 이상 학생 리스트 출력
student_scores.save_below_average(output_filename)  # 평균 이하 학생 데이터를 파일에 저장


