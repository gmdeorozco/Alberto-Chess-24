from bitarray import bitarray
from move_solver.precalculated_moves.utils_precalculated import get_row, is_white

def get_king_precalculated():
    result = dict()
    for a in range(64):
        result[a] =set()
        color = is_white(a)

        if color != is_white(a+1) and a+1<=63 :
            result[a].add(a+1)

        if color != is_white(a-1) and a-1>=0:
            result[a].add(a-1)

        if color != is_white(a+8) and a+8<=63:
            result[a].add(a+8)
        
        if color != is_white(a-8) and a-8>=0:
            result[a].add(a-8)

        if color == is_white(a+9) and a+9<=63:
            result[a].add(a+9)
        
        if color == is_white(a-9) and a-9>=0:
            result[a].add(a-9)

        if color == is_white(a+7) and a+7<=63:
            result[a].add(a+7)
        
        if color == is_white(a-7) and a-7>=0:
            result[a].add(a-7)
    return result

