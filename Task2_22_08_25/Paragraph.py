from collections import Counter

# Take paragraph input
paragraph = input("Enter a paragraph:\n")

# Convert to lowercase and split into words
words = paragraph.lower().split()

# Remove punctuation (optional, simple way)
cleaned_words = [word.strip(".,!?;:-()[]{}\"'") for word in words]

# Total words
total_words = len(cleaned_words)

# Word frequency
word_freq = Counter(cleaned_words)

# Longest word
longest_word = max(cleaned_words, key=len)

# Top 3 most frequent words
top_3 = word_freq.most_common(3)

# Results
print("\n--- Analysis ---")
print("Total words:", total_words)
print("Word frequencies:", dict(word_freq))
print("Longest word:", longest_word)
print("Top 3 most frequent words:", top_3)