'''
You're tasked with filtering out brands that are not sustainable from a list of fashion brands. 
A sustainable brand is defined as one that meets a specific criterion, such as using eco-friendly materials, 
ethical labor practices, or being carbon-neutral.

Write the filter_sustainable_brands() function, which takes a list of brands and a criterion, then returns a 
list of brands that meet the criterion.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why 
you believe your solution has the stated time and space complexity.

def filter_sustainable_brands(brands, criterion):
    pass
    
Example Usage:
brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))

Example Output:
['EcoWear', 'GreenThreads']
['Earthly']
['GreenLife']
'''

def filter_sustainable_brands(brands, criterion):
    sustainable_brands = []
    
    for brand in brands:
        if criterion in brand["criteria"]:
            sustainable_brands.append(brand["name"])
    
    return sustainable_brands

# Time Complexity: O(n * m)
# Space Complexity: O(n)
# -> n is the number of brands in the input list, m is the average number of criteria per brand.

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]
print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))