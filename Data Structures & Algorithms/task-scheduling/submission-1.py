class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        count = Counter(tasks)

        maxHeap = []
        for c in count.values():
            maxHeap.append(-c)

        heapq.heapify(maxHeap)

        time = 0

        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
                #if nothing in maxheap, jump to the next time that's the cooldown is done
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                #only add to maxheap if the cooldown is complete
                heapq.heappush(maxHeap, q.popleft()[0])
        return time 