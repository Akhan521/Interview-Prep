'''
Problem 5: Group Animals by Habitat
You are managing a wildlife sanctuary where animals of the same species need to be grouped together by their habitats. 
Given a string habitats representing the sequence of animals, where each character corresponds to a particular species, 
you need to partition the string into as many contiguous groups as possible, ensuring that each species appears in at most one group.

The order of species in the resultant sequence must remain the same as in the input string habitats.

Return a list of integers representing the size of these habitat groups.

def group_animals_by_habitat(habitats):
  pass
  
Example Usage:
print(group_animals_by_habitat("ababcbacadefegdehijhklij")) 
print(group_animals_by_habitat("eccbbbbdec"))

Example Output:
[9,7,8]
[10]
'''

'''
Approach:
1. Record the last occurrence of each species in the habitats string.
2. Iterate through the string, maintaining the current group's end based on the last occurrences.
3. When the current index reaches the end of the group, finalize the group and start a new one.

Why This Works:
- By tracking the last occurrence of each species, we ensure that all instances of a species are included in the same group.
- The greedy approach of extending the group's end ensures that we create the largest possible groups without splitting species.

Time Complexity: O(n), where n is the length of the habitats string. We make a single pass to record last occurrences and another pass to form groups.
'''

def group_animals_by_habitat(habitats):
    # Step 1: Record the last occurrence of each species in the habitats string.
    last_occurrence = {species: i for i, species in enumerate(habitats)}

    # Step 2: Initialize variables to track the start and end of the current group.
    groups = []
    start, end = 0, 0

    # Step 3: Iterate through the habitats string to determine the groups.
    for i, species in enumerate(habitats):
        # Update the end of the current group to the last occurrence of the current species.
        end = max(end, last_occurrence[species])

        # If the current index reaches the end of the group, finalize this group.
        if i == end:
            groups.append(end - start + 1)  # Calculate the size of the group.
            start = i + 1  # Move the start to the next index for the next group.

    return groups

print(group_animals_by_habitat("ababcbacadefegdehijhklij")) 
print(group_animals_by_habitat("eccbbbbdec"))