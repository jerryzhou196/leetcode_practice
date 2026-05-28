class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        groups = []
        hand = sorted(hand)
        c = Counter(hand)

        for num in hand: 
            if num in c: 
                for i in range(groupSize):
                    if num + i not in c: 
                        return False
                    c[num + i] -= 1
                    if c[num + i] == 0: del c[num + i]
            # print(c)
        
        return True

 class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        groups = []
        hand = sorted(hand)
        c = Counter(hand)
        open_groups = 0
        last_card = -1
        queue = deque()
        
        for c, count in c.items(): 
            if open_groups > count or (open_groups > 0 and c != last_card + 1): return False 
            
            queue.append(count - open_groups)
            open_groups += count - open_groups
            
            if len(queue) == groupSize: 
                open_groups -= queue.popleft()

            last_card = c
            # print(count, open_groups, queue)
        
        return open_groups == 0 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        
        for num in hand:  
            # print(c)
            curr = num 
            if curr in c:
                while curr - 1 in c: 
                    curr -= 1
                # print('curr', curr, num, curr - 1 in c)
                
                while c[num]:  
                    while curr in c: 
                        # print(c[curr], curr)
                        for i in range(groupSize): 
                            if not curr + i in c: return False
                            c[curr + i] -= 1
                            if c[curr + i] == 0: 
                                del c[curr + i]
                    curr += 1
        # print(c)
        return len(c) == 0

    
        
