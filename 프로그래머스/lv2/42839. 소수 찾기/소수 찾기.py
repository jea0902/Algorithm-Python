from itertools import permutations

# 순열로 조합을 해야 할 때, 즉 순서가 바뀐 것도 다른 조합이다라고 여기고싶을 때는 permutation 사용
# 리스트랑, 몇개씩 뽑을지만 정해주면 됨. 

def solution(numbers): # 숫자가 적힌 문자열
    answer = 0
    prime_set = set() # 중복 제거 집합
    
    # 1. 모든 숫자 조합을 만든다. - 파이썬 permutation 경우의 수 모든 조합 만들어주는 유용한 함수
    for i in range(len(numbers)):
        num_permutaion = permutations(list(numbers), i + 1)
        # 첫인자는 각각 떨어져있는 리스트[] 주고,
        # 첫인자들을 이용해서 몇개로 조합을 할까?가 두번째 인자 => i = 0일 때 1개 , i = 1일때 2개
        num_per_list = map(int, map("".join, num_permatation))
        # 4가지 경우의 수에 전부 "".join 함수를 적용시켜 (그룹함수 map)
        # 스트링으로 전부 엮어준 후, int화
        # => [1,7] [17,71]
        prime_set = prime_set | set(num_per_list) # set라 합집합 
        # 한 곳에 집합화 => {1,71,17,7}
        
    # 2. 소수가 아닌 수를 제외한다.
    prime_set -= set(range(0,2)) # 0,1은 소수 제외
    lim = int(max(prime_set)**0.5) # 어차피 제일 큰 값에 루트 씌어준 애까지만 확인해보면 소수인지 아닌지를 확인 가능 - 에라토스 핵심이자 약수의 대칭 성질. ex 13 , 71 
    for i in range(2,lim + 1):
        prime_set -= set(range(i*2,max(prime_set)+1,i)) # i텀 = 배수처럼

    
    return len(prime_set)

    # ex) 71이면 2의 배수 제거, 3배수 제거, 4배수 제거 --- 8x9보다 작으므로 8배수까지만 제거해보면 71이 소수인지 알 수 있다.
    
    # 에라토스테네스의 체 : 약수의 성질 때문에 n이 아니라 n의 제곱근까지만 약수가 있는지를 확인해보면 소수 찾기가 더 빠르고 편해진다.
    
    
    from itertools import permutations

def solution(numbers):
    answer = []                                   
    nums = [n for n in numbers]                   # numbers를 하나씩 자른 것
    per = []                                      
    for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))        # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per]   # 각 순열조합을 하나의 int형 숫자로 변환

    for n in new_nums:                            # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:                                 # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈
            if n % i == 0:                        # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n)                      # 소수일경우 answer 배열에 추가

    return len(set(answer))                       # set을 통해 중복 제거 후 반환
    
            
    