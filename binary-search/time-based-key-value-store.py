class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        if not arr:
            return ''
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] < timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid - 1
            else:
                return arr[mid][1]
        if arr[right][0] > timestamp:
            return ''
        return arr[right][1]