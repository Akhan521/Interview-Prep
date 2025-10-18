'''
Problem 3: Delete Duplicates in a Linked List
Given the head of a sorted linked list, delete all elements that occur more than once in the list (not just the duplicates). 
The resulting list should maintain sorted order. Return the head of the linked list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    pass
    
Example Usage:
head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

Example Output:
1 -> 2 -> 4 -> 5
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

def delete_dupes(head):
    # Use a dummy node to handle edge cases easily.
    dummy = Node(0)
    dummy.next = head

    # We'll use two pointers: prev (last node before the duplicates) and current (to traverse the list).
    prev = dummy
    current = head

    while current:
        # Move current forward while there are duplicates.
        while current.next and current.value == current.next.value:
            current = current.next

        # If prev's next is still current, no duplicates were found in between.
        if prev.next == current:
            prev = prev.next
        else:
            # Skip all duplicates.
            prev.next = current.next

        # Move current forward.
        current = current.next

    return dummy.next

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))