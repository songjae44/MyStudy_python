import re

# IP 주소에 매칭할 정규식 패턴을 정의
IP_PATTERN = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# 로그 파일을 열음
with open('access.log', 'r') as f:
    # 파일 내용을 문자열로 읽어옴
    log = f.read()

    # 정규식을 사용하여 로그에서 IP 주소를 추출
    ips = re.findall(IP_PATTERN, log)

    # 각 IP 주소의 발생 횟수를 계산
    ip_counts = {} #딕셔너리 생성
    for ip in ips:
        if ip in ip_counts:
            ip_counts[ip] += 1 #해당 ip 를 키 값으로 가지는 value에 +1
        else:
            ip_counts[ip] = 1
    
    # ip 주소를 횟수가 많은 순서로 정렬 [:3] 으로 상위 3개만 정렬
    most_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    # 상위 3개 ip 주소와 해당 주소의 발생 횟수 출력
    for ip, count in most_ips:
        print(f'ip : {ip}, 빈도 수 : {count}')

