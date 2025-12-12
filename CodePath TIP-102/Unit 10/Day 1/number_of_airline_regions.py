'''
Problem 8: Number of Airline Regions
CodePath Airlines operates in different regions around the world. Some airports are connected directly with flights, while others are not. 
However, if airport a is connected directly to airport b, and airport b is connected directly to airport c, then airport a is indirectly 
connected to airport c.

An airline region is a group of directly or indirectly connected airports and no other airports outside of the group.

You are given an n x n matrix is_connected where is_connected[i][j] = 1 if CodePath Airlines offers a direct flight between airport i and airport j, 
and is_connected[i][j] = 0 otherwise.

Return the total number of airline regions operated by CodePath Airlines.

def num_airline_regions(is_connected):
    pass
    
Example Usage:
is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 

Example Output:
2
2
'''

def num_airline_regions(is_connected):
    '''
    Plan:
    1. Initialize a set to keep track of visited airports.
    2. Define a DFS function that marks all connected airports starting from a given airport.
    3. Iterate through each airport in the is_connected matrix.
    4. For each unvisited airport, perform a DFS to mark all connected airports and increment the region count.
    5. Return the total count of airline regions.
    '''
    n = len(is_connected)
    visited = set()
    region_count = 0

    def dfs(airport):
        # Mark the current airport as visited
        visited.add(airport)
        # Explore all connected airports
        for neighbor in range(n):
            if is_connected[airport][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    # Iterate through each airport
    for airport in range(n):
        if airport not in visited:
            # Start a new DFS for each unvisited airport (to find a new region)
            dfs(airport)
            region_count += 1

    return region_count

is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 