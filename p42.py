import math
import tkinter as tk
import graphviz

def conv(tokens):
    pos = 0
    open_brace = 0
    close_brace = 0
    count = 0
    while pos < len(tokens):
        if tokens[pos] == '{':
            if count == 0:
                open_brace = pos
            count += 1
        if tokens[pos] == '}':
            if count == 1:
                close_brace = pos
                cb_list = tokens[open_brace + 1: close_brace]
                cb_list = conv(cb_list)
                del tokens[open_brace: close_brace + 1]
                tokens.insert(open_brace, cb_list)
                pos = open_brace
            count -= 1
        pos += 1
    return tokens


def parse(tokens, start=0):
    code = []
    pos = start
    while pos < len(tokens):
        if tokens[pos].isdigit():
            tokens[pos] = int(tokens[pos])
        pos += 1
    conv(tokens)
    code = tokens.copy()
    return code


class PS:
    def __init__(self):
        self.stack = []
        self.words = {
            'dup': self.op_dup,
            'add': self.op_add,
            'sub': self.op_sub,
            'mul': self.op_mul,
            'div': self.op_div,
            'pop':  self.op_pop,
            'eq':  self.op_eq,
            'ifelse': self.op_ifelse,
            'def':  self.op_def
        }

    def execute(self, code):
        for i in range(code.count('def')):
            pos = 0
            while pos <= code.index('def'):
                if code[pos] == 'def':
                     self.words[code[pos]]()
                else:
                    self.stack.append(code[pos])
                pos += 1
            del code[:pos]
        pos = 0
        while pos < len(code):
            if isinstance(code[pos], int) or isinstance(code[pos], list):
                self.stack.append(code[pos])
            else:
                self.words[code[pos]]()
            pos += 1


    def op_dup(self):
        self.stack.append(self.stack[len(self.stack) - 1])

    def op_add(self):
        fir = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        sec = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        self.stack.append(fir + sec)

    def op_sub(self):
        fir = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        sec = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        self.stack.append(sec - fir)

    def op_mul(self):
        fir = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        sec = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        self.stack.append(fir * sec)

    def op_div(self):
        fir = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        sec = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)
        self.stack.append(int(sec / fir))

    def op_pop(self):
        self.stack.pop()

    def op_eq(self):
        fir = self.stack.pop()
        sec = self.stack.pop()
        if sec == fir:
            self.stack.append(True)
        else:
            self.stack.append(False)

    def op_ifelse(self):
        if_false = self.stack.pop()
        if_true = self.stack.pop()
        cond = self.stack.pop()
        if cond:
            self.execute(if_true)
        else:
            self.execute(if_false)

    def op_def(self):
        name = self.stack.pop(0).lstrip('/')
        ops = self.stack.pop(0)
        self.words[name] = lambda: self.execute(ops)


source = '/fact { dup 0 eq { pop 1 } { dup 1 sub fact mul } ifelse } def 5 fact'
ps = PS()
ast = parse(source.split())
ps.execute(ast)
#print(ps.stack)


from pathlib import Path

def load_csv(filename):
    text = Path(filename).read_text().strip()
    rows = []
    for line in text.split('\n')[1:]:
        rows.append(line.split(';'))
    return rows


class Cluster:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def toGraph(self, dot):
        dot.node(str(id(self)), label=str(self.Count_elims()))
        if self.data == 0:
            dot.node(str(id(self.left)), label=str(self.left.Count_elims()))
            dot.node(str(id(self.right)), label=str(self.right.Count_elims()))
            dot.edges([(str(id(self.left)), str(id(self))), (str(id(self.right)), str(id(self)))])
            self.left.toGraph(dot)
            self.right.toGraph(dot)

    def Count_elims(self):
        if self.data == 0:
            return self.right.Count_elims()+self.left.Count_elims()
        else:
            return 1


def jaccard_dist(row1, row2):
    a = 0
    b = 0
    c = 0
    for i in range(len(row1)):
        if row1[i] == '1' and row2[i] == '1':
            a += 1
        if row1[i] == '1' and row2[i] == '0':
            b += 1
        if row1[i] == '0' and row2[i] == '1':
            c += 1
    jac = 1 - a/(a+b+c)
    return jac



def cluster_dist(data1, data2):
    dist = 1.0
    if isinstance(data1, Cluster):
        if data1.left is not None:
            dist = cluster_dist(data1.left, data2)
        elif data1.right is not None:
            dist = cluster_dist(data1.right, data2)
    if isinstance(data2, Cluster):
        if data2.left is not None:
            dist = cluster_dist(data1, data2.left)
        elif data2.right is not None:
            dist = cluster_dist(data1, data2.right)
    if isinstance(data1.data, list) and isinstance(data2.data, list):
        dist = jaccard_dist(data1.data[0], data2.data[0])
    return dist


def hclust(rows):
    clusters = [Cluster([row]) for row in rows]
    while len(clusters) > 1:
        tup = tuple([1.0, 0, 0])
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                if cluster_dist(clusters[i], clusters[j]) <= tup[0]:
                    tup = tuple([cluster_dist(clusters[i], clusters[j]), clusters[j], clusters[i]])
        new_clust = Cluster(0, tup[2], tup[1])
        clusters.remove(tup[1])
        clusters.remove(tup[2])
        clusters.append(new_clust)
    return clusters[0]


def gen_dot(cluster, min_dist):
    dot = graphviz.Digraph()
    cluster.toGraph(dot)
    return dot



rows = load_csv('pract4/langs.csv')
cluster = hclust(rows)
print(gen_dot(cluster, 0.5))