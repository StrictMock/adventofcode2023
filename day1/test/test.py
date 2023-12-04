from main import solve


def test_empty_list():
    assert solve([]) == 0


def test_single_item():
    assert solve(["1asd3"]) == 13


def test_more_items():
    assert solve(["1asd3", "3qwe5f", "ho7a1"]) == 119


def test_multiple_numbers():
    assert solve(["111a2345", "123hggf4fsdf5", "563asdfg54354g53"]) == 83


def test_zeros():
    assert solve(["0asd1", "1wer45", "q01b8"]) == 24
