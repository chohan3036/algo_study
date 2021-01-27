# 최단 경로 탐색 알고리즘 🚀
모두 **다이나믹 프로그래밍** 기반으로 하고 있다.

다이나믹 프로그래밍이란?

문제 해결까지의 단계를 여러 개로 나누어,  
첫번째 단계부터 마지막 단계까지 **메모이제이션**을 통해 
최적화 해 나가는 과정을 말한다.

## 1. 다익스트라 (Dijkstra)
#### 출발 노드로부터 그래프의 다른 모든 노드까지의 최단 거리와 경로를 찾는다.

> _어떤 점 R이 점 P를 거쳐 점 Q로 가는 최단 경로에 있는 꼭짓점이라면, 
> 이 경로는 마찬가지로 P에서 R까지 가는 최단 경로라는 사실을 이용한다._

### 알고리즘 (우선순위 큐를 사용했을 때)
1. 모든 노드를 미방문 상태로 표시하고, 미방문 노드를 우선순위 큐에 넣는다.
2. 시작 노드로부터의 거리를 저장할 거리 행렬을 만든다. 자기 자신을 0, 나머지는 무한으로 초기화한다.
3. 현재 노드에서 미방문한 인접 노드를 찾아 그 거리 값을 **갱신**한다. 새로 계산한 거리를 현재 값과 비교해서 더 작은 값을 넣는다.
4. 만약 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드를 방문한 것으로 표시하고 큐에서 제거한다.
5. 나머지 모든 노드로의 거리 값이 갱신될 때까지 반복한다.
6. 두 노드 사이의 경로를 찾는 경우: 도착점이 방문한 상태로 표시되면 멈추고 알고리즘을 종료한다.

