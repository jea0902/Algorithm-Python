def solution(numbers):
    # 이런 완전탐색 문제를 풀 때, for문 쓰면서 코드를 줄이고 줄여도 계속 시간초과면 다른 방법으로 풀라는 의미.
    # 이런 문제를 스택으로 풀라는 게 악질문제
    
#     answer = [0]*(len(numbers)-1) + [-1] 
    
#     for i in range(0,len(numbers)):
#         if i == len(numbers):
#             answer[i] = -1
#             break
#         else:
#             for j in range(i+1,len(numbers)):
#                 if numbers[i] < numbers[j]:
#                     answer[i] = numbers[j]
#                     break
#                 else:
#                     answer[i] = -1
#     return answer

    answer = [-1] * len(numbers)
    stk = []
    # [2,3,3,5]
    for i in range(len(numbers)): # 4
        while stk and numbers[stk[-1]] < numbers[i]: # 2 < 3
            answer[stk.pop()] = numbers[i] # stk[0] = 3
        stk.append(i) # 0
    
    return answer

# 자신보다 큰 수를 찾는 문제는 스택 유형인 경우가 많다.
# 순서대로 삽입되면서 조건에 충족한 수(자신보다 큰 수)가 들어오는 경우에 스택을 비우면 된다.

# enumerate를 쓰면 idx,값을 한번에 할당해 사용할 수 있고, 시간효율성도 좋기에 써보자.
