'''
Problem 3: Get Flight Itinerary
Given an adjacency dictionary of flights flights where each key is an airport i and flights[i] is an array indicating that there is a flight 
from destination i to each destination in flights[i], return an array with the flight path from a given source location to a given destination location.

If there are multiple flight paths from the source to destination, return any flight path.

def get_itinerary(flights, source, destination):
    pass
    
Example Usage:
flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))

Example Output:
['LAX', 'SFO', 'ORD', 'MIA']
Explanation: ['LAX', 'SFO', 'ERW', 'ORD', 'MIA'] is also a valid answer
'''

def get_itinerary(flights, source, destination):
    '''
    Plan:
    1. Define a recursive DFS function to explore paths from source to destination.
        - Track the current node and the path taken so far.
    2. If the current node is the destination, return the path.
    3. If the current node has been visited, return None to avoid cycles.
    4. For each neighbor of the current node, attempt to extend the path recursively.
        - If a valid path is found, return it.
        - If no valid path is found, backtrack and try the next neighbor.
        - Make sure to avoid cycles by keeping track of visited nodes.
    5. Start the DFS from the source airport.
    '''
    visited = set() # To keep track of visited airports to avoid cycles

    def dfs(current, path):
        # If we reached the destination, return the current path.
        if current == destination:
            return path
        
        # If the current airport has been visited, return None to avoid cycles.
        if current in visited:
            return None
        
        visited.add(current)  # Mark the current airport as visited
        for neighbor in flights.get(current, []):
            result = dfs(neighbor, path + [neighbor])
            if result:
                return result
            
        return None  # No valid path found from this airport
    
    return dfs(source, [source])

flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))
    
