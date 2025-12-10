'''
Problem 6: Finding Itinerary II
If you implemented find_itinerary() in the previous problem without using Depth First Search, solve it using DFS. If you solved it using DFS, 
try solving it using an alternative approach.

def find_itinerary(boarding_passes):
    pass
    
Example Usage:
boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))

Example Output:
['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
['LHR', 'DFW', 'JFK', 'LAX', 'DXB']
'''

from collections import defaultdict
def find_itinerary(boarding_passes):
    '''
    Plan:
    1) Create an adjacency list `flights` to represent the directed graph. The key is the departure airport, and the value is a list of destination airports.
    2) Sort the destination airports for each departure in reverse lexicographical order (so we can pop elements in correct order).
    3) Define a recursive DFS function `dfs(airport)` that visits all destinations of `airport`.
        a) Pop each destination from the adjacency list and recursively call `dfs` for that destination.
        b) Once all destinations are visited, append the current airport to the result list.
    4) Start DFS from the starting airport (first departure).
    5) Reverse the result list to obtain the correct itinerary.
    '''
    # Step 1: Create the adjacency list
    flights = defaultdict(list)

    # Step 2: Populate the adjacency list
    for departure, arrival in boarding_passes:
        flights[departure].append(arrival)

    # We sort the destinations in reverse order for correct popping
    for departure in flights:
        flights[departure].sort(reverse=True)

    # Step 3: Perform DFS and build the itinerary
    result = []

    def dfs(airport):
        # Visit all the destinations for the current airport
        while flights[airport]:
            next_destination = flights[airport].pop()
            dfs(next_destination)
        
        # Append the airport to the result after visiting all its destinations
        result.append(airport)

    # Step 4: Start DFS from the starting airport
    start_airport = boarding_passes[0][0] # Assuming the first departure is the starting point
    dfs(start_airport)

    # Step 5: Reverse the result to get the correct itinerary
    return result[::-1]

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))

'''
Time Complexity: O(E log E), where E is the number of edges (flights). Sorting the destinations takes O(E log E), and DFS visits each edge exactly once.
Space Complexity: O(E + V), where E is the number of edges and V is the number of vertices (airports), for storing the adjacency list and result list.
'''

