import os
import pathlib

BASE_FOLDER = str(pathlib.Path(__file__).parent.parent.resolve())

DATA_FOLDER = [
    "dataset_generator",
    "data",
]

DATASET_FOLDER = "final"

DATASET_FILENAME = "dataset.json"

DATASET_LOCATION = os.sep.join(
    [BASE_FOLDER, *DATA_FOLDER, DATASET_FOLDER, DATASET_FILENAME]
)

RAW_DATA_FOLDER = "raw"

COMMON_WORDS_FILENAME = "english_words_frequency.csv"

COMMON_WORDS_LOCATION = os.sep.join(
    [BASE_FOLDER, *DATA_FOLDER, RAW_DATA_FOLDER, COMMON_WORDS_FILENAME]
)


if __name__ == "__main__":
    print(DATASET_LOCATION)
