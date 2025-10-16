"""
Word Occurrences
Estimate: 40 minutes
Actual:   27 minutes
"""

word_collection = input("Text: ").strip().split()

word_to_count = {}

for word in word_collection:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

longest_key_length = len(max(word_to_count, key=len))  # NOTE: had to search how to use key= for max()

for word in sorted(word_to_count):
    print(f"{word:{longest_key_length}} : {word_to_count[word]}")
