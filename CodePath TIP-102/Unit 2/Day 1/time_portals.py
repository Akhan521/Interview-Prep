'''
Problem 4: Time Portals
In your time travel adventures, you are given an array of digit strings portals and a digit string destination. 
Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.

Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.

def num_of_time_portals(portals, destination):
    pass
    
Example Usage:
portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))

Example Output:
4
2
6
'''

def num_of_time_portals(portals, destination):
    # We can use a dictionary to count occurrences of each portal string.
    counts = {}
    for portal in portals:
        counts[portal] = counts.get(portal, 0) + 1

    total_pairs = 0
    # We iterate through each portal and check if the destination can be formed by concatenating it with another portal.
    for portal in portals:
        required_portal = destination[len(portal):]  # The string needed to complete the destination.
        if destination.startswith(portal) and required_portal in counts:
            total_pairs += counts[required_portal]
            # If the required portal is the same as the current portal, we need to subtract one to avoid counting the same portal twice.
            if required_portal == portal:
                total_pairs -= 1 

    return total_pairs

    
portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))