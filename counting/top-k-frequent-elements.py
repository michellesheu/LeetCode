class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # Sort the keys of the dictionary based on their frequency values
        # Then take the first k elements
        return sorted(freq, key=freq.get, reverse=True)[:k]
