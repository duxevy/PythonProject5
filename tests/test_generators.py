import pytest
from src.generators import card_number_gen

@pytest.mark.parametrize("start, stop, first, second", [
    (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0002"),
    (99, 101, "0000 0000 0000 0099", "0000 0000 0000 0100"),
    (999, 1001, "0000 0000 0000 0999", "0000 0000 0000 1000")
])
def test_card_number_gen(start, stop, first, second):
    gen = card_number_gen(start, stop)
    assert next(gen) == first
    assert next(gen) == second