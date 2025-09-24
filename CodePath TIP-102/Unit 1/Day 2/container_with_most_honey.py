'''
Problem 5: Container with Most Honey
Christopher Robin is helping Pooh construct the biggest hunny jar possible.
Help him write a function that accepts an integer array heights of length n. The height of each element is given by heights[i].
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, heights[i]).
Find two lines that, together with the x-axis, form the container that holds the most honey.
Return the maximum amount of honey a container can store.
Notice that you may not slant the container.

def most_honey(heights):
	pass

Example Usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)

Example Output:
49
1
'''

def most_honey(heights):
    l, r = 0, len(heights) - 1
    max_area = 0

    while l < r:
        # Calculate the area formed by the lines at positions l and r.
        h = min(heights[l], heights[r])
        w = r - l # Width between the two lines.
        area = h * w
        max_area = max(max_area, area)

        # We move the shorter line inward, hoping to find a taller line.
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))
