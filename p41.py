class Num:
    def __init__(self, num):
        self.num = num

    def to_str(self):
        return str(self.num)

    def get_val(self):
        return self.num

    def get_beg_code(self):
        return str("PUSH " + str(self.num) + '\n')


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.summ = self.left.get_val() + self.right.get_val()

    def to_str(self):
        return str('(' + self.left.to_str() + ' + ' + self.right.to_str() + ')')

    def get_val(self):
        return self.summ

    def get_beg_code(self):
        return str(self.left.get_beg_code() + self.right.get_beg_code() + "ADD" + '\n')

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.mul = self.left.get_val() * self.right.get_val()

    def to_str(self):
        return str('(' + self.left.to_str() + ' * ' + self.right.to_str() + ')')

    def get_val(self):
        return self.mul

    def get_beg_code(self):
        return str(self.left.get_beg_code() + self.right.get_beg_code() + "MUL" + '\n')


class PrintVisitor:
    def visit(self, tree):
        return tree.to_str()


class CalcVisitor:
    def visit(self, tree):
        return tree.get_val()

class StackVisitor:
    def visit(self, tree):
        self.tree = tree

    def get_code(self):
        return  self.tree.get_beg_code()



#re = Add(Mul(Num(3), Num(2)), Num(7))
#pv = PrintVisitor()
#cv = CalcVisitor()
#sv = StackVisitor()
#print(pv.visit(tre))
#print(cv.visit(tre))
#sv.visit(tre)
#print(sv.get_code())

class Body:
    def __enter__(self):
        print("<body>")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("</body>")


class Div:
    def __enter__(self):
        print("<div>")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("</div>")


class P:
    def __init__(self, stra):
        print("<p>" + stra + "</p>")

class HTML:
    def body(self):
        return Body()

    def div(self):
        return Div()

    def p(self, stra):
        return P(stra)

html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
