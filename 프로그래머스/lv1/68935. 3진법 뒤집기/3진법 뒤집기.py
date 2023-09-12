def solution(n):
    나머지 = []
    while True:
        if n == 0:
            return 0
        if n//3 == 0:
            나머지.append(n%3)
            break
        나머지.append(n%3) # 만약에 2면 여기서 2 나머지 들어가고 아래에서도 2 들어가버려서 틀리네
        n = n//3
    # print(''.join(map(str,나머지[::-1]))) # int 리스트를 3진법으로 바꾸는 법
    # 여기선 굳이 뒤집을 필요가 없어서
    결과 = ""
    for i in 나머지:
        결과 += str(i)
    # 결과 = 결과.lstrip("0") # 아래 문법이 있으니 이건 필요 없게됨.
    
    return int(결과,3) # int(String,n) => n진법인 String을 10진법으로 변환