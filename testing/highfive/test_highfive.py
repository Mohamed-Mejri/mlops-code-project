import pytest
from highfive import is_highfive



@pytest.mark.parametrize(
    "test_input, expected",
    [(105, True), (100, False), (106, False)],
)
def test_is_highfive(test_input, expected):
    assert is_highfive(test_input) == expected
