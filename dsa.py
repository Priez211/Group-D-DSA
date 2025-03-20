# # adjacency matrix for 7 cities
# Rows and columns represent cities 1 to 7
# Distance from city i to city j is stored in matrix[i][j]
# Assume distances are symmetric (bidirectional)

import numpy as np
def create_graph():
    """Creates the adjacency matrix representation of the TSP graph."""
    return [
        [0, 12, 10, 8, 12, float('inf'), float('inf')],
        [12, 0, float('inf'), 3, float('inf'), 9, 11],
        [10, float('inf'), 0, float('inf'), 6, 7, float('inf')],
        [8, 3, float('inf'), 0, float('inf'), 9, float('inf')],
        [12, float('inf'), 6, float('inf'), 0, float('inf'), 9],
        [float('inf'), 9, 7, 9, float('inf'), 0, 10],
        [float('inf'), 11, float('inf'), float('inf'), 9, 10, 0]
    ]
print(create_graph())

## Using dynamic programming(Held-Karp algorithm)vto solve TSP
def tsp_dynamic_programming(graph):
    """Solves TSP using Dynamic Programming (Held-Karp algorithm)."""
    n = len(graph)
    all_sets = (1 << n) - 1
    
    # DP table to store min cost of reaching a subset of cities
    memo = {}
    
    def visit(city, visited):
        """Recursively computes the shortest path visiting all cities."""
        if visited == all_sets:
            if graph[city][0]==float('inf'): 
                # no valid return path
                return float('inf'), []
            return graph[city][0], [city, 0]
        
        if (city, visited) in memo:
            return memo[(city, visited)]
        
        min_cost = float('inf')
        best_route = None
        for next_city in range(n):
            if visited & (1 << next_city) == 0 and graph[city][next_city]!=float('inf'):  # If not visited and path exists
                cost, route = visit(next_city, visited | (1 << next_city))
                total_cost = graph[city][next_city] + cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_route = [city]+route
        
        memo[(city, visited)] = (min_cost, best_route if best_route else [])
        return memo[(city, visited)]
    
    min_cost, route = visit(0, 1)  # Start at city 0 (index 0)
    return min_cost, route if route else ["No valid route found"]
graph=create_graph()
min_cost, route=tsp_dynamic_programming(graph)
print(f"Optimal TSP route distance (DP):{min_cost}")
print(f"Optimal TSP route:{route}")




    







