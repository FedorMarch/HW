def int_func (text):
    return text[0].upper() + text[1:]
lower_words = input('Слова из латинских букв в нижнем регистре через пробел').split()
upper_words = []
for word in lower_words:
    upper_words.append(int_func(word))
print(' '.join(upper_words))
