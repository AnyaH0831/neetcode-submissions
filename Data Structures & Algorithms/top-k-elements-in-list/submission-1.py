class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        aMap = {}
        freq = [[] for i in range(len(nums) + 1)]
        # print(freq)

        for num in nums: 
            aMap[num] = 1 + aMap.get(num, 0)
        for n, c in aMap.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result