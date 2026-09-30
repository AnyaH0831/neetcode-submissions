from collections import deque
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        l = 0
        minOp = float('inf')
        for r in range(k,len(blocks)+1):
            # print(blocks[l:r])
            wCount = blocks[l:r].count("W")

            if wCount < minOp:
                minOp = wCount
            
            l += 1

        return minOp
            
            
