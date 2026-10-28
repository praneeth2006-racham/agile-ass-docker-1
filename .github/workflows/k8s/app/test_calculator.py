from app.calculator import add, subtract

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
