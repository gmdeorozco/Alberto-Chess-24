
from bitarray import bitarray
from board_printer import print_bits
from board_cells import column_a, column_h, add_9_to_diagonal, add_7_to_diagonal, sub_7_to_diagonal, sub_9_to_diagonal


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


