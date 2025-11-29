'''
Problem 2: Expanding Flight Offerings
CodePath Airlines wants to expand their flight offerings so that for any airport they operate out of, it is possible to reach all other airports. 
They track their current flight offerings in an adjacency dictionary flights where each key is an airport i and flights[i] is an array indicating 
that there is a flight from destination i to each destination in flights[i]. Assume that if there is flight from airport i to airport j, the reverse 
is also true.

Given flights, return the minimum number of flights (edges) that need to be added such that there is flight path from each airport in flights to 
every other airport.

def min_flights_to_expand(flights):
    pass
    
Example Usage:
flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))

Example Output:
1
'''

def min_flights_to_expand(flights):
    '''
    Plan:
    1. Build an undirected graph from the adjacency dictionary.
    2. Initialize a visited set to keep track of visited airports.
    3. Use DFS to find connected components in the graph.
    4. The minimum number of flights needed to connect all components is (number of components - 1).
    '''
    def dfs(airport, visited):
        # Mark the current airport as visited.
        visited.add(airport)
        # Explore all connected airports.
        stack = [airport]
        while stack:
            current = stack.pop()
            for neighbor in flights.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    # Build an undirected graph and find connected components.
    graph = {}
    for airport in flights:
        if airport not in graph:
            graph[airport] = set()
        for dest in flights[airport]:
            if dest not in graph:
                graph[dest] = set()
            graph[airport].add(dest)
            graph[dest].add(airport)

    visited = set()
    components = 0

    for airport in graph:
        if airport not in visited:
            # Found a new connected component.
            dfs(airport, visited)
            components += 1

    # Minimum flights needed to connect all components is (components - 1).
    return components - 1
    
flights = {
    'JFK': ['LAX', 'SFO'],
    'LAX': ['JFK', 'SFO'],
    'SFO': ['JFK', 'LAX'],
    'ORD': ['ATL'],
    'ATL': ['ORD']
}

print(min_flights_to_expand(flights))

'''
- Time Complexity: O(V + E), where V is the number of airports (vertices) and E is the number of flights (edges). 
  We build the graph and then use DFS to explore all vertices and edges.
  
- Space Complexity: O(V + E) for storing the graph and visited set.
'''