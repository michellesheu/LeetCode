from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list of int nums, k number of top frequent
        # output: list of k most frequent nums
        # brute force: use a counter to get nums_freq and return only the k most frequent but that's O(n) n being len of nums to build counter and then O(k) to only keep the k most frequent which in total time complexity is just O(n) and O(n) space complexity?
        # better: use a heap bc it says top k lmao and use a min heap bc the smallest freq (idk if this is true? what can a min heap do again?) will be at root so o(1) retrieval and then remove those n-k times and return the list of k most freq elements
        # by default python uses min heap i forgot how to import heaps tho i think it's heapq
        # i forgot u can push tuples into a minheap and pop whenever the heapsize exceeds k so the smallest freq is always removed from the top ahhh and then it keeps the k elements with the highest frequencies
        heap = []
        num_freq = Counter(nums)
        for num, freq in num_freq.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
