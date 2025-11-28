from detection import DeadlockDetector

def test_cycle_detection():
    allocation = [
        [0,1],
        [1,0]
    ]
    request = [
        [1,0],
        [0,1]
    ]
    d = DeadlockDetector(allocation, request)
    cycles = d.detect_deadlocks()
    assert len(cycles) > 0
