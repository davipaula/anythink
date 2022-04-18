import csv
import json
import logging
from dataclasses import dataclass

import numpy as np
import spacy
from spacy.tokens import Token

from dataset_generator import DATASET_LOCATION, COMMON_WORDS_LOCATION

logger = logging.getLogger(__name__)

VALID_POSITIONS = ["NOUN", "VERB"]

MAXIMUM_WORD_LENGTH = 10
MINIMUM_WORD_LENGTH = 5

nlp = spacy.load("en_core_web_lg")


@dataclass
class Word:
    word: str
    related_words: list[str]


def generate_words() -> None:
    """
    This function creates a dataset containing some of the most common words in English and their most similar words.

    This is a very rudimentary function and should only be used for development (and fun) purposes. the selection of
    words should be improved before the app goes to production to improve the user experience.

    It depends on the common english words file that can be downloaded from Kaggle:
    https://www.kaggle.com/datasets/rtatman/english-word-frequency?resource=download

    The file should be saved as ./anythink/dataset_generator/data/raw/english_words_frequency.csv

    Final format:
    {
        "word": "aCommonWordInEnglish",
        "related_words": [
            "FirstRelatedWord",
            "SecondRelatedWord",
            "NRelatedWord"
        ]
    }
    """
    # Open csv and filter words between 4 and 10 letters
    common_words = __open_common_words()

    # Filter in spacy for: nouns, verbs, non stop-words
    tokens = __filter_valid_words(common_words)

    logger.info("Generating most similar words")
    dataset = list()
    for token in tokens[:10]:
        dataset.append(
            {"word": str(token), "related_words": __get_most_similar(token, 1000)}
        )

    logger.info(f"Generated most similar words. Dataset size {len(dataset)}")

    logger.info("Saving dataset")
    with open(DATASET_LOCATION, "w+") as fp:
        json.dump(dataset, fp)

    logger.info("Dataset saved successfully")


def __filter_valid_words(common_words: list[str]) -> list[Token]:
    docs = nlp.pipe(common_words[:1000])
    filtered_tokens = []
    for doc in docs:
        for token in doc:
            if __is_valid(token):
                filtered_tokens.append(token)

    logger.info(f"Generated {len(filtered_tokens)} filtered tokens")

    return filtered_tokens


def __open_common_words() -> list[str]:
    logger.info("Opening common English words file")
    with open(COMMON_WORDS_LOCATION) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)
        common_words = [
            row[0]
            for row in csv_reader
            if MAXIMUM_WORD_LENGTH >= len(row[0]) > MINIMUM_WORD_LENGTH
        ]

    logger.info(f"Loaded Common English words file. File contains {len(common_words)} lines")

    return common_words


def __is_valid(token: Token):
    return (
            not token.is_stop
            and token.is_alpha
            and not token.like_num
            and token.pos_ in VALID_POSITIONS
    )


def __get_most_similar(token: Token, limit: int = 100) -> list[str]:
    """
    This is a very rudimentary function to return the most similar words for a specific word. It uses the pre-calculated
    similarity functions from SpaCY

    :param token: Word to generate the similar words
    :param limit: Number of similar words to generate
    :return:
    """
    queries = [w for w in token.vocab if np.count_nonzero(w.vector)]

    by_similarity = sorted(queries, key=lambda w: token.similarity(w), reverse=True)

    return [w.lower_ for w in by_similarity[: limit + 1] if w.lower_ != token.lower_]


if __name__ == "__main__":
    generate_words()
