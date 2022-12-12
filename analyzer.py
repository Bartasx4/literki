from pprint import pprint


class Analyzer:

    def __init__(self, length=5):
        self.dictionary = []
        self.tags = []
        self.length = length

    def load_dictionary(self, file_name, append=False):
        if not append:
            self.dictionary = []
        with open(file_name, 'r') as file:
            try:
                for index, word in enumerate(file):
                    raw_word = word.strip().strip('\n')
                    tags = []
                    position = raw_word.find('/')
                    if position != -1:
                        tags = list(raw_word[position+1:])
                        for tag in tags:
                            if tag not in self.tags:
                                self.tags.append(tag)
                        raw_word = raw_word[:position]
                    self.dictionary.append((raw_word, tags))
            except Exception as e:
                print(index, word)
                print(e)
        return self.dictionary

    def get(self, include= None, exclude = None, length = None):
        pass

    def __getitem__(self, item):
        return self.dictionary[item]
