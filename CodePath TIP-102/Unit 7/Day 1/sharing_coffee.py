'''
Problem 3: Sharing the Coffee
The deli staff is in desperate need of caffeine to keep them going through their shift and has decided to divide the coffee 
supply equally among themselves. Each batch of coffee is stored in containers of different sizes. Write a recursive function can_split_coffee() 
that accepts a list of integers coffee representing the volume of each batch of coffee and returns True if the coffee can be split evenly by volume 
among n staff and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the 
stated time and space complexity.

def can_split_coffee(coffee, n):
pass

Example Usage:
print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))

Example Output:
True
False
'''

def can_split_coffee(coffee, n):
    '''
    Plan:
    1. Calculate the total volume of coffee.
    2. Check if the total volume is divisible by n. If not, return False.
    3. Define a helper recursive function to check if we can form n subsets each with the target volume (total_volume // n).
    4. Use backtracking to explore different combinations of coffee batches to form the required subsets.
    Note: Backtracking is used here to explore all possible combinations of coffee batches. For each batch, we have the choice to include it in 
    the current subset or not. If we achieve the target volume for one subset, we move on to form the next subset. 
    '''
    total_volume = sum(coffee)

    if total_volume % n != 0:
        return False
    
    target_volume = total_volume // n
    
    return can_divide(coffee, n, target_volume, 0)

def can_divide(coffee, n, target_volume, current_sum):
    # If we've partitioned coffee for all staff, return True.
    if n == 0:
        return True
    # If current subset reaches the target volume, start forming the next subset.
    if current_sum == target_volume:
        return can_divide(coffee, n - 1, target_volume, 0) # We have 1 less subset to fill.
    # If we have no more coffee batches to consider, return False.
    if not coffee:
        return False
    
    # Try including the first batch in the current subset.
    include_first = can_divide(coffee[1:], n, target_volume, current_sum + coffee[0])
    # Try excluding the first batch from the current subset.
    exclude_first = can_divide(coffee[1:], n, target_volume, current_sum)

    # Return True if either including or excluding the first batch leads to a valid partitioning.
    return include_first or exclude_first

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))