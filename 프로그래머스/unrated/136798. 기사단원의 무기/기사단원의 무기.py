def solution(number, limit, power):
    # number 기사단원 수 , limit는 공격력 제한 수치, 초화한 기사가 사용할 무기 공격력 power 
    # 공격력 1당 1kg 철 - 무기점에서 최종 필요한 철의 무게 
    answer = 0
    
    # 약수의 갯수를 먼저 구해야 함. 나누는 수 1,2,3,4,5,6,7,8,9
    # 약수의 갯수 로직 ex 10 1 2 5 10  1 - 10 2 - 5 3x4x5x6x7x8x9x 나누었을 때 나머지가 0 
    
    
    for i in range(1,number+1): # 고민1. 이중for문이고 number가 10만까지라서 시간초과 - 66.7
        cnt_ys = 0 # 약수 갯수 i마다 초기화
        # k = 0
        for j in range(1,int(i**0.5)+1):
            # *** 약수 갯수는 제곱근까지만 검사하면 된다.(반이 아니라)
                
            # if j == k:            몫 차례일 때 바로 넘기려고 넣은건데 시간차이X
            #     cnt_ys += 1
            #     continue
            if i%j == 0:
                if i // j == j: # 제곱근이 약수인 경우, 중복 카운트를 피하자
                    cnt_ys += 1
                else:   
                # k = i//j # 시간 줄이려고 몫(반대쪽) 차례가 나오면 바로 cnt 늘리고 continue
                    cnt_ys += 2 # ex 10일 때 2x5일 때 양쪽 다 +1씩
        if cnt_ys > limit:
            cnt_ys = power
        answer += cnt_ys
        
    return answer