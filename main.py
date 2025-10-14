text = input("Введите текст: ").lower()

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
cleaned_text = ""
for char in text:
    if char not in punctuation:
        cleaned_text += char

words = cleaned_text.split()
word_count = len(words)

vowels = "аеёиоуыэюя"
vowel_count = 0
for char in cleaned_text:
    if char in vowels:
        vowel_count += 1

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(f"1. Общее количество слов: {word_count}", f"2. Самое длинное слово: '{longest_word}'", f"3. Количество гласных букв: {vowel_count}", "4. Частота слов:", sep="\n")
for word, freq in word_frequency.items():
    print(f"   '{word}': {freq}")






