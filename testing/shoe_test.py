import pytest
from lib.shoe import Shoe

class TestShoe:
    def test_has_brand_and_size(self):
        shoe = Shoe("Nike", 10)
        assert shoe.brand == "Nike"
        assert shoe.size == 10

    def test_size_must_be_int(self, capsys):
        shoe = Shoe("Adidas", 9)
        shoe.size = "large"
        captured = capsys.readouterr()
        assert "size must be an integer" in captured.out
        assert shoe.size == 9

    def test_cobble_sets_condition_to_new(self, capsys):
        shoe = Shoe("Puma", 8)
        shoe.cobble()
        captured = capsys.readouterr()
        assert "Your shoe is as good as new!" in captured.out
        assert shoe.condition == "New"
