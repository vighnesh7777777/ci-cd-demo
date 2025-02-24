def add(a, b ,c):
    return a + b + c

def test_add():
    assert add(2, 3 ,5) == 10  # Test case

if __name__ == "__main__":
    print("Addition:", add(2, 3 ,5))
