class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def findDifference(a, b):
            difference = 0
            for i in range(len(min(a, b))):
                if a[i] != b[i]:
                    difference += 1
            
            difference += abs(len(a) - len(b))
            return difference

        edges = defaultdict(list)
        n = len(wordList)

        seen = {}
        for word in wordList:
            seen[word] = True
        
        if not endWord in seen:
            return 0 

        for i in range(n): 
            for j in range(i + 1, n): 
                if findDifference(wordList[i], wordList[j]) == 1: 
                    edges[wordList[i]].append(wordList[j])
                    edges[wordList[j]].append(wordList[i])
            if not beginWord in seen and findDifference(wordList[i], beginWord) == 1:
                edges[beginWord].append(wordList[i])
                edges[wordList[i]].append(beginWord)

        # print(edges)

        queue = deque()
        queue.append([1, beginWord])
        seen = set()

        while queue: 
            length, next_word = queue.popleft()
            seen.add(next_word)
            if next_word == endWord: return length
            for neighbour in edges[next_word]:
                if not neighbour in seen: 
                    queue.append([length + 1, neighbour])
        
        return 0

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = defaultdict(list)
        n = len(wordList)

        seen = {}
        for word in wordList:
            seen[word] = True
        
        if not endWord in seen:
            return 0 

        for i in range(n): 
            word = wordList[i]
            for j in range(len(beginWord)):
                edges[word[:j] + '*' + word[j + 1:]].append(word)

        # print(edges)
        queue = deque()
        queue.append([1, beginWord])
        seen = set()

        while queue: 
            length, next_word = queue.popleft()
            seen.add(next_word)
            if next_word == endWord: return length
            for j in range(len(beginWord)):
                neighbours = edges[next_word[:j] + '*' + next_word[j + 1:]]
                for neighbour in neighbours:
                    if not neighbour in seen:
                        seen.add(neighbour)
                        queue.append([length + 1, neighbour])
        return 0

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def advanceQueue(queue, seen, other_seen):
            queue_size = len(queue)
            # print(queue_size)
            for _ in range(queue_size):
                length, next_word = queue.popleft()
                for j in range(len(beginWord)):
                    neighbours = edges[next_word[:j] + '*' + next_word[j + 1:]]
                    print(length, next_word, neighbours)
                    for neighbour in neighbours:
                        if neighbour in other_seen: 
                            return other_seen[neighbour] + length
                        if not neighbour in seen:
                            seen[neighbour] = length + 1
                            queue.append([length + 1, neighbour])
            return False
            
        edges = defaultdict(list)
        n = len(wordList)

        seen = {}
        for word in wordList:
            seen[word] = True
        
        if not endWord in seen:
            return 0 

        for i in range(n): 
            word = wordList[i]
            for j in range(len(beginWord)):
                edges[word[:j] + '*' + word[j + 1:]].append(word)

        # print(edges)
        queue, queue2 = deque(), deque()
        queue.append([1, beginWord])
        queue2.append([1, endWord])
        seen = {}
        seen[beginWord] = 1
        seen1 = {}
        seen1[endWord] = 1

        while queue and queue2: 
            # print(queue, queue2)
            if len(queue) <= len(queue2):
                res = advanceQueue(queue, seen, seen1)
            else: 
                res = advanceQueue(queue2, seen1, seen)
            if res: return res

        return 0
