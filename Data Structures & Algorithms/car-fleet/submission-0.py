class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []

        for i in range(len(position)):
            pairs += [[position[i], speed[i]]]

        pairs.sort(reverse=True)

        # print(pairs)

        stack = []
        for i in range(len(pairs)):

            time = (target - pairs[i][0]) / pairs[i][1]

            if i == 0:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)

