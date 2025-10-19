'''
Problem 4: Does it Cycle?
A variation of the two-pointer technique introduced earlier in the course is to have a slow and a fast pointer that increment at 
different rates. Given the head of a linked list, use the slow-fast pointer technique to write a function has_cycle() that returns 
True if the list has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer 
points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    pass
    
Example Usage:
Linked list with four nodes where fourth node points back to second node

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))

Example Output:
True
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))