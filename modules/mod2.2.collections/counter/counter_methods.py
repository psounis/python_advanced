from collections import Counter

mystr = """
Chaos isn't a pit. Chaos is a ladder. 
Many who try to climb it fail and never get to try again. 
The fall breaks them. And some are given a chance to climb, but they refuse. 
They cling to the realm or the gods or love. Illusions. 
Only the ladder is real. The climb is all there is.
"""

words = mystr.replace(",","").replace(".","").lower().split()
word_count = Counter(words)
print(word_count)

print(word_count.most_common(2))

word_count.subtract({"the": 2})
print(word_count)

print("=" * 20)
for word in sorted(word_count.elements()):
    print(word)
print("=" * 20)

word_count["the"] = 0
print(word_count["the"], word_count["game"])
print("the" in word_count, "game" in word_count)