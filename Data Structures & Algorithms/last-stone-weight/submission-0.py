class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq

        max_heap = []
        for stone in stones:

            heapq.heappush(max_heap, stone*(-1))

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x= -heapq.heappop(max_heap)
            

            if x == y:
                continue
            
            if x < y:
                heapq.heappush(max_heap, -(y-x))

        if len(max_heap) == 0:
            return 0
        else:
            return -heapq.heappop(max_heap)