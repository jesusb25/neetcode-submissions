class UnionFind:
    def __init__(self, n):
        # parents [num] parents of each self
        self.par = [i for i in range(n)]
        # rank order to keep parents
        self.rank = [1] * n

    # find parent
    def find(self, x):
        # find parents iteratively
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        # if same parents already in one group
        if p1 == p2:
            return False
        
        # share parents of higher rank, increase rank
        # union
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        # email -> index of acc
        emailToAcc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                # if email already mapped, union
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        # index of acc -> list of emails
        accToEmails = defaultdict(list)
        for e, i in emailToAcc.items():
            # parent of account
            leader = uf.find(i)
            # set account parent to group
            # parent to all assocaited emails
            accToEmails[leader].append(e)

        res = []
        for i, emails in accToEmails.items():
            name = accounts[i][0]
            res.append([name] + sorted(accToEmails[i]))
        return res