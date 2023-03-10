#doctest.testfile("example.txt")

def fir(a, b, c):

    if a == b == c:
        return "Равносторонний"
    elif a == b or a == c or b == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

def test_fact():
    assert fir(5, 5, 5) == "Равносторонний"
    assert fir(5, 3, 5) == "Равнобедренный"