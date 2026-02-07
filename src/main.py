import random
import string
from abc import ABC, abstractmethod
import nltk


class PasswordGenerator(ABC):
    """
    Base class for generating password.
     """
    @abstractmethod
    def generate(self):
        """
        Subclasses should override this method to generat password.
        """
        pass


class PinPasswordGenerator(PasswordGenerator):
    """Generates a pin password which consists of numbers.
    """
    def __init__(self, length=4):
        self.length = length
    
    def generate(self):
        """
        Generates a numeric password for the given length.
        """
        return ''.join(random.choice(string.digits) for i in range(self.length))
    
    
class RandomPasswordGenerator(PasswordGenerator):
    """
    Class to creates a random password. Can be include of charecters and symbols.
    """
    def __init__(self, length=8, include_numbers=False, include_symbols=False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        """
        Generate a password from specified characters.
        """
        return ''.join(random.choice(self.characters) for i in range(self.length))
    
    
class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate a memorable password.
    """
    def __init__(
            self,
            num_of_words=4,
            seperator='-',
            capitalize=False,
            vocabulary=None
        ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        self.num_of_words = num_of_words
        self.vocabulary = vocabulary
        self.seperator = seperator
        self.capitalize = capitalize

    def generate(self):
        """
        Generate a password with words that are easy to rememmber.
        """
        password_words = [random.choice(self.vocabulary) for i in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower()  for word in password_words]
        return self.seperator.join(password_words)
    
if __name__ == '__main__':
    r_object = RandomPasswordGenerator()
    p_object = PinPasswordGenerator()
    m_object = MemorablePasswordGenerator()
    print(r_object.generate())
    print(p_object.generate())
    print(m_object.generate())
    