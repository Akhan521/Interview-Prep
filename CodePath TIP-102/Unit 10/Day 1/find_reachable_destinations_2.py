'''
Problem 4: Finding All Reachable Destinations II
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a 
starting airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, 
and the corresponding value is a list of other destinations that are reachable through a direct flight.

Given a starting location start, write a function get_all_destinations() that uses Depth First Search (DFS) to return a list of all destinations 
that can be reached from start. The list should include both direct and connecting flights and should be ordered based on the order in which airports 
are visited in DFS.

def get_all_destinations(flights, start):
    pass
    
Example Usage:
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))

Example Output:
['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 
'New York']
['Helsinki', 'Cairo', 'Reykjavik', 'New York']
'''

def get_all_destinations(flights, start):
    '''
    Plan:
    1. Initialize a set to keep track of visited destinations and a list to store the order of reachable destinations.
    2. Define a recursive DFS function that:
        - Marks the current destination as visited and adds it to the reachable list.
        - Recursively visits all unvisited neighbors (destinations reachable by direct flight).
    3. Call the DFS function starting from the start location.
    '''
    visited = set()
    reachable = []

    def dfs(current):
        # Mark the current destination as visited and add to reachable list.    
        visited.add(current)
        reachable.append(current)

        # Visit all unvisited neighbors (destinations reachable by direct flight).
        for neighbor in flights.get(current, []):
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from the starting location.
    dfs(start)

    return reachable

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))