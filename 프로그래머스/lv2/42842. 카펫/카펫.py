def solution(brown, yellow):
    answer = []
    # 문제에서 노란색 격자가 무조건 직사각형이어야한다라는 말이 없었다.
    
    # a >= b
    # ab - (a-2)*(b-2) = brown
        # ab - ab + 2a + ab - 4네 풀어보면 나오는구나.. 직사각형 넓이를 이용한 갯수
    # (a-2) * (b-2) = yellow
    
    # brown + yellow = ab(가로*세로) 이건 알고있었고, - 약수까지 생각했었음. - 약수문제 맞네
    
    # 가로가 특정 몇이고, 세로가 특정 몇인지 알 수 있는 로직은?
    
    # 외부 사각형 갯수 : 2a + 2b - 4 = brown
    # 내부 사각형 갯수 : (a-2)*(b-2) = yellow
    
    size = brown + yellow # size = a*b
    # 카펫의 가로 길이가 세로 길이보다 크거나 같아서 큰 수에서 작은 수로 반복문 완전탐색 - 즉 약수 중에서 a가 같거나 큰 최소 수
    
    for a in range(size,2,-1): # a구하기/거꾸로 a최소가 3
        if size % a == 0: # 약수라면
            b = size // a # b는 전체를 a로 나눈 것의 몫일 테니까 - 그래야 약수 짝이 맞지
            if (a-2)*(b-2) == yellow:
                answer.append(a)
                answer.append(b)
                break
    
    return answer