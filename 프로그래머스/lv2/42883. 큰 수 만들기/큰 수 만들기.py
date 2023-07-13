from itertools import combinations

def solution(number, k):
    
    # 순열 = n개의 원소를 사용해 순서를 정하여 r개의 배열로 나타내는 것.
    # 순열은 순서가 있어서 원소의 종류가 같아도 순서가 다르면 다른 배열.
    # 조합은 n개의 원소를 사용해서 순서의 관계없이 r개의 배열로 나타낸다.
    # 조합은 * 순서가 없어서 원소의 종류가 같으면 같은 배열로 나타낸다.
    
    # = > 아 조합을 사용하면 되네 - 시간 초과(시간을 줄일 수 있는 방법이 필요.)
#     num_combination = combinations(list(number), len(number)-k)
    
#     num_combi_list = map(int,map("".join, num_combination))
#     # prime_set = set(num_combi_list)
#     # print(prime_set)
#     answer = str(max(num_combi_list))
    
    
    # 스택 풀이법 - 핵심은 k와 스택리스트
    # 생각해야 할 것이 1. 리스트가 비어있을 때
                #    2. 값 비교해야할 때
                #    3. 추가할 때
                #    4. k개 제거하면 끝
                #    5. 예외 상황 가정
    answer = []
    for i in number:
        if len(answer) == 0:
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k-=1 # k개 제거하면 끝
                if k <= 0 or len(answer) == 0:
                    break # 비교 그만
        answer.append(i)
         # 리스트가 비어있지 않고, k<=0일 때(비교 끝이고, 더이상 제거할 필요 없을 때)
        
    answer = answer[0:-k] if k > 0 else answer
    # 이 경우까지 고려해야 되네 999 k=1 (비교를 못할 때)
    return ''.join(answer)
