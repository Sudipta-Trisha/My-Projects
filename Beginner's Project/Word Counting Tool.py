def word_count(text):
    words = text.split()
    word_frequency = {}

    for word in words:
        # Remove punctuation from the word (optional)
        word = word.strip('.,?!()[]{}"\'')
        word = word.lower()

        # Update the word frequency dictionary
        if word:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    return word_frequency


print("Welcome to the Word Counting Tool!")

# Get input text from the user
input_text = input("Enter some text: ")

# Count words
word_frequency = word_count(input_text)

# Display word count results
print("\nWord Count Results:")
for word, count in sorted(word_frequency.items()):
    print(f"{word}: {count} times")
