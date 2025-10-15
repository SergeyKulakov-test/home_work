def clean_text(text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    cleaned_text = ""
    for char in text.lower():
        if char not in punctuation:
            cleaned_text += char
    return cleaned_text


def count_words(words):
    return len(words)


def find_longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def count_vowels(text):
    vowels = "аеёиоуыэюя"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count


def count_word_frequency(words):
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


def analyze_text(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    word_count = count_words(words)
    longest_word = find_longest_word(words)
    vowel_count = count_vowels(cleaned_text)
    word_frequency = count_word_frequency(words)

    return {
        'word_count': word_count,
        'longest_word': longest_word,
        'vowel_count': vowel_count,
        'word_frequency': word_frequency
    }

def print_results(results):
    print(f"1. Общее количество слов: {results['word_count']}")
    print(f"2. Самое длинное слово: '{results['longest_word']}'")
    print(f"3. Количество гласных букв: {results['vowel_count']}")
    print("4. Частота слов:")
    for word, freq in results['word_frequency'].items():
        print(f"   '{word}': {freq}")

text = input("Введите текст: ")
results = analyze_text(text)
print_results(results)







