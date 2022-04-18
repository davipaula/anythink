import json

from dataset_generator import DATASET_LOCATION
from word import Word


def get_words():
    with open(DATASET_LOCATION) as json_file:
        dataset = json.load(json_file)

    print(f"Loaded {len(dataset)} lines")

    # Transform object
    print("Preparing data")

    return [Word(row["word"], [row["word"], *row["related_words"]]) for row in dataset]
