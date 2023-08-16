def solution(n, computers):
    # ***이해하기 어려우니까 목요일에도 다시 보기
    
    # DFS 사용
    
#     answer = 0
#     visit = [False for i in range(n)]
    
#     for com in range(n):
#         if visit[com] == False:
#             DFS(n,computers,com,visit)
#             answer += 1 # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크 맞네
#     return answer

# def DFS(n,computers,com,visit):
#     visit[com] = True
#     for connect in range(n):
#         if connect != com and computers[com][connect] == 1: # 연결된 컴퓨터
#             if visit[connect] == False:
#                 DFS(n,computers,connect,visit)
                
    # BFS 사용
    
    answer = 0
    visit = [False for i in range(n)]
    
    for com in range(n):
        if visit[com] == False:
            BFS(n,computers,com,visit)
            answer += 1
    return answer

def BFS(n,computers,com,visit):
    visit[com] = True # 여기 세줄은 가장 큰 바깥 범위의 list 3개
    queue = []
    queue.append(com)
    while queue: # 여기서부터는 바깥 범위의 list 1개씩 보는 것. // 여기가 두번째로 도는
        com = queue.pop(0)
        visit[com] = True # 이게 있어야 하네?
        for connect in range(n): # 여기가 가장 먼저 돌고,
            if connect != com and computers[com][connect] == 1:
                if visit[connect] == False:
                    queue.append(connect)
        
    
    
    
    
    
    
    
#     # n = 노드의 수
#     # 독립적 네트워크 수 = return
    
#     # 76.9점이라 예외 경우의 수를 고려해줘야 하나봄.
#     # 테스트4 실패, 5 런타임 에러, 7 실패
    
#     # 런타임 에러는
#     # 0으로 나누었을 때 발생하는 zerodivisionerror
#     # 인덱싱을 할 때 길이 이상으로 했을 때 발생하는 IndexError
#     # 선언하지 않은 변수를 사용할 때 발생하는 NameError가 발생합니다.
#     # 이밖에도 TypeError(연산, 함수가 계산할 때 데이터의 유형이 잘못되었을 때)
#     # valueError(데이터의 타입이 맞지 않아 발생하는 에러)
    
#     g = {i:[] for i in range(1,n+1)}

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if computers[i-1][j-1] == 1:
#                 if i==j:
#                     continue
#                 else:
#                     g[i].append(j) # 인덱스 때문에 -1씩 해줘야 할 거 같은데
#     print(g)
#                     # 이차원 배열은 g[i].append(j)랑 g[j].append(i)하면 값이 두번씩 들어가더라.
#                     # g[j].append(i)
#                     # print(g)
                
#     for i in range(1,n+1):
            
#         if g[i] != []:
#             visit = []
#             q = []
#             q.append(i)
#                 # node = [] # while 문 안의 node가 정의되어있지 않아서 초기화
#             while q:
#                 node = q.pop()
#                 if node not in visit:
#                     visit.append(node)
#                     q.extend(g.get(node,[]))
#     print(visit)
    
#     if len(visit) == 0:
#         answer = n
#     else:
#         answer = n - len(visit) + 1 # 하나라도 연결이 안되어 있으면 그냥 n이 답임.
    
#     return answer