class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  
        aMap = {}
        
        for i in range(len(strs)):
            key = [0]*26

            for j in range(len(strs[i])):
                key[ord(strs[i][j]) - ord('a')] += 1

            aTuple = tuple(key)

            if aTuple in aMap:
                aMap[aTuple].append(strs[i])
            else:
                aMap[aTuple] = [strs[i]]
        # print(aMap)
        return [list(l) for l in aMap.values()]
        # Need to convert the map values into  list before return
        


