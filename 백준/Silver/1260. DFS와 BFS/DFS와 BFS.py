import copy

n, m, start = map(int, input().split(' '))

# 딕셔너리형으로 풀이 이유
# 1. 내가 이해하기 쉬웠다.
# 2. 리스트보다 빠르다고 함.

graph = {i: [] for i in range(1, n+1)}
    # 모든 정점을 키로 가지는 항목 추가
    # 값을 빈 리스트로 두고, 뒤에 appned로 추가할 수 있게

# 문제 풀이 순서
# 1. 먼저, 그래프 형식 딕셔너리로 g = {i:[] for i in range(1,노드수+1)}
# 2. 간선 주어진 걸로 그래프 만들고, 그래프 sort 해주고 시작
# 3. DFS, BFS 함수 만들어주면 끝.


for i in range(1, m + 1): # m개의 간선이 주어졌으니까.
    a, b = map(int, input().split(' '))
    graph[a].append(b) # 딕셔너리 값 추가 방법 : 딕셔너리[키].append(값)
    graph[b].append(a)    
    
for i in range(1,n+1): # 모든 노드들 sort (기본 세팅)**
    graph[i].sort()
    


def Dfs(graph,start):
    
    visit = list()
    stack = list() # 뒤에 있는 애들부터 깊게 탐색하니까 stack
    # 선입후출의 DFS
    
    node = [] # 이 문제선 노드까지 리스트로 만들어줘야하네.
    
    stack.append(start)

    while stack:

        node = stack.pop()
        if node not in visit:
            visit.append(node)
            extended_nodes = copy.deepcopy(graph.get(node,[]))
            # 얘를 미리 변수로 저장하고 얘만 sort reverse하고
            # 추가하면 되잖아?
            extended_nodes.sort(reverse=True)
            # 얘는 이렇게 하면 글로벌 graph가 바뀐다고 함. 그래서 초기화 해줘야 함.
            # Dfs 함수에서 extended_nodes.sort(reverse=True)를 사용하면
            # 원래의 graph의 노드 순서가 변경되어 버립니다.
            # 파이썬에서 객체는 참조에 의해 전달되므로, 
            # extended_nodes 리스트를 정렬하면 원래의 graph의 노드 순서도 변경되어 버립니다.

            #이 문제를 해결하기 위해 Dfs 함수에서 extended_nodes를 정렬하기 전에 이를 복사해야 합니다.
            # 이를 위해 copy 모듈의 deepcopy 함수를 사용할 수 있습니다.
            stack.extend(extended_nodes)
    return visit


def Bfs(graph,start):
# BFS는 숫자가 적은 노드부터 탐색하게 만드려면 sort 필요 없는가?
# 대신 성철이가 말했던 거 처럼 처음부터 sort를 해주면 될 듯? 그래프 요소 하나하나에서
# 기본 세팅 sort + 선입선출인 BFS는 어차피 적은 숫자 노드부터 탐색함.


    visit = list() # 탐색 완료한 친구들 추가
    queue = list() # 큐 대기열 (노드 탐색 리스트)
    
    queue.append(start)
    
    while queue: # 큐가 남아 있다면 반복해서 탐색 로직

        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph.get(node,[]))
        # graph에 node가 있으면 node를 가져오는데, node가 없으면 뒤의 []를 반환한다.
    
    return visit # 탐색 완료된 친구들 출력

# print(Dfs(graph,start))
# print('') # 백준식 출력
# Bfs(graph,start)

# 백준식 출력
for i in Dfs(graph,start):
    print(i,end=" ")
print("")
for j in Bfs(graph,start):
    print(j,end=" ")