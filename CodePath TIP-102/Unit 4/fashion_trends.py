'''
Problem 3: Fashion Trends
In the fast-changing world of fashion, certain materials and practices become trending based on how frequently 
they are adopted by brands. You want to identify which materials and practices are trending. A material or practice 
is considered "trending" if it appears in the dataset more than once.

Write the find_trending_materials() function, which takes a list of brands (each with a list of materials or practices) 
and returns a list of materials or practices that are trending (i.e., those that appear more than once across all brands).

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe 
your solution has the stated time and space complexity.

def find_trending_materials(brands):
    pass
    
Example Usage:
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))

Example Output:
['organic cotton', 'recycled polyester', 'bamboo']
['hemp', 'linen']
['recycled polyester']
'''

def find_trending_materials(brands):
    material_count = {}
    trending_materials = []

    for brand in brands:
        for material in brand["materials"]:
            if material in material_count:
                material_count[material] += 1
            else:
                material_count[material] = 1

    for material, count in material_count.items():
        if count > 1:
            trending_materials.append(material)

    return trending_materials

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))