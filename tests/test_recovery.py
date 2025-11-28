from recovery import Recovery

def test_lowest_alloc_kill():
    allocation = [
        [2,0],
        [0,1],
        [1,1]
    ]
    need = [
        [1,1],
        [2,0],
        [0,1]
    ]
    available = [0,0]
    killed = Recovery.kill_processes("lowest_alloc", allocation, need, available)
    assert isinstance(killed, list)
    assert killed == [1] or killed == [0] or killed == [2]
