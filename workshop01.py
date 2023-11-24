def get_word_counts(sentence):
    word_counts = {}
    words = sentence.split()
    
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

def main():
    sentence = input("Enter a sentence in English: ")
    
    word_counts = get_word_counts(sentence)
    
    total_words = len(word_counts)
    repeated_words = {k: v for k, v in word_counts.items() if v > 1}
    num_repeated_words = len(repeated_words)
    
    print("Total number of words:", total_words)
    print("Number of repeated words:", num_repeated_words)
    
    if num_repeated_words > 0:
        print("Repeated words:")
        for word, count in repeated_words.items():
            print(f"{word}: {count} times")

if __name__ == "__main__":
    main()