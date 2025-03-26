MOD = 10**9+7

class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(list)
        for u,v,time in roads:
            graph[u].append((v,time))
            graph[v].append((u,time))

        min_time = [float('inf')]*n
        ways = [0]*n
        min_time[0] = 0
        ways[0]= 1

        pq = [(0,0)]

        while pq:
            curr_time, node = heapq.heappop(pq)

            if node == n-1 and curr_time>min_time[n-1]:
                break

            if curr_time>min_time[node]:
                continue

            for neighbour, travel_time in graph[node]:
                new_time = curr_time+travel_time

                if new_time< min_time[neighbour]:
                    min_time[neighbour] = new_time
                    ways[neighbour] = ways[node]
                    heapq.heappush(pq,(new_time, neighbour))

                elif new_time == min_time[neighbour]:
                    ways[neighbour] = (ways[neighbour]+ways[node])%MOD

        return ways[n-1]%MOD