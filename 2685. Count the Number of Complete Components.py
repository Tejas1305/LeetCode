class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """     
     
     # Step 1: Build the graph using an adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: DFS to find connected components
        visited = [False] * n
        def dfs(node):
            stack = [node]
            component_nodes = []
            component_edges = 0
            while stack:
                current = stack.pop()
                if not visited[current]:
                    visited[current] = True
                    component_nodes.append(current)
                    # Count the edges for the component
                    for neighbor in adj[current]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
                        component_edges += 1
            # Each edge is counted twice (undirected), so divide by 2
            component_edges //= 2
            return component_nodes, component_edges
        
        # Step 3: Count complete components
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                nodes, edges_in_component = dfs(i)
                # Check if this component is complete
                k = len(nodes)
                if edges_in_component == k * (k - 1) // 2:
                    complete_components += 1
        
        return complete_components