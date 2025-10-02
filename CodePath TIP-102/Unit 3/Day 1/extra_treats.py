'''
Problem 1: Extra Treats
At the pet adoption center, there are two groups of volunteers:

'C' — Cat Lovers
'D' — Dog Lovers

Each week, these groups vote to decide which type of pet should receive extra treats. The voting happens in rounds, following these rules:

Ban a Vote: In each round, a volunteer can ban one volunteer from the opposite group. 
A banned volunteer loses all voting rights for the rest of the process.

Declare Victory: If at any point all remaining volunteers are from the same group, that group can declare victory, 
and their preferred pet will receive the extra treats.\

You are given a string votes representing the group affiliation of each volunteer. 
The character at index i is either 'C' (Cat Lovers) or 'D' (Dog Lovers).

Assuming each volunteer acts in order (from left to right) and the process repeats until
one group wins, predict which group will eventually declare victory.

Return:
"Cat Lovers" if the Cat Lovers will win.
"Dog Lovers" if the Dog Lovers will win.

def predict_adoption_victory(votes):
  pass
  
Example Usage:
print(predict_adoption_victory("CD")) 
print(predict_adoption_victory("CDD")) 

Example Output:
Cat Lovers
Dog Lovers
'''

from collections import deque
def predict_adoption_victory(votes):
    # Initialize queues for both groups; we'll use 2 queues to simulate voting queues/lines for each group.
    cat_queue = deque()
    dog_queue = deque()

    for i, vote in enumerate(votes):
        # Add the position of each volunteer to their respective queue.
        if vote == 'C':
            cat_queue.append(i)
        else:
            dog_queue.append(i)

    # Process the voting rounds until one group is completely banned.
    while cat_queue and dog_queue:
        # Get the front volunteer from each group.
        cat_index = cat_queue.popleft()
        dog_index = dog_queue.popleft()

        # The volunteer with the smaller index bans the other.
        if cat_index < dog_index:
            # The Cat Lover bans the Dog Lover; the Cat Lover gets to vote again in the next round.
            cat_queue.append(cat_index + len(votes))
        else:
            # The Dog Lover bans the Cat Lover; the Dog Lover gets to vote again in the next round.
            dog_queue.append(dog_index + len(votes))

    # Determine which group has remaining volunteers.
    return "Cat Lovers" if cat_queue else "Dog Lovers"

print(predict_adoption_victory("CD")) 
print(predict_adoption_victory("CDD")) 