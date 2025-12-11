'''
Problem 7: Number of Flights
You are a travel planner and have an adjacency matrix flights with n airports labeled 0 to n-1 where flights[i][j] indicates CodePath Airlines 
offers a flight from airport i to airport j. You are planning a trip for a client and want to know the minimum number of flights (edges) it will 
take to travel from airport start to their final destination airport destination on CodePath Airlines.

Return the minimum number of flights needed to travel from airport i to airport j. If it is not possible to fly from airport i to airport j, return -1.

def counting_flights(flights, i, j):
    pass
    
# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))

Example Output:
1 
Example 1 Explanation: Flight path: 0 -> 2
3
Example 2 Explanation: Flight path 0 -> 2 -> 3 -> 4
-1
Explanation: Cannot fly from Airport 4 to Airport 0
'''

from collections import deque
def counting_flights(flights, start, destination):
    '''
    Plan:
    1. Use BFS to find the shortest path (minimum number of flights) from start to destination.
    2. If the destination is reached, return the number of flights.
    3. If the queue is exhausted and the destination is not reached, return -1.
    Note: BFS is used here because it explores all nodes level by level, ensuring the shortest path in an unweighted graph.
    '''
    n = len(flights)

    # Edge case: If start is the same as destination, no flights are needed
    if start == destination:
        return 0
    
    # Initialize data structures for BFS
    visited = set([start])
    queue = deque([(start, 0)]) # (current_airport, number_of_flights)

    # BFS loop
    while queue:
        current_airport, num_flights = queue.popleft()

        # Check all possible flights from the current airport
        for next_airport in range(n):
            if flights[current_airport][next_airport] == 1 and next_airport not in visited:
                # If the destination is reached, return the number of flights
                if next_airport == destination:
                    return num_flights + 1
                # Otherwise, add the next airport to the queue and mark it as visited
                visited.add(next_airport)
                queue.append((next_airport, num_flights + 1))

    # If the queue is exhausted and the destination is not reached, return -1
    return -1

flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))