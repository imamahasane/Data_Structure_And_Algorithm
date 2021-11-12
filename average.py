def average(L):
    if not L:
        return None
    
    return sum(L) / len(L)

def test_agerage():
    assert 3.0 == average([1, 2, 3, 4, 5])