from dataclasses import dataclass


@dataclass
class Word:
    word: str
    related_words: list[str]
