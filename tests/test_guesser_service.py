from anythink.guesser_service import guess_word


def test_when_word_is_not_in_list_return_error():
    result = guess_word("unknown_word")

    assert result.found is False


def test_when_word_is_in_list_return_true():
    result = guess_word("word")

    assert result.found is True
