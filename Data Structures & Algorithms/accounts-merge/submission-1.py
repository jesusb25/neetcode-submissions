class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        emailMap = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailMap:
                    union(i, emailMap[email])
                emailMap[email] = i

        merged = collections.defaultdict(set)
        for i in range(len(accounts)):
            root = find(i)
            merged[root].update(accounts[i][1:])

        result = []
        for i in merged:
            result.append([accounts[i][0]] + sorted(list(merged[i])))
        return result