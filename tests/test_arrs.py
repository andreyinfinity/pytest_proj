from utils import arrs


def test_get(list_array):
    assert arrs.get(list_array, 2, "test") == 3
    assert arrs.get([], -1, "test") == "test"


def test_slice(list_array):
    assert arrs.my_slice(list_array, 1, 3) == [2, 3]
    assert arrs.my_slice(list_array, 3, 1) == []
    assert arrs.my_slice(list_array, -1) == [4]
    assert arrs.my_slice(list_array, -5) == [1, 2, 3, 4]
    assert arrs.my_slice(list_array, 1) == [2, 3, 4]
    assert arrs.my_slice([], 0) == []
