from dataclasses import dataclass

WORDS = ["word", "apple", "music", "phantom", "phone", "head", "set"]


@dataclass
class GuessResult:
    found: bool
    word: str
    position: int


def guess_word(word: str) -> GuessResult:
    if word in WORDS:
        return GuessResult(found=True, word=word, position=WORDS.index(word) + 1)
    else:
        return GuessResult(found=False, word=word, position=0)
