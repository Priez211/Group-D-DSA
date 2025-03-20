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






