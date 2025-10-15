'''
Problem 4: Telephone
The Villager constructor has been updated to include an additional attribute neighbor. A villager's neighbor is another Villager 
instance and represents their closest neighbor. By default, a Villager's neighbor is set to None.

Given two Villager instances start_villager and target_villager, write a function message_received() that returns True if you can 
pass a message from the start_villager to the target_villager through a series of neighbors and False otherwise.

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems
	
def message_received(start_villager, target_villager):
    pass
    
Example Usage:
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))

Example Output:
True
Example 1 Explanation: Isabelle can pass a message to her neighbor, Tom Nook. Tom Nook can then pass the 
message to his neighbor, KK Slider. KK Slider is the target, therefore the function should return True.

False
Example 2 Explanation: KK Slider doesn't have a neighbor, so you cannot pass a message to Isabelle from 
KK Slider. 
'''

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

def message_received(start_villager, target_villager):
    curr_villager = start_villager
    visited = set() # To avoid infinite loops in case of cycles.

    while curr_villager is not None:
        # If we reach the target villager, return True.
        if curr_villager == target_villager:
            return True
        # If we've already visited this villager, we're in a cycle.
        if curr_villager in visited:
            break
        # Mark the current villager as visited.
        visited.add(curr_villager)
        # Move to the next neighbor.
        curr_villager = curr_villager.neighbor

    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))