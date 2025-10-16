"""
Word Occurrences
Estimate: 40 minutes
Actual:   .... minutes
"""

word_collection = input("Text: ").strip().split()

word_to_count = {}

for word in word_collection:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

for word in word_to_count:
    print(f"{word} : {word_to_count[word]}")
