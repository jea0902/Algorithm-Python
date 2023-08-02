def solution(prices):
    
    # prices의 길이가 10만 이하라서 이거 시간 효율성 테스트
        # **이중 for문이 무조건 느린 게 아니다. 연산 한줄에 의해서도 코드의 소요 시간이 크게 차이날 수 있다는 걸 알게됨.
        # 참고자료 : https://velog.io/@gouz7514/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%EB%93%9C-%EC%8B%9C%EA%B0%84-%EB%8B%A8%EC%B6%95time-complexity
    
    answer = [0]*len(prices)    
    
    # 1차 시도 : 테스트 1만 맞고 전부 틀림 + 전부 시간초과 => 로직 아예 틀린 거고, 이중 for문은..
    # 3차 시도 : 이중 for문 형태는 유지하되, 내부 코드를 바꿔주는 것만으로도 시간이 확 준다는 블로그 참고
    for idx in range(0,len(prices)):
        for idx2 in range(idx+1,len(prices)):
            if prices[idx] > prices[idx2]: # 시간을 줄여주려면 가격이 한번이라도 떨어졌을 때 바로 break하려고 앞에 있어야 함.      # answer[idx] += 1처럼 하나하나 올려주는 게 아니라 바로 할당
                answer[idx] += 1
                break
            else:                                   
                answer[idx] += 1
    return answer

    # 2차 시도 : 리스트 요소끼리 빼주어서 0이상인 애들의 수로 => 마찬가지
    # for idx in range(0,len(prices)):
    #     new_p = [prices[idx]]*(len(prices)-idx-1)
    #     not_under_0 = [pi - ni for pi,ni in zip(prices[idx+1:],new_p)]
    #     count = len([c for c in not_under_0 if c >= 0])
    #     answer[idx] += count
    # return answer
    