from googletrans import Translator, LANGUAGES
from pprint import pprint

text = 'Buruk is my son'
t = Translator().translate(text, dest='am')
print(t)
print(LANGUAGES)
# print(Translator().detect(text))
# for language in LANGUAGES:
#     t = Translator().translate(text, dest='am')
#     print(LANGUAGES[language] + ':' + t.text)
# print(len(LANGUAGES))

