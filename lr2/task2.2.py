import os.path
import re


class WordProcessing:
    """
    Class WordProcessing
    This class is used to analyze the text
    It takes 1 parameter: name of text file
    Class has one method that counts the number of
    symbols, words and sentences in the text file
    """
    def __init__(self, name):
        if not os.path.exists(name):
            raise FileNotFoundError("Can not open the file")
        self.__name = name
        self.__symbols = 0
        self.__words = 0
        self.__sentences = 0

    def text_analysis(self):
        with open(self.__name) as f:
            text = f.read()
            self.__symbols = len(text)
            self.__words = len(re.findall("[\\w]+", text))
            self.__sentences = text.count('.') + text.count('!') + text.count('?')
        f.close()

    def get_symbols_numbers(self):
        return self.__symbols

    def get_words_numbers(self):
        return self.__words

    def get_sentences_numbers(self):
        return self.__sentences

    def __str__(self):
        return f'File name "{self.__name}"\nSymbols = {self.__symbols}\n' \
               f'Words = {self.__words}\nSentences = {self.__sentences}'


if __name__ == '__main__':
    o1 = WordProcessing("file.txt")
    o1.text_analysis()
    print(f"Symbols {o1.get_symbols_numbers()}")
    print(f"Words {o1.get_words_numbers()}")
    print(f"Sentences {o1.get_sentences_numbers()}")
