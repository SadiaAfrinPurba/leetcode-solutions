from collections import defaultdict
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        online = set()
        min_heaps = defaultdict(list)
        groups = defaultdict(int)

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        # adj: defaultdict(<class 'list'>, {1: [2], 2: [1, 3], 3: [2], 4: [5], 5: [4]})

        
        def dfs(node, group_id):
            if node in online:
                return
            online.add(node)
            groups[node] = group_id
            heapq.heappush(min_heaps[group_id], node)

            for neighbor in adj[node]:
                dfs(neighbor, group_id)
        # group (node, group_id): defaultdict(<class 'int'>, {1: 1, 2: 1, 3: 1, 4: 4, 5: 4})
        # minheap: defaultdict(<class 'list'>, {1: [1, 2, 3], 4: [4, 5]})

        for idx in range(1, c+1):
            # build the graph connected component
            #
            dfs(node=idx, group_id=idx)
        
        res = []
        print(groups)

        for query_type, query_node in queries:
            if query_type == 1:
                if query_node in online:
                    res.append(query_node)
                    continue
                grp = groups[query_node]
                min_heap = min_heaps[grp]
                while min_heap and min_heap[0] not in online:
                    heapq.heappop(min_heap)
                if min_heap:
                    res.append(min_heap[0])
                else:
                    res.append(-1)
            else:
                online.discard(query_node)
        return res