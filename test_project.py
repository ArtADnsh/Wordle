import random
from project import generate_random_word, get_input_word, guess_checker, letter_counter
from project import WORDS
from unittest.mock import patch


def test_generate_random_word():
    for _ in range(10):
        assert generate_random_word() in WORDS


def test_get_input_word():
    with patch('builtins.input', return_value=' apple ') as mock:
        res = get_input_word(1)
        mock.assert_called_once_with("Make your first guess: ")
        assert res == 'apple'

    with patch('builtins.input', return_value='APPLE') as mock:
        res = get_input_word(4)
        mock.assert_called_once_with("Make your guess: (three remaining) ")
        assert res == 'apple'

    with patch('builtins.input', return_value='apple') as mock:
        get_input_word(6)
        mock.assert_called_once_with("Make your last guess: ")


def test_guess_checker(capsys):
    assert guess_checker('apple', 'apple') == 5
    assert guess_checker('apple', 'tiger') == 0
    assert guess_checker('apple', 'appid') == 3

    guess_checker('apple', 'crane')
    out = capsys.readouterr().out
    assert 'NNWNC' in out

    guess_checker('month', 'youth')
    out = capsys.readouterr().out
    assert 'NCNCC' in out


def test_letter_counter():
    assert letter_counter('l', 2, 'apple') == False
    assert letter_counter('o', 2, 'month') == False
    assert letter_counter('a', 1, 'chair') == True