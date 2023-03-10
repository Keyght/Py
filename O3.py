import struct

def f31(bt):
    parse_data = struct.unpack('<IHbIIIHIQiHQ', bt[3:50])
    print(parse_data)
    parse_b1 = ()
    for i in range(parse_data[0]):
        parse_b1 = parse_b1 + struct.unpack('<b', bt[parse_data[1]+i:parse_data[1]+i+1])

    q = ''
    for i in range(len(parse_b1)):
        q += chr(parse_b1[i])
    parse_b1 = q                                                                                                        #Для чаров

    parse_c1 = struct.unpack('<qi', bt[parse_data[3]:parse_data[3]+12])
    parse_c2 = struct.unpack('<qi', bt[parse_data[4]:parse_data[4] + 12])
    parse_c3 = struct.unpack('<qi', bt[parse_data[5]:parse_data[5] + 12])
    parse_b4 = struct.unpack('<iqHBIH', bt[parse_data[6]:parse_data[6] + 21])

    parse_b4_mass = ()
    for i in range(parse_b4[4]):
        parse_b4_mass = parse_b4_mass + struct.unpack('<I', bt[parse_b4[5] + i*4:parse_b4[5] + i*4 + 4])                #Для других массивов
    parse_b5 = struct.unpack('<fIIiIHb', bt[parse_data[7]:parse_data[7]+23])

    parse_b5_mass1 = ()
    for i in range(parse_b5[1]):
        parse_b5_mass1 = parse_b5_mass1 + struct.unpack('<f', bt[parse_b5[2] + i*4:parse_b5[2] + i*4 + 4])

    parse_b5_mass2 = ()
    for i in range(parse_b5[4]):
        parse_b5_mass2 = parse_b5_mass2 + struct.unpack('<Q', bt[parse_b5[5] + i * 8:parse_b5[5] + i * 8 + 8])

    return ({
        "A1": {
            "B1": parse_b1,
            "B2": parse_data[2],
            "B3": [{
                "C1": parse_c1[0],
                "C2": parse_c1[1]
                }, {
                "C1": parse_c2[0],
                "C2": parse_c2[1]
                }, {
                "C1": parse_c3[0],
                "C2": parse_c3[1]
                }],
            "B4": {
                "D1": parse_b4[0],
                "D2": parse_b4[1],
                "D3": parse_b4[2],
                "D4": parse_b4[3],
                "D5": list(parse_b4_mass)
            },
            "B5": {
                "E1": parse_b5[0],
                "E2": list(parse_b5_mass1),
                "E3": parse_b5[3],
                "E4": list(parse_b5_mass2),
                "E5": parse_b5[6]
            },
            "B6": parse_data[8],
            "B7": parse_data[9]
        },
        "A2": parse_data[10],
        "A3": parse_data[11]
    })

class C32:
    def __init__(self):#1-trace 2-skid 3-bend 4-fetch 5-code
        self.matrix = [[(0, 1), None, None, None, None], #A
                       [None, (1, 2), None, None, None], #B
                       [None, None, (2, 3), None, None], #C
                       [(3, 4), None, None, None, None], #D
                       [(6, 1), (4, 5), (5, 2), (8, 0), (7, 4)],#E
                       [None, None, None, None, None]] #D
        self.state = 0

    def trace(self):
        result = self.matrix[self.state][0]
        if result is None:
            raise RuntimeError()
        self.state = result[1]
        return  result[0]

    def skid(self):
        result = self.matrix[self.state][1]
        if result is None:
            raise RuntimeError()
        self.state = result[1]
        return  result[0]

    def bend(self):
        result = self.matrix[self.state][2]
        if result is None:
            raise RuntimeError()
        self.state = result[1]
        return  result[0]

    def fetch(self):
        result = self.matrix[self.state][3]
        if result is None:
            raise RuntimeError()
        self.state = result[1]
        return  result[0]

    def code(self):
        result = self.matrix[self.state][4]
        if result is None:
            raise RuntimeError()
        self.state = result[1]
        return  result[0]