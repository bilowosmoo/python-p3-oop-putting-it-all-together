import pytest
from lib.book import Book

class TestBook:
    def test_has_title_and_page_count(self):
        book = Book("Python 101", 250)
        assert book.title == "Python 101"
        assert book.page_count == 250

    def test_page_count_must_be_int(self, capsys):
        book = Book("Intro to CS", 300)
        book.page_count = "a lot"
        captured = capsys.readouterr()
        assert "page_count must be an integer" in captured.out
        assert book.page_count == 300

    def test_turn_page_prints_message(self, capsys):
        book = Book("Algorithms", 150)
        book.turn_page()
        captured = capsys.readouterr()
        assert "Flipping the page...wow, you read fast!" in captured.out
