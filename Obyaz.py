def f23(e):
    i = 0
    while i < len(e):
        j = 0
        while j < len(e[i]):
            if (e[i][j] == '') or (e[i][j] is None):
                e[i].pop(j)
                j -= 1
            j += 1
        i += 1
    i = 0
    while i < len(e):
        if (e[i] == []) or (e[i] is None):
            e.pop(i)
            i -= 1
        i += 1
    e = [*zip(*e)]
    e = [list(i) for i in e]
    i = 0
    while i < len(e):
        j = 0
        while j < len(e[i]):
            if (e[i][j] == '') or (e[i][j] is None):
                e.pop(i)
                break
            j += 1
        i += 1
    i = 0
    while i < len(e):
        j = i + 1
        while j < len(e):
            if e[i] == e[j]:
                e.pop(j)
                j -= 1
            j += 1
        i += 1
    for i in range(len(e)):
        for j in range(len(e[i])):
            if isinstance(e[i][j], str):
                if e[i][j] == 'нет':
                    e[i][j] = 'N'
                elif e[i][j] == 'да':
                    e[i][j] = 'Y'
                elif '%' in e[i][j]:
                    q = e[i][j].index('%')
                    e[i][j] = e[i][j][:q]
                    e[i][j] = float(e[i][j])
                    e[i][j] /= 100
                    e[i][j] = str(e[i][j])
                    if len(e[i][j]) < 4:
                        e[i][j] += '0'

                elif '@' in e[i][j]:
                    q = e[i][j].index('@')
                    e[i][j] = e[i][j][q+1:]
    return e
