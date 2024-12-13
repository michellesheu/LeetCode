class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # index is frequency val is list of nums
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums).items()
        print(count)
        for num, freq in count:
            bucket[freq].append(num)
        flat_list = [item for sublist in bucket for item in sublist]
        print(bucket)
        print(bucket[::-1])
        return flat_list[::-1][:k]

            