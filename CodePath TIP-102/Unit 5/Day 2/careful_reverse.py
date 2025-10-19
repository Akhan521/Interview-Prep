'''
Problem 6: Careful Reverse
Given the head of a singly linked list and an integer k, reverse the first k elements of the linked list. Return the new head of 
the linked list. If k is larger than the length of the list, reverse the entire list.

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
        
def reverse_first_k(head, k):
	pass
    
Example Usage:
head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))

Example Output:
orange -> cherry -> apple -> peach -> pear
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

def reverse_first_k(head, k):
    '''
    Plan:
    1. Initialize three pointers: prev (None), current (head), and next_node (None).
    2. Use a counter to keep track of the number of nodes reversed.
    3. Iterate through the linked list, reversing the pointers of the first k nodes.
    4. If k is larger than the length of the list, reverse the entire list.
    5. After reversing, connect the last node of the reversed segment to the remaining part of the list.
    6. Return the new head of the linked list.
    '''
    # Edge case: if head is None or k <= 1, return head.
    if not head or k <= 1:
        return head
    
    prev, current, next_node = None, head, None
    count = 0

    # Reverse the first k nodes:
    while current and count < k:
        next_node = current.next  
        current.next = prev       # Reverse the link.
        prev = current            
        current = next_node       
        count += 1

    # If there are remaining nodes, connect the last node of the reversed segment to the rest of the list.
    # Here, head is now the last node of the reversed segment.
    if head:
        head.next = current

    # prev is the new head of the reversed segment.
    return prev

head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))