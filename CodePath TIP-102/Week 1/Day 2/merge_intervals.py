'''
Problem 6: Merge Intervals
You are given an array of intervals, where each interval is represented as [start, end].
Write a function merge_intervals(intervals) that merges all overlapping intervals and returns a new array of the merged, non-overlapping intervals.

def merge_intervals(intervals):
	pass
    
Example Usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)

Example Output:
[[1, 6], [8, 10], [15, 18]]
[[1, 5]]
'''

def merge_intervals(intervals):
    '''
    Plan:
        1. If the intervals list is empty, return an empty list.
        2. Sort the intervals based on their starting points.
        3. Initialize a list `merged` and add the first interval.
        4. For each subsequent interval:
            a. Compare the current interval with the last merged interval.
            b. If they overlap (i.e., the start of the current interval is less than or equal to the end of the last merged interval):
                - Merge them by updating the end of the last merged interval.
            c. If they do not overlap:
                - Append the current interval to the `merged` list.
        5. Return the `merged` list.
    '''
    # If the intervals list is empty, we'll simply return an empty list.
    if not intervals:
        return []
    
    # We first sort our intervals by their starting times.
    intervals.sort(key = lambda time: time[0])

    merged = [intervals[0]] # Adding the first interval to our merged list.
    
    for current_interval in intervals[1:]:
        last_merged = merged[-1]
        # If they overlap, we'll merge our current interval with the last merged interval.
        if current_interval[0] <= last_merged[1]:
            last_merged[1] = max(current_interval[1], last_merged[1])
        # If they don't overlap, we'll append the current interval to our merged list.
        else:
            merged.append(current_interval)

    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))