[
![Dijkstra_Animation](https://user-images.githubusercontent.com/55574154/105514402-c9b9e900-5d16-11eb-9005-b7fd308ac4a1.gif)
](url)
[다익스트라 예시]

### Pseudo Code
    dist[source] ← 0                    // 초기화
    
    create vertex set Q
    
    for each vertex v in Graph:
        if v ≠ source
            dist[v] ← INFINITY          // 소스에서 v까지의 아직 모르는 길이
        prev[v] ← UNDEFINED             // v의 이전 노드(경로 생성)
        Q.add_with_priority(v, dist[v])

    while Q is not empty:
         u ← Q.extract_min()            // 가장 가까운 노드 선택
         for each neighbor v of u:      // Q 안에 있고, 인접한 노드를 순회
             alt ← dist[u] + length(u, v)
             if alt < dist[v]
                 dist[v] ← alt
                 prev[v] ← u
                 Q.decrease_priority(v, alt)
    
     return dist, prev

### 시간 복잡도
노드의 개수를 V, 간선의 개수를 E라고 했을 때,

- 인접 리스트를 활용한 선형 탐색 : `O(E + V^2)`
- 힙, 우선순위큐를 활용한 탐색 : `O(E*logV)`


## 2. 플로이드-와샬 (Floyd-Warshall)
#### 가능한 모든 노드 쌍 간의 최단 거리와 경로를 찾는다.

> 거쳐가는 노드를 기준으로 최단 거리와 경로를 갱신해 나간다.

### 알고리즘
1. 경로 행렬을 만든다. 노드 쌍 (u, v)에 대해 v를 저장한다.
2. 이번에 거쳐가는 노드를 설정한다. k
3. 거리 행렬을 모두 순회하며, 그 때의 노드 쌍 (i, j)의 거리와 (i, k, j)의 거리 중 작은 것으로 **갱신**한다.
4. 3에서 거리의 갱신이 일어나면, 경로 행렬 (i, j)에 경로 행렬 (i, k)값을 저장한다.
5. 모든 노드에 대해 반복한다.

![900px-Floyd-Warshall_example svg](https://user-images.githubusercontent.com/55574154/105522701-e78c4b80-5d20-11eb-9748-ad66adfc8066.png)
[플로이드 와샬 예시]


`k = 0`

|  |  |  |  |
|---|---|---|---|
| 0|∞ |-2| ∞|
| 4|0 | 3| ∞|
| ∞|∞ | 0| 2|
| ∞|-1| ∞| 0|

`k = 1`
 
|  |  |  |  |
|---|---|---|---|
| 0|∞ |-2| ∞|
| 4|0 | 2| ∞|
| ∞|∞ | 0| 2|
| ∞|-1| ∞| 0|

### Pseudo Code

    function FloydWarshallWithPathReconstruction():
        for each edge (u,v)
            dist[u][v] ← w(u,v)             // 간선 (u, v)의 가중치
            next[u][v] ← v                  // 간선 (u, v)의 경로
        
        for k from 1 to |V|                 // 모든 노드에 대해
            for i from 1 to |V|             // 다른 모든 노드로 가는 거리 및 경로 구함
                for j from 1 to |V|         // 따라서 거리 행렬을 계속 순회
                    if dist[i][j] > dist[i][k] + dist[k][j] then
                        dist[i][j] ← dist[i][k] + dist[k][j]
                        next[i][j] ← next[i][k]

### 시간 복잡도
노드의 개수를 V라고 했을 때,
- 최선, 최악의 경우 모두 `O(V^3)`


## 3. A* 알고리즘
#### 시작 노드에서 목표 노드까지의 최단 거리 및 경로를 구한다.

> 다익스트라와 유사하나, 각 단계에 대해 `h(n)`의 추정값을 적용하는 것이 차이점이다.

> `f(n) = g(n) + h(n)` 일 때,
> - `g(n)` : 시작 노드로부터 노드 `n`까지의 가중치
> - `h(n)` : 노드 `n`으로부터 목표 노드까지의 **추정** 가중치

### 알고리즘
1. 문제에 대한 `h(n)`을 정의한다. (맨하탄 거리, 유클리디안 거리 등)
2. 시작 노드를 큐에 넣는다.
2. 현재 노드에 방문 표시하고, 인접한 노드들에 대해 `f(n)`을 각각 구한다.
3. `f(n)`이 가장 작은 노드를 선택하고, 탈락한 노드들을 방문 표시한다.
4. 목표 노드에 도달할 때까지 반복한다.

### Pseudo Code

    function a_star():
        open.append(start)
        
        while open:
            cur_node <- min F val in open
            open.remove(cur_node)
            close.append(cur_node)
            
            if end == cur_node:
                print(ans)
            
            linked <- all neighbor node with cur_node
            for link in linked
                if link in close
                    continue
                
                link.f = g(cur_node) + 1 + h(link)
                if link in open and link.f > link in open.f
                    continue
                open.append(link)

### 시간 복잡도
정의한 `h(n)`에 따라 다르다.  
b가 각 노드의 하위 요소, d가 그래프의 깊이(트리 형태로 의사 결정을 하고 있음) 일 때,
- `O(b^d)`


# 그 외 그래프 알고리즘
## 위상 정렬
#### 방향 비순환 그래프에서 노드들의 순서(경로)를 정한다.
> 순환 그래프에서는 시작점이 존재하지 않기 때문에 적용 불가 ❌

### 알고리즘
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐에서 노드를 꺼내 연결된 간선을 모두 제거한다.
3. 진입차수를 갱신한다.
4. 큐가 빌 때까지 위 과정을 반복한다.

### Psudo Code

    function Topology():
        graph[u] = [v, x, ..]
        link[u] <- linked_cnt
        if link[u] == 0
            Q.append(u)
        
        while Q:
            ans.append(cur u)
            for v neighbor cur u
                link[v] -= 1
                if link[v] == 0
                    Q.append(v)
                    
               
### 시간 복잡도
노드의 개수를 V, 간선의 개수를 E라고 했을 때,
- `O(V + E)`


---
### 출처
- [다익스트라 (위키백과)](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%81%AC%EC%8A%A4%ED%8A%B8%EB%9D%BC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)  
- [플로이드-와샬 (위키백과)](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)  
- [A* 알고리즘 (Programming ETC 블로그)](https://choiseokwon.tistory.com/210)  
- [위상정렬 (안경잡이개발자 블로그)](https://blog.naver.com/ndb796/221236874984)