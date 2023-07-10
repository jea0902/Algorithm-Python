def solution(progresses, speeds):
    days = 0 # 한 날짜에 한번만 일괄적 배포
    cnt = 0 # 배포 완료 수
    answer = []
    
    # 스택처럼 한방향으로 빼주면서 클리어
    while len(progresses) > 0:
        if (progresses[0] + days*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        else: # 100을 못넘었으면 - 연속으로 배포할 수 없을 때의 조건 + 날짜 변경
            if cnt > 0: # 배포해야 될 게 있어?
                answer.append(cnt) # 이 날은 여기까지만 배포하고,
                cnt = 0 # 카운트 초기화
            days += 1 # 배포 수 추가 다하고 카운트까지 초기화하고 나서야 날짜 바꾸고
    
    answer.append(cnt) # 마지막 녀석 추가
    return answer