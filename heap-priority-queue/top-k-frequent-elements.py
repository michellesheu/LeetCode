class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort O(n) time complexity 
        # store nested list of size len(nums) + 1 
        # length of list is n + 1 bc at most n frequent elements, 0-n
        # each index represents 0-n frequency, values stored in nested list are the elements of that frequency
        # iterate through freq_map to create bucket arr
        # iterate thru bucket_elems reversed from most freq to least freq, add elem in that bucket to output list until len of list is k then return output
        output = []
        n = len(nums)
        bucket_elems = [[] for _ in range(n + 1)]
        # print(f"{bucket_elems=}")
        freq_map = Counter(nums)
        # print(f"{freq_map=}")
        for num,count in freq_map.items():
            # print(f"---{bucket_elems=}---")
            # print(f"{count=} {bucket_elems[count]=}")
            bucket_elems[count].append(num)
            # print(f"{count=} {bucket_elems[count]=}")
            # print(f"---{bucket_elems=}---")
        print(f"{bucket_elems=}")
        for bucket in reversed(bucket_elems):
            for elem in bucket:
                # print(f'{elem=}')
                output.append(elem)
                # print(f'{output=}')
                # print(f'{len(output)=}')
                if len(output) == k:
                    return output


