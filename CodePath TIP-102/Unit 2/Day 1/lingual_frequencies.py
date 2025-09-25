'''
Problem 7: Lingual Frequencies
As a time traveling linguist, you are analyzing texts written in an ancient script. However, some words in the text are 
illegible and can't be deciphered. Write a function find_most_frequent_word() that accepts a string text and a list of 
illegible words illegibles and returns the most frequent word in text that is not an illegible word.

def find_most_frequent_word(text, illegibles):
    pass
    
Example Usage:
paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 

Example Output:
a
ball

Example 2 Explanation:
"hit" occurs 3 times, but it is an unknown word.
"ball" occurs twice (and no other word does), so it is the most frequent legible word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is illegible.
'''

from collections import Counter 
def find_most_frequent_word(text, illegibles):
    # Lowercase the text to make it case insensitive.
    text = text.lower()

    # Create a set for faster lookup of illegible words.
    illegibles = set(word.lower() for word in illegibles)

    # Replace punctuation with spaces to isolate words.
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char
        else:
            cleaned_text += " "

    # Split the cleaned text into words.
    words = cleaned_text.split()

    # Remove illegible words from the list of words.
    legible_words = [word for word in words if word not in illegibles]

    # Count the frequency of each legible word.
    word_counts = Counter(legible_words)

    # Find the most common legible word.
    if word_counts:
        most_common, _ = word_counts.most_common(1)[0]
        return most_common
    return None

paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 