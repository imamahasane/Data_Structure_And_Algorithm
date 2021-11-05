def fibonacci(n):
    if n in [1, 2]:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8