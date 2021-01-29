def print_upper_words(words):
    # Convert every word to upper 
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    # Convert every word to upper if starts with e

    for word in words:
        if word.startswith('e') or words.startswith('E'):
            print(word.upper()) 

def print_upper_words3(words, letters):
    # Convert every word to upper if it meets the rules

    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                break