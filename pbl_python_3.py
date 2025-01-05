import os
import time
import re

# 모니터링할 디렉터리 경로
MONITOR_DIR = "./monitor_directory"

# 감지할 주요 정보 패턴 정의
# PATTERNS 딕셔너리의 키는 탐지하려는 정보 유형이며, 값은 해당 정보를 찾기 위한 정규 표현식입니다.
PATTERNS = {
    "comments": r"#.*",  # 주석: '#'로 시작하는 모든 문자열
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",  # Email 주소: 일반적인 이메일 형식
    "sql": r"SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER"  # SQL 키워드: 주요 SQL 명령어
}

# 주의 대상 확장자: 모니터링 대상 파일 중 주의가 필요한 확장자 목록
WATCH_EXTENSIONS = (".js", ".class", ".py")

# 이미 존재하는 파일 리스트를 초기화
def get_initial_files(directory):
    """
    주어진 디렉터리의 파일 목록을 반환.
    디렉터리가 존재하지 않을 경우 빈 집합을 반환.
    Args: directory (str): 모니터링할 디렉터리 경로.
    Returns: set -> 디렉터리에 존재하는 파일 이름들의 집합.
    """
    return set(os.listdir(directory)) if os.path.exists(directory) else set()

# 파일 내용에서 주요 정보 검색
def scan_file_for_issues(filepath):
    """
    파일 내용을 확인하여 주요 정보(주석, 이메일, SQL 코드 등)를 탐지.
    Args: filepath (str): 파일 경로.
    Returns: list-> 발견된 주요 정보의 목록 (줄 번호, 내용, 유형).
    """
    issues = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):  # 파일을 한 줄씩 읽고 줄 번호를 함께 반환
            for issue_type, pattern in PATTERNS.items():  # 주요 정보 패턴과 매칭
                if re.search(pattern, line):  # 패턴과 일치하는 내용이 있으면
                    issues.append((line_number, line.strip(), issue_type))  # 줄 번호, 내용, 유형 저장
    return issues

# 디렉터리를 모니터링하고 새로운 파일을 분석
def monitor_directory(directory, known_files):
    """
    디렉터리를 모니터링하여 새로운 파일을 감지하고 분석.
    Args: directory (str)-> 모니터링할 디렉터리 경로.
        known_files (set)-> 이미 존재하는 파일 이름들의 집합.
    Returns:
        set: 업데이트된 파일 이름들의 집합.
    """
    # 현재 디렉터리에 존재하는 파일 목록
    current_files = set(os.listdir(directory))
    # 새로운 파일 감지
    new_files = current_files - known_files

    if new_files:  # 새로운 파일이 발견된 경우
        print(f"[INFO] 새로운 파일이 추가되었습니다: {new_files}")

        for new_file in new_files:
            filepath = os.path.join(directory, new_file)  # 파일의 전체 경로 생성
            
            # 파일 확장자가 주의 대상인 경우 경고 출력
            if new_file.endswith(WATCH_EXTENSIONS):
                print(f"[WARNING] 주의 파일 발견: {new_file}")
            
            # 파일 내용 스캔하여 주요 정보 탐지
            try:
                issues = scan_file_for_issues(filepath)
                if issues:  # 주요 정보가 발견된 경우
                    print(f"[ALERT] {new_file}에서 중요한 정보가 발견되었습니다:")
                    for issue in issues:
                        line_number, content, issue_type = issue
                        print(f"  - {issue_type} (줄 {line_number}): {content}")
            except Exception as e:  # 파일 분석 중 오류 발생 시
                print(f"[ERROR] {new_file} 분석 중 오류 발생: {e}")

    return current_files  # 업데이트된 파일 목록 반환

if __name__ == "__main__":
    # 모니터링할 디렉터리가 존재하는지 확인
    if not os.path.exists(MONITOR_DIR):
        print(f"[ERROR] 디렉터리 {MONITOR_DIR}가 존재하지 않습니다.")
        exit(1)  # 프로그램 종료
    
    print(f"[INFO] {MONITOR_DIR} 디렉터리 모니터링 시작...")
    # 초기 파일 리스트 가져오기
    known_files = get_initial_files(MONITOR_DIR)
    
    try:
        while True:
            # 디렉터리 모니터링 및 업데이트
            known_files = monitor_directory(MONITOR_DIR, known_files)
            time.sleep(1)  # 1초 간격으로 디렉터리 확인
    except KeyboardInterrupt:  # 사용자가 Ctrl+C를 눌러 종료할 경우
        print("[INFO] 모니터링 종료")
