import re
from collections import Counter
import csv
import os

# IP 추출 함수
# 로그 파일에서 IP 주소를 추출하는 함수
def extract_ips_from_log(file_path):
    try:
        # 로그 파일을 읽기 모드로 열기
        with open(file_path, "r") as log_file:
            log_data = log_file.read()  # 로그 파일 전체 내용을 읽어들임
            
            # 정규 표현식을 사용하여 IP 주소 추출
            # IP 주소 형식: 숫자.숫자.숫자.숫자 (0~255 범위, 여기서는 단순한 형식만 검출)
            ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
            # 정규 표현식에 매칭되는 IP 주소를 모두 찾음
            ip_addresses = re.findall(ip_pattern, log_data)  
            return ip_addresses  # 추출된 IP 주소 리스트 반환
    except FileNotFoundError:  # 파일이 존재하지 않을 경우
        print("로그 파일을 찾을 수 없습니다.")  # 에러 메시지 출력
        return None  # None 반환

# IP 빈도 분석 함수
# 추출된 IP 주소들의 빈도를 계산하는 함수
def analyze_ip_count(ip_addresses):
    return Counter(ip_addresses)  # IP 주소 리스트를 입력받아 각 IP의 개수를 세는 Counter 객체 반환

# CSV 저장 함수
# 분석 결과를 CSV 파일로 저장하는 함수
def save_to_csv(counter, output_file):
    # CSV 파일을 한글이 깨지지 않도록 utf-8-sig 인코딩으로 저장
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)  # CSV 작성 객체 생성
        writer.writerow(["IP 주소", "접속 횟수"])  # 헤더 작성
        # Counter 객체의 아이템(IP, 빈도)을 행 단위로 작성
        writer.writerows(counter.items())  
    # 저장 완료 메시지 출력
    print(f"분석 결과가 '{output_file}' 파일에 저장되었습니다.")  

# 실행
log_file_path = "access.log"  # 분석할 로그 파일의 경로
output_file = "ip_analysis.csv"  # 분석 결과를 저장할 CSV 파일의 경로

# 로그 파일 존재 여부 확인
if not os.path.exists(log_file_path):  # 로그 파일이 존재하지 않으면
    # 오류 메시지 출력
    print(f"로그 파일 '{log_file_path}'이(가) 존재하지 않습니다.")  
    exit(1)  # 프로그램 종료

# IP 주소 추출
ips = extract_ips_from_log(log_file_path)
if ips:  # IP 주소가 정상적으로 추출되었을 경우
    # IP 빈도 분석
    ip_count = analyze_ip_count(ips)
    
    # 상위 3개 IP 주소와 빈도를 출력
    print("\nIP 주소 빈도 분석 결과 (상위 3개):")
    # 가장 많이 등장한 상위 3개 IP 출력
    for ip, count in ip_count.most_common(3):  
        print(f"{ip}: {count}회")
    
    # 분석 결과를 CSV 파일로 저장
    save_to_csv(ip_count, output_file)  
