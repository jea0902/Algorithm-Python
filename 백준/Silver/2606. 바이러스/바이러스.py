# 그래프 문제는 먼저, graph 형식을 만들 것. - 노드, 간선, 그래프
# bfs, dfs 함수 형식 떠올리기
# 특히 나는 그냥 딕셔너리로

from collections import deque
import copy # dfs 노드들 역순으로 둬야해서 import copy


# map함수는 iterable한 객체를 입력받아야 한다.

n = int(input()) # 첫째 줄 노드 수
m = int(input()) # 둘째 줄 간선 수

g = {i:[] for i in range(1,n+1)} # 그래프 형식 = 키(i): [] for i in range(1,노드 수 +1)

for i in range(1,m+1): # 셋째 줄 부터 간선을 " " 형식으로 입력.
    a, b = map(int,input().split(" "))
    g[a].append(b)
    g[b].append(a)
    
for i in range(1,n+1):
    g[i].sort() # 모든 노드들 sort 세팅

start = 1 # 1번 노드가 감염되면 총 몇개의 노드가 감염되는지 출력하시오.

def bfs(g,start): # 선입선출이 bfs
    
    visit = list() # 탐색 완료한 애들 추가
    q = deque()
    # 큐 대기열 # from collections import deque 이걸 가져와서,
    # deque로 해야된단다.
    
    q.append(start)
    
    while q:
        #node = q.pop(0)
        node = q.popleft()
        if node not in visit:
            visit.append(node)
            q.extend(g.get(node,[])) # extend는 iterable(객체)의 모든 항목을 append
            # 그래프에 node가 있으면 node를 가져오는데,
            # node가 없으면 뒤의 []를 반환.
            
    return len(visit) - 1 # 1번 노드 빼줘야 함..

#def dfs(g,start): # 후입선출이 dfs
    
#    visit = list()
#    s = list()
    
#    node = []
    
#    s.append(start)
    
#    while s:
#        node = s.pop()
#        if node not in visit:
#            visit.append(node)
#            extended_nodes = copy.deepcopy(g.get(node,[]))
#            extended_nodes.sort(reverse=True) # 글로벌 g가 바뀌어버려서 초기화 필수.
#            s.extend(extended_nodes)
            
#     return len(visit)
    
print(bfs(g,start))





