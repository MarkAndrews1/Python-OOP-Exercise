"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Finds a random word from dict

    >>> test = WordFinder('test.txt')
    6 words read

    >>> test.random() in ["pig", "dog", "fish", "bird", "cat", "horse"]
    True
    """


    def __init__(self, path):
        """Reads the dict adn reports words with #"""
        file = open(path)
        self.words = self.create_list(file)
        print(f"{len(self.words)} words read")


    def create_list(self, file):
        """Makes a list of words"""
        return list(word.strip() for word in file)
    
    def random(self):
        """Returns a random word"""
        return choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Finds a random word from dict without blank lines or #

    >>> test = SpecialWordFinder("specialTest.txt")
    4 words read

    >>> test.random() in ["mango", "apple", "parsnips", "kale"]
    True
    """
    def create_list(self, file):
        """Makes list excluding words with blank lines or #"""
        return list(word.strip() for word in file if word.strip() and not word.startswith("#"))