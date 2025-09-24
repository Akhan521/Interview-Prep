'''
Problem 2: HulkSmash
Write a function hulk_smash() that accepts an integer n and returns a 1-indexed string array answer where:

answer[i] == "HulkSmash" if i is divisible by 3 and 5.
answer[i] == "Hulk" if i is divisible by 3.
answer[i] == "Smash" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

def hulk_smash(n):
	pass
    
Example Usage:
n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)

Example Output:
["1", "2", "Hulk"]
["1", "2", "Hulk", "4", "Smash"]
["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]
'''

def hulk_smash(n):
    answer = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("HulkSmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(str(i))

    return answer

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))