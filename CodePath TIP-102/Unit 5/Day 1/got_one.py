'''
Problem 6: Got One!
Imagine that behind the scenes, Animal Crossing uses a linked list to represent the order fish will appear to a player who is 
fishing in the river. The head of the list represents the next fish that a player will catch if they keep fishing.

Write a function catch_fish() that accepts the head of a list. The function should:

Print the name of the fish in the head node using the format "I caught a <fish name>!".
Remove the first node in the list.
The function should return the new head of the list. If the list is empty, print "Aw! Better luck next time!" and return None.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the list data has also been provided for testing purposes.

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    pass
    
Example Usage:
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))

Example Output:
Carp -> Dace -> Cherry Salmon
I caught a Carp!
Dace -> Cherry Salmon
Aw! Better luck next time!
None
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

def catch_fish(head):
    if head is None:
        print("Aw! Better luck next time!")
        return None
    print(f"I caught a {head.fish_name}!")
    return head.next

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))