"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi,
and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the
city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Example 1:

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.


Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
"""

# NOTE: Isolated nodes are possible in this setup.

from collections import deque
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        isolated_cities = self.find_isolates(n, edges)
        if isolated_cities:
            return isolated_cities.pop()
        target_city = 0
        min_paths = n
        adj_list = self.edge_list_to_adjacency_list(edges)
        for i in range(n):
            short_paths = self.dijkstra(adj_list, i)
            for x in list(short_paths.keys()):
                if short_paths[x] > distanceThreshold:
                    del short_paths[x]
            del short_paths[i]
            if len(short_paths) <= min_paths:
                min_paths = len(short_paths)
                target_city = i

        return target_city

    def edge_list_to_adjacency_list(self, edge_list):
        adj_list = {}
        for (src, dest, weight) in edge_list:
            if src not in adj_list:
                adj_list[src] = {}
            if dest not in adj_list:
                adj_list[dest] = {}

            adj_list[src][dest] = weight
            adj_list[dest][src] = weight

        return adj_list

    def dijkstra(self, adj_list, start):
        import heapq
        distances = {node: float('inf') for node in adj_list}
        distances[start] = 0

        # Priority queue to track nodes and current shortest distance
        priority_queue = [(0, start)]

        while priority_queue:
            # Pop the node with the smallest distance from the priority queue
            current_distance, current_node = heapq.heappop(priority_queue)

            # Skip if a shorter distance to current_node is already found
            if current_distance > distances[current_node]:
                continue

            # Explore neighbors and update distances if a shorter path is found
            for neighbor, weight in adj_list[current_node].items():
                distance = current_distance + weight

                # If shorter path to neighbor is found, update distance and push to queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def find_isolates(self, n, edge_list):
        isolated = []
        for i in range(n):
            isolated.append(i)
            for x in edge_list:
                if x[0] == i or x[1] == i:
                    isolated.pop()
                    break
        return isolated


if __name__ == "__main__":
    s = Solution()

    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold = 4
    print(s.findTheCity(n, edges, distanceThreshold))

    n = 5
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    distanceThreshold = 2
    print(s.findTheCity(n, edges, distanceThreshold))

    n = 5
    edges = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
    distanceThreshold = 417
    print(s.findTheCity(n, edges, distanceThreshold))
