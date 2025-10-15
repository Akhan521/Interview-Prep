'''
Problem 8: Restocking the Lake
Imagine that Animal Crossing is still using a linked list to represent the order fish will appear to a player who is fishing! 
The head of the list represents the next fish that a player will catch if they keep fishing.

Write a function restock() that accepts the head of a linked list and a string new_fish, and adds a Node with the fish_name new_fish 
to the end of the list. Return the head of the modified list.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided 
for testing purposes.

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):
    pass
    
Example Usage:
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))

Example Output:
Carp -> Dace -> Cherry Salmon -> Rainbow Trout
'''

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def restock(head, new_fish):
    new_node = Node(new_fish)
    
    # If our list is empty, return the new node as the head.
    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next

    # Link the new node at the end of the list.
    current.next = new_node
    return head

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))