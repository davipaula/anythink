from dataset_reader import get_words
from word import Word

WORDS = ["word", "apple", "music", "phantom", "phone", "head", "set"]


def generate_word_of_day() -> Word:
    return get_words()[0]
