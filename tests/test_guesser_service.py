from anythink.guesser_service import GuesserService


def test_when_word_is_not_in_list_return_error():
    result = GuesserService().guess_word("unknown_word")

    assert result.found is False


def test_when_word_is_in_list_return_true():
    result = GuesserService().guess_word("search")

    assert result.found is True
