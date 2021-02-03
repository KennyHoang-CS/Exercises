"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    

    def __init__(self,path):
        """Read in the dictionary and report the total count of items read. """
        file = open(path)
        self.words = self.parse(file)
        print(f'{len(self.words)} words read')

    def parse(self, file):
        """Parse the file into a list of words. """
        return [word.strip() for word in file]

    def random(self):
        """Return random word. """
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """ Specialized WordFinder that eliminate lines that starts with '#' """
    def parse(self, file):
        """Parse the file into a list of words without the '#'. """
        return [word.strip for word in file if word.strip and not word.startswith('#')]
