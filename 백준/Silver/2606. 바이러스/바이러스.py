# 그래프 문제는
# 1. 입력받는 거랑, graph 형식 완료 (n,m,g)
# 2. g[i].sort()
# 3. 함수

import copy # dfs 노드들 역순으로 둬야해서 import copy

# dfs 풀이

n = int(input())
m = int(input())

g = {i:[] for i in range(1,n+1)}

for i in range(1,m+1):
    a,b = map(int,input().split(' '))
    g[a].append(b)
    g[b].append(a)
    
for i in range(1,n+1):
    g[i].sort()
    
start = 1

def dfs(g,start):
    visit = []
    s = []
    # node = [] # 이거 필요한지 알았는데 필요없다네?
    
    s.append(start)
    
    while s:
        node = s.pop()
        if node not in visit:
            visit.append(node)
            extended_nodes = copy.deepcopy(g.get(node,[]))
            extended_nodes.sort(reverse=True)
            s.extend(extended_nodes)
    return len(visit) - 1
    
print(dfs(g,start))
    