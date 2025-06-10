'''
## 해석
- 리퀘스트 카운터다.
- 이전 3000 밀리초 내의 call 수를 반환한다. [t-3000, t]
    - 현재 요청 포함
- 모든 ping 요청은 이전 요청보다 더 많은 call 수를 반환한다.
- 구현 시 SC와 TC는 O(n) 예상: 범위 내의 순차적인 요소들에 접근하기 위해 배열, 연결리스트, 큐를 사용할 수 있음

## 구현 방향
### 인덱스 포인터를 사용하지 않아도 되는 이유:
- ping은 시간 순으로 호출됨이 *보장*됨 t1< t2< t3 ...
- 매번 3000 밀리초 이전 요청만 앞에서 제거하면 된다. => `범위 밖으로 벗어난 값은 항상 리스트 앞에 존재` (볼드처리 문구는 항상 유의할 점)
- startIdx, endIdx 같은 인덱스 포인터로 범위를 계산할 필요 없음, requests 배열을 업데이트함
- 만약 RecentCounter에서 이전의 모든 로그를 공간에 유지하면서, 3000ms 요청 수만 반환하는 경우라면, startIdx를 멤버변수로 유지하면서 유효한 윈도우가 시작되는 위치를 업데이트할 수 있다.

### 배열보다 큐를 사용하는 게 효과적인 이유: 
- 배열의 pop은 동적 배열 앞의 모든 요소들을 한 칸씩 당기므로 TC O(n)이다. => deque가 효율적 (연결리스트 포인터 이동/많은 삭제가 필요한 경우에 장점)
'''

class RecentCounter:
    def __init__(self):
        self.requests = deque()
        
    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)