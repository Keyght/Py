import re
import doctest
def fir(a, b, c):
    """

    >>> fir(5, 5, 5)
    'Равносторонний'
    """

    if a == b == c:
        return "Равносторонний"
    elif a == b or a == c or b == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"


assert fir(5, 5, 5) == "Равносторонний"
assert fir(5, 3, 5) == "Равнобедренный"
assert fir(5, 3, 4) == "Разносторонний"
#assert fir(5, 5, 4) == "Разносторонний"

def sec(stra):
    res = re.findall(r'[a-z]', stra)
    res.append(re.findall(r'[A-Z]', stra))
    res.append(re.findall(r'[0-9]', stra))
    res.append(re.findall(r'[!, @, #, $, %, ^, &, *, (, ), -, _, +, =]', stra))
    count = 0
    for i in res:
        if isinstance(i, list) and len(i) != 0:
            count += 1
    if count == 3 and len(stra) > 5:
        return "Надёжный"
    else:
        return "Ненадёжный"

assert sec('rrrrr') == "Ненадёжный"
assert sec('QwertY2$') == "Надёжный"
assert sec('qwertyuh34') == "Ненадёжный"
#assert sec('rrrrr') == "Надёжный"

def thi(stra):
    if stra.count(".") == 3 and all(str(int(i)) == i and 0 <= int(i) <= 255 for i in stra.split(".")):
        return "IPv4"
    else:
        return "NO"

assert thi("255.243.231.23") == "IPv4"
assert thi("23.45.123.266") == "NO"
#assert thi("23") == "IPv4"

class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in range(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data

buf = RingBuffer(4)
for i in range(10):
    buf.append(i)
assert (buf.get()) == [6, 7, 8, 9]
#assert (buf.get()) == [6, 7, 8, 0]


def fif(stra):
    p = re.compile(r'<.*?>')
    return p.sub('', stra)

assert fif('<b>Hello</b> and <a href="">bye</a>') == "Hello and bye"
assert fif('<b>Hello mf</b><a href=""></a><body> beach</body>') == "Hello mf beach"
#assert fif('<b>Hello mf</b><a href=""></a><body> beach</body>') == "Hello and bye"

def sixth(a, b, c):
    if a[1:] == "см":
        a = float(a[0])
    elif a[1:] == "мм":
        a = float(a[0])/10
    elif a[1:] == "м":
        a = float(a[0])*100
    elif a[2:] == "см":
        a = float(a[0])*10+float(a[1])
    elif a[2:] == "мм":
        a = (float(a[0])*10+float(a[1]))/10
    elif a[2:] == "м":
        a = (float(a[0])*10+float(a[1]))*100
    if c[1:] == "см":
        c = float(c[0])
    elif c[1:] == "мм":
        c = float(c[0])/10
    elif c[1:] == "м":
        c = float(c[0])*100
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c
    elif b == '/':
        return a / c

assert sixth("1м", "+", "1мм") == 100.1
assert sixth("10см", "+", "1мм") == 10.1
#assert sixth("1мм", "+", "1мм") == 0.1

