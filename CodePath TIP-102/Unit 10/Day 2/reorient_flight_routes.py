'''
Problem 5: Reorient Flight Routes
There are n airports numbered from 0 to n - 1 and n - 1 direct flight routes between airports such that there is exactly one way to travel 
between any two airports (this network forms a tree). Last year, the aviation authority decided to orient the flight routes in one direction 
due to air traffic regulations.

Flight routes are represented by connections, where connections[i] = [airport_a, airport_b] represents a one-way flight route from airport 
airport_a to airport airport_b.

This year, there will be a major aviation event at the central hub (airport 0), and many flights need to reach this hub.

Your task is to reorient some flight routes so that every airport can send flights to airport 0. Return the minimum number of flight routes 
that need to be reoriented.

It is guaranteed that after the reordering, each airport will be able to send a flight to airport 0.

def min_reorient_flight_routes(n, connections):
    pass
    
Example Usage:
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

print(min_reorient_flight_routes(n, connections))

Example Output:
3

Explanation: 
- Initially, the flight routes are: 0 -> 1, 1 -> 3, 2 -> 3, 4 -> 0, 4 -> 5
- We need to reorient the routes [1, 3], [2, 3], and [4, 5] to ensure that every airport can send a flight to airport 0.
'''

def min_reorient_flight_routes(n, connections):
    '''
    General Idea:
    Convert the given one-way flight routes into an undirected graph representation. Then, perform DFS to explore all airports,
    counting the number of edges that are directed away from airport 0. Each such edge needs to be reoriented.

    Plan:
    1. Create an adjacency list to represent the undirected graph of connections.
    2. Use a set to keep track of the original directed edges for easy lookup.
    3. Implement a DFS function that traverses the graph, starting from airport 0.
        - Traverse the graph, skipping the parent node to avoid cycles.
        - If an edge is directed away from airport 0, increment the reorientation count.
        - Recursively call DFS for each connected airport.
    4. Return the total count of reoriented edges after the DFS completes.
    '''
    graph = {i: [] for i in range(n)}
    directed_edges = set()

    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
        directed_edges.add((a, b))

    def dfs(current, parent):
        nonlocal reorient_count
        # Explore all connected airports:
        for neighbor in graph[current]:
            # Skip the parent airport to avoid cycles
            if neighbor == parent:
                continue

            # If the edge is directed away from airport 0, it needs reorientation. 
            # An edge is directed away from airport 0 if it goes from current to neighbor because we are traversing from 0 outwards.
            if (current, neighbor) in directed_edges: 
                reorient_count += 1

            dfs(neighbor, current)

    reorient_count = 0
    # Start DFS from airport 0.
    dfs(0, -1)
    return reorient_count

n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

print(min_reorient_flight_routes(n, connections))