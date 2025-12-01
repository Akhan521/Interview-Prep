'''
Problem 4: Pilot Training
You are applying to become a pilot for CodePath Airlines, and you must complete a series of flight training courses. There are a total of 
num_courses flight courses you have to take, labeled from 0 to num_courses - 1. Some courses have prerequisites that must be completed before you 
can take the next one.

You are given an array flight_prerequisites where flight_prerequisites[i] = [a, b] indicates that you must complete course b first in order to 
take course a.

For example, the pair ["Advanced Maneuvers", "Basic Navigation"] indicates that to take "Advanced Maneuvers", you must first complete "Basic Navigation".

Return True if it is possible to complete all flight training courses. Otherwise, return False.

def can_complete_flight_training(num_courses, flight_prerequisites):
    pass
    
Example Usage:
flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))

Example Output:
True
Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, you must first complete *Basic Navigation*. This is possible.
False
Example 1 Explanation: There are 2 flight training courses. To take *Advanced Maneuvers*, you must first complete *Basic Navigation*, 
but to take *Basic Navigation*, you must first complete *Advanced Maneuvers*. This creates a cycle, making it impossible to complete all courses.
'''

def can_complete_flight_training(num_courses, flight_prerequisites):
    '''
    General Approach:
    We can represent the flight training courses and their prerequisites as a directed graph, where each course is a node and each prerequisite
    relationship is a directed edge. To determine if it's possible to complete all courses, we need to check if the directed graph contains any cycles.
    If there are cycles, it means there are circular dependencies among the courses, making it impossible to complete all of them. We can use DFS!

    Steps:
    1. Build an adjacency list to represent the graph.
    2. Initialize a visited array to keep track of visited nodes and a recursion stack to track the nodes in the current path.
    3. Define a recursive DFS function that checks for cycles.
        - If a node is already in the recursion stack, we have found a cycle, so we return False.
        - If a node has been visited and is not in the recursion stack, we return True.
        - Mark the node as visited and add it to the recursion stack.
        - Recursively visit all neighbors of the node.
        - After visiting all neighbors, remove the node from the recursion stack.
            -> This is because we are done exploring all paths from this node.
            -> If we don't remove it, we might incorrectly detect a cycle in future DFS calls.
    4. Iterate through all courses and perform DFS from each unvisited node.
    5. If we complete the DFS without finding any cycles, return True.
    '''
    # Step 1: Build the adjacency list
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in flight_prerequisites:
        graph[prereq].append(course)

    # Step 2: Initialize visited set and recursion stack
    visited = [False] * num_courses
    rec_stack = [False] * num_courses

    def dfs(course):
        # If the node is in the recursion stack, we found a cycle, so return False.
        if rec_stack[course]:
            return False
        
        # If the node has been visited and is not in the recursion stack, return True.
        if visited[course]:
            return True # No cycle found from this node.
        
        # Mark the node as visited and add it to the recursion stack.
        visited[course] = True
        rec_stack[course] = True

        # Recursively visit all neighbors of the node.
        for neighbor in graph[course]:
            # If a cycle is found in any neighbor, return False.
            if not dfs(neighbor):
                return False
            
        # Remove the node from the recursion stack after exploring all neighbors.
        rec_stack[course] = False

        return True # No cycle found from this node.
    
    # Step 4: Iterate through all courses and perform DFS from each unvisited node.
    for course in range(num_courses):
        if not visited[course]:
            # If there is a cycle found from this course, return False.
            if not dfs(course):
                return False # Cycle detected, cannot complete all courses.
            
    return True # No cycles detected, can complete all courses.

flight_prerequisites_1 = [['Advanced Maneuvers', 'Basic Navigation']]
flight_prerequisites_2 = [['Advanced Maneuvers', 'Basic Navigation'], ['Basic Navigation', 'Advanced Maneuvers']]

print(can_complete_flight_training(2, flight_prerequisites_1))
print(can_complete_flight_training(2, flight_prerequisites_2))