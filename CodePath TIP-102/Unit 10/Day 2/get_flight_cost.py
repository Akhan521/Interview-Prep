'''
Problem 1: Get Flight Cost
You are given an adjacency dictionary flights where for any location source, flights[source] is a list of tuples in the form (destination, cost) 
indicating that there exists a flight from source to destination at ticket price cost.

Given a starting location start and a final destination dest return the total cost of flying from start to dest. If it is not possible to fly from 
start to dest, return -1. If there are multiple possible paths from start to dest, return any of the possible answers.

def calculate_cost(flights, start, dest):
    pass
    
Example Usage:
flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW': 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))

Example Output:
550
Explanation: There is a path from LAX -> SFO -> ORD -> MIA with ticket prices 50 + 100 + 400 = 550
960 would also be an acceptable answer following the path from LAX -> SFO -> ERW -> ORD -> MIA
'''

def calculate_cost(flights, start, dest):
    # A set to keep track of visited locations to avoid cycles.
    visited = set()

    def dfs(current, total_cost):
        # If we reach the destination, return the total cost.
        if current == dest:
            return total_cost
        
        # Mark the current location as visited.
        visited.add(current)

        # Explore all possible flights from the current location.
        for neighbor, cost in flights.get(current, []):
            if neighbor not in visited:
                # Recursively search from the neighbor location.
                result = dfs(neighbor, total_cost + cost)
                if result != -1:
                    return result
                
        # Backtrack: unmark the current location as visited.
        visited.remove(current)

        return -1  # No valid path found from current location.

    return dfs(start, 0)

flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))