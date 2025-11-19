'''
Problem 1: There and Back
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of 
a different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]. 
Write a function bidirectional_flights() that returns True if for every flight from a destination i to a destination j there also exists a flight 
from destination j to destination i. Return False otherwise.

def bidirectional_flights(flights):
    pass
    
Example Usage:
Example 1: flights1

'flights1' graph diagram

Example 2: flights2'flights2' graph diagram

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

Example Output:
True
False
'''

def bidirectional_flights(flights):
    '''
    Plan:
    1. Iterate through each destination in the flights adjacency list.
    2. For each destination, check its list of connected destinations.
    3. For each connected destination, verify that the original destination is also listed in its connections.
    4. If any connection is found to be unidirectional, return False.
    '''
    n = len(flights)
    # Check each destination:
    for i in range(n):
        # Check each connection from destination i:
        for j in flights[i]:
            if i not in flights[j]:
                return False
            
    return True

flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))