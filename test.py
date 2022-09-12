import pytest

def test_create_list_from_tuple():
    initial_data = ('apple', 'banana', 'cherry')
    array = list(initial_data)
    assert array == ['apple', 'banana', 'cherry']

def test_count_specific_elements_in_array():
    array = [1, 2, 3, 1, 1, 2]
    elements_count = array.count(1)
    assert elements_count == 3

def test_delete_from_empty_list():
    array = list()
    try:
        array.pop()
    except IndexError:
        pass

def test_create_set_with_duplicate_values():
    set = {"apple", "banana", "cherry", "cherry"}
    assert set == {"apple", "banana", "cherry"}

def test_check_is_subset():
    left = {"apple", "banana", "cherry"}
    right = {"apple", "banana"}
    is_subset = right.issubset(left)
    assert is_subset

@pytest.mark.parametrize(
    "left, right, expected",
    [
        (set(), set(), set()),
        (set(), set("apple"), set()),
        ({"apple", "banana", "cherry"}, set(), set()),
        ({"apple", "banana", "cherry"}, {"lemon", "not apple"}, set()),
        ({"apple", "banana", "cherry"}, {"not apple", "banana", "lemon"}, {"banana"}),
    ]
)
def test_intersect_sets(left, right, expected):
    intersection = left.intersection(right)
    assert intersection == expected
