from bitarray import bitarray
from board_representation.board_cells import column_a, column_h
from board_representation.board_printer import print_bits

def get_rook_precalculated():
    result = dict()
    for a in range(64):
        result[a] = list()
        origin = bitarray(64)
        origin[a] = True
        add_1_to_row(origin=origin, lst=result[a])
        sub_1_to_row(origin=origin, lst=result[a])
        add_8_to_row(origin=origin, lst=result[a])
        sub_8_to_row(origin=origin, lst=result[a])

    return result

def add_1_to_row(origin:bitarray, lst:list ):
    plus = origin >> 1
    if plus & column_a == plus:
        return
    if plus.any():
        lst.append(plus)
        add_1_to_row(plus, lst)

def add_8_to_row(origin:bitarray, lst:list ):
    plus = origin >> 8
    
    if plus.any():
        lst.append(plus)
        add_8_to_row(plus, lst)

def sub_1_to_row(origin:bitarray, lst:list ):
    minus = origin << 1
    if minus & column_h == minus:
        return
    if minus.any():
        lst.append(minus)
        sub_1_to_row(minus, lst)

def sub_8_to_row(origin:bitarray, lst:list ):
    minus = origin << 8
    if minus.any():
        lst.append(minus)
        sub_8_to_row(minus, lst)