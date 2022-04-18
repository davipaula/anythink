from dataclasses import dataclass

from word_generator import generate_word_of_day


@dataclass
class GuessResult:
    found: bool
    word: str
    position: int


class GuesserService:
    def __init__(self):
        self.word_of_day = generate_word_of_day()

    def guess_word(self, word: str) -> GuessResult:
        if word in self.word_of_day.related_words:
            return GuessResult(
                found=True,
                word=word,
                position=self.word_of_day.related_words.index(word) + 1,
            )
        else:
            return GuessResult(found=False, word=word, position=0)

    def get_word_of_day(self) -> str:
        return self.word_of_day.word
