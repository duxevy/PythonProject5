import pytest
from src import filter_by_state

@pytest.fixture()
def operations():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"}
    ]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"}
    ]),
    ("CANCELED", [
        {"id": 2, "state": "CANCELED"},
    ])
])
def test_filter_by_state(state, expected, operations):
    result = filter_by_state(operations, state=state)
    assert result == expected