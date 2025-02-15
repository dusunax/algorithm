'''
# 207
참고 영상: https://www.youtube.com/watch?v=EgI5nU9etnU
문제 풀이: https://www.algodale.com/problems/course-schedule/

## 문제 개념정리
- prerequisites: 필수 선수 과목
- 그래프: 방향성이 있는 연결 관계이므로, Directed Graph
- Cycle 발생 시, 코스를 이수할 수 없음
    - 서로 의존하는 순환이 있을 때, 끝없이 돌게 되는 경우를 순환이라 함

## 해결 방식
1. BFS, Queue, Topological Sort: 위상 정렬
2. DFS, Cycle Detection: 순환 탐지

## 위상 정렬(Topological Sort) - BFS, Queue
- 진입 차수(indegree): 노드로 들어오는 화살표 수
- 그래프로 인접 리스트 구성
- Queue에 넣기
- Queue BFS 탐색
- 모든 과목을 들었는지 확인

## 순환 탐지(Cycle Detection) - DFS
- 그래프로 인접 리스트 구성
- 방문 상태 배열 초기화
- dfs 함수
- 모든 노드에 대해 dfs 실행
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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