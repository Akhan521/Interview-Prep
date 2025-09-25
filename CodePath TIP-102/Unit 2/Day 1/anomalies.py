'''
Problem 5: Detect Temporal Anomaly
As a time traveler, you have recorded the occurrences of specific events at different time points. 
You suspect that some events might be occurring too frequently within short time spans, indicating potential 
temporal anomalies. Given an array time_points where each element represents an event ID at a particular time point, 
and an integer k, determine if there are two distinct time points i and j such that time_points[i] == time_points[j] 
and the absolute difference between i and j is at most k.

Note: The indices must be unique, but not the values i and j themselves.

def detect_temporal_anomaly(time_points, k):
    pass
    
Example Usage:
time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 

Example Output:
True
True
False
'''

def detect_temporal_anomaly(time_points, k):
    seen = {}
    for i, event in enumerate(time_points):
        if event in seen and i - seen[event] <= k:
            return True
        seen[event] = i
    return False

time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 
