import one_dim_array

# remove_duplicates()

def test_remove_duplicates_short_array():
    x = [2]
    n = one_dim_array.remove_duplicates(x, -1)
    assert n == 1
    assert x == [2]

def test_remove_duplicates_no_actual_duplicates():
    x = [2, 4, 6, 8, 10]
    n = one_dim_array.remove_duplicates(x, -1)
    assert n == 5
    assert x == [2, 4, 6, 8, 10]

def test_remove_duplicates_all_are_duplicates():
    x = [3, 3, 3, 3, 3]
    n = one_dim_array.remove_duplicates(x, -1)
    assert n == 1
    assert x == [3, -1, -1, -1, -1]

def test_remove_duplicates_typical_case():
    x = [2, 2, 3, 3, 3, 5, 7, 7, 10]
    n = one_dim_array.remove_duplicates(x, -1)
    assert n == 5
    assert x == [2, 3, 5, 7, 10, -1, -1, -1, -1]

# shift_zeros()

def test_shift_zeros_empty_array():
    x = []
    n = one_dim_array.shift_zeros(x)
    assert n == 0
    assert x == []

def test_shift_zeros_short_array_nozeros():
    x = [2]
    n = one_dim_array.shift_zeros(x)
    assert n == 1
    assert x == [2]

def test_shift_zeros_short_array_onezero():
    x = [0]
    n = one_dim_array.shift_zeros(x)
    assert n == 0
    assert x == [0]

def test_shift_zeros_no_zeros():
    x = [2, 4, 5, 7, 9]
    n = one_dim_array.shift_zeros(x)
    assert n == 5
    assert x == [2, 4, 5, 7, 9]

def test_shift_zeros_all_zeros():
    x = [0, 0, 0, 0, 0]
    n = one_dim_array.shift_zeros(x)
    assert n == 0
    assert x == [0, 0, 0, 0, 0]