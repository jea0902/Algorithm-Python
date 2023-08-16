# import itertools

# def solution(l, r):
#     answer = []
#     str_list = [str(i) for i in range(l,r+1)]
#     # 아 맞다. 콤비네이션인가뭔가 그 순열 쓰면 되잖아 카드 느낌으로
#     # 순열 = n개 중 r개를 선택한 뒤, 순서대로 정렬하는 것
#     # 조합 = n개 중 r개를 선택하는 것(순서 고려X 튜플같음.)
#     i = 0
#     nums = [0]*len(str(r)) + [5]*len(str(r))
#     perm = itertools.permutations(nums,len(str(r)))
#     # combination은 0,5랑 5,0이랑 같다고 보네.
#     lp = ''.join(list(perm))
#     print(lp)
    
#     # 1. l,r이 어디에 있는지 + 어디에 있든 그거에 맞는 로직이 필요  l<=x<=r
#     # 2. "0"과 "5"로 이루어진 정수 배열을 만들어야 함.
    
# #     for i in range(l,r+1):
    
# #     else:
# #         answer.append(-1)
    
#     return lp

def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    
    return answer
