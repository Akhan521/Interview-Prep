'''
Problem 4: Super Sandwich
A regular at the deli has requested a new order made by merging two different sandwiches on the menu together. 
Given the heads of two linked lists sandwich_a and sandwich_b where each node in the lists contains a sandwich layer, 
write a recursive function merge_orders() that merges the two sandwiches together in the pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

Return the head of the merged sandwich.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe 
your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b)
    pass
    
Example Usage:
sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))

Example Output:
Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
Bacon -> Bread -> Lettuce -> Tomato
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    # Base case: if one of the sandwiches is empty, return the other sandwich.
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    
    # Recursive case: link the first layer of sandwich_a to the first layer of sandwich_b,
    # then recursively merge the rest of the layers.
    next_a = sandwich_a.next
    next_b = sandwich_b.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(next_a, next_b)

    return sandwich_a

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))