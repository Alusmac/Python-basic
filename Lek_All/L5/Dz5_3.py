import string

text = input("Введіть рядок: ")

text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()
hashtag = '#' + ''.join([word.capitalize() for word in words])

hashtag = hashtag[:140]

print(hashtag)
