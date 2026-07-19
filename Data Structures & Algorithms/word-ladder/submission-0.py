class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord==endWord or endWord not in wordList:
            return 0
        wordList.append(beginWord)
        mapper=defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern=w[:i]+'*'+w[i+1:]
                mapper[pattern].append(w)
        visited=set()
        visited.add(beginWord)
        q=deque()
        q.append(beginWord)
        res=1
        while q:
            for i in range(len(q)):
                tmp=q.popleft()
                if tmp==endWord:
                    return res
                for i in range(len(tmp)):
                    pattern=tmp[:i]+'*'+tmp[i+1:] # we are getting the pattern of first word so we can traverse to other words
                    for x in mapper[pattern]:# we got all the neigh of hit->*it->git for eaxmple as we insert and remove at same time
                        if x not in visited:
                            visited.add(x)
                            q.append(x)
            res+=1
        return 0

