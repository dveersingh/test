import requests

class DictSearch:
    def __init__(self, word):
        self.word = word
    def meaning(self):

        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/{}".format(word)
        try:
            x = requests.get(url)
            for items in x.json():
                meaning = items['meanings']
                for mean in meaning:
                    defi = mean['definitions']
                    for real in defi:
                        print(items['word'],", ",mean['partOfSpeech'], ", ",real['definition'])
        except Exception as e:
            print("Error", e)
word = input("Word??")
p1 = DictSearch(word)
s = p1.meaning()