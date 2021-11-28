class Solution:
    def allPathsSourceTarget(self, graph):
        res=[]
        end=len(graph)-1
        path=[0]
        def dfs(node):
            if node==end:
                res.append(path.copy())
                return
            for next in graph[node]:
                path.append(next)
                dfs(next)
                path.pop()
        dfs(0)
        return res