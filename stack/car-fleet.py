class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev_t = None
        n = 0
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            t = dist / vel
            if not prev_t or t > prev_t:
                prev_t = t
                n += 1
        return n
        