'''
Problem 3: Finding All Reachable Destinations
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting 
airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, and the 
corresponding value is a list of other destinations that are reachable through a direct flight.

Given a starting location start, return a list of all destinations reachable from the start location either through a direct flight or connecting 
flights with layovers. The list should be provided in ascending order by number of layovers required.

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
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))

Example Output:
['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
'Reykjavik']
['Helsinki', 'Cairo', 'New York', 'Reykjavik']
'''

from collections import deque
def get_all_destinations(flights, start):
    '''
    General Idea:
    Use a breadth-first search (BFS) approach to explore all reachable destinations from the starting airport.

    Plan:
    1. Initialize a queue with the starting location and a set to keep track of visited destinations.
    2. While the queue is not empty:
        - Dequeue the front element and mark it as visited.
        - Enqueue all unvisited destinations that can be reached directly from the current destination.
    3. After the BFS completes, return the list of visited destinations.
    '''
    visited = set()
    queue = deque([start])
    reachable = []

    while queue:

        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            reachable.append(current)

            for neighbor in flights.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return reachable

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))




