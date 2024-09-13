import random  
import string  
from abc import ABC, abstractmethod

import nltk  
nltk.download('words')  # Downloading the NLTK words corpus, which contains a list of words

# Abstract Base Class for password generators
class ParentPasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        # Abstract method that must be implemented by all subclasses
        pass

# Class for generating PIN (numeric) passwords
class PinPasswordGenerator(ParentPasswordGenerator):
    
    def __init__(self, length):
        # Initializing the class with the desired length of the PIN
        self.length = length
        
    def generate(self):
        # Generate a random PIN consisting of digits only, with the specified length
        return ''.join(random.choice(string.digits) for _ in range(self.length))

# Class for generating random character-based passwords
class RandomPasswordGenerator(ParentPasswordGenerator):
    
    def __init__(self, length, include_num=False, include_symbols=False):
        # Initialize the length of the password and optional inclusion of numbers and symbols
        self.length = length
        self.characters = string.ascii_letters  # Start with letters only by default
        
        # If numbers are to be included, add digits to the character set
        if include_num:
            self.characters += string.digits
        
        # If symbols are to be included, add punctuation to the character set
        if include_symbols:
            self.characters += string.punctuation
              
    def generate(self):
        # Generate a random password consisting of characters from the selected set (letters, numbers, symbols)
        return ''.join(random.choice(self.characters) for _ in range(self.length))

# Class for generating random word-based passwords
class RandomWordsGenerator(ParentPasswordGenerator):
    
    def __init__(self, num_words):
        # Initialize the number of words for the password
        self.num_words = num_words
        self.words = nltk.corpus.words.words()  # Get the list of words from the NLTK corpus
        
    def generate(self):
        # Generate a password by choosing random words from the word list and converting them to lowercase
        self.password = [random.choice(self.words).lower() for _ in range(self.num_words)]
        
        # Check if all words in the password are unique (no duplicates)
        if len(set(self.password)) == self.num_words:
            return self.password  # Return the password if no duplicates
        
        # If there are duplicates, regenerate the password
        self.generate()
