class Solution:
    def kClosest(self, P, k):
        squared_distance= lambda x, y : x*x + y*y
        for p in P:
            p.insert(0, squared_distance(p[0], p[1]))
        heapify(P)
        return [heappop(P)[1:] for i in range(k)]