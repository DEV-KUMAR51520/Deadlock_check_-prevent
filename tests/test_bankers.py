from bankes import Bankers

def test_is_safe_true():
    available = [3, 3, 2]
    max_matrix = [
        [7,5,3],
        [3,2,2],
        [9,0,2],
        [2,2,2],
        [4,3,3]
    ]
    allocation = [
        [0,1,0],
        [2,0,0],
        [3,0,2],
        [2,1,1],
        [0,0,2]
    ]
    b = Bankers(available, max_matrix, allocation)
    safe, seq = b.is_safe()
    assert safe is True
    assert len(seq) == 5
