import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        print(num_freq)
        min_heap = []
        for num, freq in num_freq.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = [num for _, num in min_heap]
        return result