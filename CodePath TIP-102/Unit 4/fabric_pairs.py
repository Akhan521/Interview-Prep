'''
Problem 4: Fabric Pairing
You want to find pairs of fabrics that, when combined, maximize eco-friendliness while staying within a budget. 
Each fabric has a cost associated with it, and your goal is to identify the pair of fabrics whose combined cost 
is the highest possible without exceeding the budget.

Write the find_best_fabric_pair() function, which takes a list of fabrics (each with a name and cost) and a budget. 
The function should return the names of the two fabrics whose combined cost is the closest to the budget without exceeding it.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity.

def find_best_fabric_pair(fabrics, budget):
    pass
    
Example Usage:
fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))

Example Output:
('Hemp', 'Organic Cotton')
('Tencel', 'Recycled Wool')
('Bamboo', 'Linen')
'''

def find_best_fabric_pair(fabrics, budget):
    # Sort fabrics by cost (to use two-pointer technique).
    fabrics.sort(key=lambda x: x[1]) 

    l, r = 0, len(fabrics) - 1
    best_pair = None
    best_cost = 0

    while l < r:
        current_cost = fabrics[l][1] + fabrics[r][1]
        
        if current_cost > budget:
            r -= 1
        else:
            if current_cost > best_cost:
                best_cost = current_cost
                best_pair = (fabrics[l][0], fabrics[r][0])
            l += 1

    return best_pair

fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

print(find_best_fabric_pair(fabrics, 45))
print(find_best_fabric_pair(fabrics_2, 70))
print(find_best_fabric_pair(fabrics_3, 60))