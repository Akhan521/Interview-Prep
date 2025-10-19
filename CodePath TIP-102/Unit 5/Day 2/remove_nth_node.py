'''
Problem 5: Remove Nth Node From End of List
Given the head of a linked list and an integer n, write a function remove_nth_from_end() that removes the nth node from 
the end of the list. The function should return the head of the modified list.

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

def remove_nth_from_end(head, n):
    pass
    
Example Usage:
head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))

Example Output:
apple -> cherry -> orange -> pear
Rainbow Trout

Example 3 Explanation: The last example returns an empty list.
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

def remove_nth_from_end(head, n):
    '''
    Plan:
    1. Initialize a dummy node that points to the head of the list.
    2. Set two pointers, first and second, both starting at the dummy node.
    3. Move the first pointer n+1 steps ahead to create a gap of n nodes between first and second.
    4. Move both pointers one step at a time until the first pointer reaches the end of the list.
    5. The second pointer will now be at the node just before the one we want to remove. Adjust its next pointer to skip the nth node from the end.
    6. Return the next of the dummy node, which is the new head of the modified list.
    '''
    dummy = Node(value=0, next=head)
    first, second = dummy, dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    # Remove the nth node from the end (second.next)
    second.next = second.next.next

    return dummy.next

head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))