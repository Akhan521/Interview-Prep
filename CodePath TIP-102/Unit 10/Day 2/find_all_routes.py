'''
Problem 6: Find All Flight Routes
You are given a flight network represented as a directed acyclic graph (DAG) with n airports, labeled from 0 to n - 1. Your goal is to find 
all possible flight paths from airport 0 (the starting point) to airport n - 1 (the final destination) and return them in any order.

The flight network is given as follows: flight_routes[i] is a list of all airports you can fly to directly from airport i (i.e., there is a 
one-way flight from airport i to airport flight_routes[i][j]).

Write a function that returns all possible flight paths from airport 0 to airport n - 1.

def find_all_flight_routes(flight_routes):
    pass
    
Example Usage 1:
flight_routes_1 = [[1, 2], [3], [3], []]

print(find_all_flight_routes(flight_routes_1))

Example Output 1:

[[0, 1, 3], [0, 2, 3]]
Explanation: 
- There are two possible paths from airport 0 to airport 3.
- The first path is: 0 -> 1 -> 3
- The second path is: 0 -> 2 -> 3

Example Usage 2:
flight_routes_2 = [[4,3,1],[3,2,4],[3],[4],[]]

print(find_all_flight_routes(flight_routes_2))
Example Output 2:

[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
'''

def find_all_flight_routes(flight_routes):
    '''
    Plan:
    1. Use Depth-First Search (DFS) to explore all possible paths from the starting airport (0) to the final destination (n-1).
    2. Keep a result list to store all the valid paths and a current path list to keep track of the current path being explored.
    3. When the final destination is reached, add the current path to the result list.
    4. Backtrack by removing the last airport from the current path list to explore other possible paths.
    '''
    result = []
    path = []

    def dfs(current_airport):
        path.append(current_airport)

        # If the current airport is the final destination, add the current path to the result list
        if current_airport == len(flight_routes) - 1:
            result.append(path.copy())
        else:
            # Recursively explore all the airports from the current airport
            for next_airport in flight_routes[current_airport]:
                dfs(next_airport)

        # Backtrack by removing the last airport from the current path list
        path.pop()

    # Start the DFS from the starting airport (0)
    dfs(0)

    return result

flight_routes_1 = [[1, 2], [3], [3], []]

print(find_all_flight_routes(flight_routes_1))

flight_routes_2 = [[4,3,1],[3,2,4],[3],[4],[]]

print(find_all_flight_routes(flight_routes_2))