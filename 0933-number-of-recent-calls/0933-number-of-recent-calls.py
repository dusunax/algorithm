'''
## 해석
- 리퀘스트 카운터다.
- `ping(t)`: 최고 3000 밀리초 내의 call 수를 반환한다. [t-3000, t]
    - 현재 요청 포함
    - 요청은 항상 시간 순서대로 증가: 모든 ping 요청은 이전 요청보다 더 많은 call 수를 반환한다.

## 구현 방향
- 범위 내의 순차적인 요소들에 접근하기 위해 배열, 연결리스트, 큐를 사용할 수 있음

### 인덱스 포인터를 사용하지 않아도 되는 이유:
- ping은 시간 순으로 호출됨이 *보장*됨 (문제의 볼드처리 문구는 항상 유의할 점)
    - 항상 이전 요청보다 시간상 나중에 호출: t1< t2< t3 ...
- `t - 3000`보다 작은 요청은 항상 리스트 앞쪽에 위치
    - 매번 3000 밀리초 이전 요청만 앞에서 제거하면 된다.
    - `범위 밖으로 벗어난 값은 항상 리스트 앞에 존재`
- 굳이 startIdx, endIdx 같은 인덱스 포인터로 범위를 계산할 필요 없음, requests 배열을 업데이트함

> \U0001f4a1 만약 RecentCounter에서 이전의 모든 로그를 공간에 유지하면서, 3000ms 요청 수만 반환하는 경우라면, startIdx를 멤버변수로 유지하면서 유효한 윈도우가 시작되는 위치를 업데이트할 수 있다.

### 배열보다 큐를 사용해야 하는 이유:
- 파이썬 List의 pop은 동적 배열 앞의 모든 요소들을 한 칸씩 당기므로 TC O(n)이다.
- 파이썬 Deque는 양방향 연결리스트 구조로, 포인터를 이동하기 때문에 삭제 연산이 TC O(1)이다.
- 데이터에서 많은 삭제/중간삽입 등의 연산이 필요한 경우에 Deque가 이점이 있다.
'''

class RecentCounter:
    def __init__(self):
        self.r_dq = deque()
        self.r_list = []

    '''
    TC: O(n^2)
    SC: O(n)
    '''
    def ping(self, t: int) -> int:
        self.r_list.append(t)

        while self.r_list[0] < t - 3000: # TC: O(n)
            self.r_list.pop(0) # TC: O(n)

        return len(self.r_list)

    '''
    TC: O(n) # 모든 요소를 지우는 최악의 경우 O(n)
    SC: O(n) # requests deque

    '''
    def pingDeque(self, t: int) -> int:
        self.r_dq.append(t)

        while self.r_dq[0] < t - 3000: # TC: O(n)
            self.r_dq.popleft() # TC: O(1)

        return len(self.r_dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)