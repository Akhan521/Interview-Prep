'''
Problem 1: Selective DNA Deletion
As a biologist, you are working on editing a long strand of DNA represented as a linked list of nucleotides. Each nucleotide in the sequence 
is represented as a node in the linked list, where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.

Given the head of the linked list dna_strand and two integers m and n, write a function edit_dna_sequence() that simulates the selective 
deletion of nucleotides in a DNA sequence. You will: - Start at the beginning of the DNA strand. - Retain the first m nucleotides from the 
current position. - Remove the next n nucleotides from the sequence. - Repeat the process until the end of the DNA strand is reached.

Return the head of the modified DNA sequence after removing the mentioned nucleotides.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has 
the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def edit_dna_sequence(dna_strand, m, n):
    pass
    
Example Usage:
Example 1 linked list before and after modification

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

Example Output:
1 -> 2 -> 6 -> 7 -> 11 -> 12
Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  
(1 -> 2) show in black nodes.
Delete the next (n = 3) nodes (3 -> 4 -> 5) show in red nodes.
Continue with the same procedure until reaching the tail of the Linked List.
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

def edit_dna_sequence(dna_strand, m, n):
    '''
    Plan:
    1. Initialize a pointer `current` to the head of the linked list.
    2. While `current` is not None:
        a. Retain the next m nodes by moving the `current` pointer m times.
        b. If `current` becomes None during this process, break the loop.
        c. Initialize a temporary pointer `temp` to `current.next`.
        d. Remove the next n nodes by moving the `temp` pointer n times.
        e. Link the last retained node to the node after the removed nodes.
        f. Move the `current` pointer to the next node after the removed nodes.
    '''
    current = dna_strand
    while current:
        # Retain m nodes:
        for _ in range(1, m):
            # If we don't have enough nodes to retain, return.
            if current is None:
                return dna_strand
            # Otherwise, move to the next node.
            current = current.next

        # If we reached the end of the list, return.
        if current is None:
            return dna_strand
        
        # Start removing n nodes:
        temp = current.next
        for _ in range(n):
            # If we don't have enough nodes to remove, break.
            if temp is None:
                break
            # Otherwise, move to the next node.
            temp = temp.next

        # Connect the last retained node to the node after the removed nodes.
        current.next = temp

        # Move current to the next node to continue the process.
        current = temp

    return dna_strand

dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))