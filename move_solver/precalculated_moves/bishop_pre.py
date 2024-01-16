
from bitarray import bitarray
from board_printer import print_bits
from move_solver.precalculated_moves.utils_precalculated import get_row, is_white
from board_cells import column_a, column_h


def get_bishop_precalculated():
    result = dict()
    for a in range(64):
        result[a] = list()
        origin = bitarray(64)
        origin[a] = True
               
        add_9_to_diagonal(origin=origin,lst=result[a])
        add_7_to_diagonal(origin=origin,lst=result[a])
        sub_9_to_diagonal(origin=origin,lst=result[a])
        sub_7_to_diagonal(origin=origin,lst=result[a])
        
    return result

def add_9_to_diagonal(origin:bitarray, lst:list ):
    plus = origin >> 9
    if plus & column_a == plus:
        return
    if plus.any():
        lst.append(plus)
        add_9_to_diagonal(plus, lst)

def add_7_to_diagonal(origin:bitarray, lst:list ):
    plus = origin >> 7
    if plus & column_h == plus:
        return
    if plus.any():
        lst.append(plus)
        add_7_to_diagonal(plus, lst)

def sub_9_to_diagonal(origin:bitarray, lst:list ):
    minus = origin << 9
    if minus & column_h == minus:
        return
    if minus.any():
        lst.append(minus)
        sub_9_to_diagonal(minus, lst)
  
def sub_7_to_diagonal(origin:bitarray, lst:list ):
    minus = origin << 7
    if minus & column_a == minus:
        return
    if minus.any():
        lst.append(minus)
        sub_7_to_diagonal(minus, lst)
