class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([startGene])
        visited = set([startGene])
        ans = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene: return ans
                for i in range(len(gene)):
                    for j in ['A','C','G','T']:
                        newGene = gene[:i] + j + gene[i+1:]
                        if newGene in bank and newGene not in visited:
                            queue.append(newGene)
                            visited.add(newGene)
            ans += 1
        return -1