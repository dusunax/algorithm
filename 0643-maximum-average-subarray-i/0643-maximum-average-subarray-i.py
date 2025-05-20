'''
## constaint
- integer array nums, integer k
- k length of subarrys => do sliding window of size k

## approach
- if checking subarrays one by one => (O(n * k))
- sliding wndow, keep the max values.

## sudo
window_sum = 첫 번쨰 윈도우(k 길이)의 합
max_sum = window_sum으로 초기화

for i를 k부터 len(n)까지
    window_sum에 i-k 번째 값을 빼고 i번째 값을 더함 (윈도우를 오른쪽으로 한 칸 이동)
    max()로 max_sum과 window_sum과 비교해서 업데이트

return 최대 합의 평균값 반환
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k