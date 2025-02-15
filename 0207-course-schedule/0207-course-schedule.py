'''
# 207
참고 영상: https://www.youtube.com/watch?v=EgI5nU9etnU
문제 풀이: https://www.algodale.com/problems/course-schedule/

## 문제 개념정리
prerequisites란? 필수 선수 과목이다.  
방향성이 있는 연결 관계이므로, Directed Graph다.  
Cycle 발생 시, 코스를 이수할 수 없다.  
- 서로 의존하는 순환이 있을 때, 끝없이 돌게 되는 경우를 순환이라 함

## 해결 방식 두가지
1. BFS, Queue, Topological Sort: 위상 정렬
2. DFS, Cycle Detection: 순환 탐지

### 위상 정렬(Topological Sort) - BFS, Queue
- 진입 차수(indegree): 노드로 들어오는 화살표 수
- 그래프로 인접 리스트 구성
- Queue에 넣기
- Queue BFS 탐색
- 모든 과목을 들었는지 확인

### 순환 탐지(Cycle Detection) - DFS
- 그래프로 인접 리스트 구성
- 방문 상태 배열 초기화
- dfs 함수
- 모든 노드에 대해 dfs 실행

## TC & SC
- 시간 복잡도와 공간 복잡도는 O(V + E)로 동일하다.
```
V: 노드 수(과목 수)
E: 간선 수(선수 과목 관계 수)
```

### TC is O(V + E)

두 방법 모두, 그래프의 모든 노드와 간선을 한 번씩 확인함
- BFS: 모든 V를 순회하면서, 각 노드에서 나가는 E를 따라가며 차수를 줄임
- DFS: 모든 V를 순회하면서, 각 노드에서 연결된 E를 따라가며 깊이 탐색

### SC is O(V + E)
- V + E를 저장하는 인접 리스트 그래프 때문에 기본 공간 O(V+E)
- O(V) 공간들: 방문 상태 저장, 진입 차수 배열, BFS 큐, DFS 호출 스택

## 위상정렬(BFS) vs 순환탐지(DFS) \U0001f914

### BFS를 사용했을 때
- 반복문을 사용한 BFS가 indegree(진입차수) 개념이 보다 직관적이므로 => "순서대로 처리할 수 있는지 확인"할 때 명확하게 사용할 수 있다. 진입 차수가 0인 노드부터 시작해서 처리
- 선수 과목을 다 들은 과목은 진입 차수가 0이 되므로 들어갈 수 있는 과목이라는 점이 명확함
```
키워드: 처리 순서를 출력, 순서대로 처리할 수 있는지
```

### DFS를 사용했을 때
- DFS 순환 탐지는 "순환 여부"가 핵심일 때 자연스럽다.
- 상태(Status)를 사용해서, 방문 중인 노드 상태를 다시 방문한다면 순환이 있음을 바로 알 수 있다.
- 순환이 발견되면 바로 중단하므로, 순환 탐지에 자연스럽다.
```
키워드: 사이클이 있는지 판단
```

### 
'''
from enum import Enum

class Status(Enum): # use it to dfs
    INITIAL = 1
    IN_PROGRESS = 2
    FINISHED = 3

class Solution:
    def canFinishTopologicalSort(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        processed_count = 0

        while queue:
            node = queue.popleft()
            processed_count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return processed_count == numCourses

    def canFinishCycleDetection(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for dest, src in prerequisites:
            graph[src].append(dest)

        statuses = {i: Status.INITIAL for i in range(numCourses)}

        def dfs(node):
            if statuses[node] == Status.IN_PROGRESS:
                return False
            if statuses[node] == Status.FINISHED:
                return True

            statuses[node] = Status.IN_PROGRESS
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            statuses[node] = Status.FINISHED
            return True

        return all(dfs(crs) for crs in range(numCourses))

    def canFinishWithCache(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for dest, src in prerequisites:
            graph[src].append(dest)

        traversing = set()

        @cache
        def dfs(node):
            if node in traversing:
                return False

            traversing.add(node)
            result = all(dfs(pre) for pre in graph[node])
            traversing.remove(node)
            return result

        return all(dfs(node) for node in range(numCourses))

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for dest, src in prerequisites:
            graph[src].append(dest)

        traversing = set() 
        visited = set()    

        def dfs(node):
            if node in traversing:
                return False
            if node in visited:
                return True

            traversing.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            traversing.remove(node)

            visited.add(node) 
            return True

        return all(dfs(i) for i in range(numCourses))
