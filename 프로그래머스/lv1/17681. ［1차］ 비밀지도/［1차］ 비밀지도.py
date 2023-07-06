def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        print(tmp)# 2진수 각 자릿수를 AND, OR, XOR, NOT 연산을 하는 비트 논리 연산자 &,|,^,~ # 여기서 쓰이는 |는 둘중 하나라도 1이면 1 # tmp 결과 ex) '0b1101'
        tmp = tmp[2:].zfill(n) # n자릿수일 때 빈공간 0으로 채워줄 것
        print(tmp)
        # 2진수로 바꾸면 앞에 0b가 붙기 때문에 제거 해주고
        # zfill함수로 0으로 채워줘 앞에도 0이 올 수 있도록 한다. 
        # 문자열에서만 사용가능한 zfill함수 기억
        tmp = tmp.replace("0"," ").replace("1","#")
        answer.append(tmp)
    return answer