import re

class knowledge_base:
    def __init__(self):
        self.is_first = True
        self.is_film_price = False

    @staticmethod
    def split_words(msg):
        return list(filter(None, str.split(re.sub(
            r'[^\w\s:]', r' ', msg).lower())))