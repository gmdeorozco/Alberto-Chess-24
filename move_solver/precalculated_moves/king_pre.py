from bitarray import bitarray
from move_solver.precalculated_moves.utils_precalculated import get_row, is_white
from board_cells import column_a, column_h

def get_king_precalculated():
    result = dict()
    for a in range(64):
        result[a] =set()
        origin = bitarray()
        origin[a] = True
        color = is_white(a)

        plus1 = origin[a] >> 1
        plus1 &= ~column_a 
        if plus1.any():
            result[a].add( plus1 )

        minus1 = origin[a] << 1
        minus1 &= ~column_h
        if minus1.any():
            result[a].add(minus1)

        plus8 = origin[a] >> 8
        if plus8.any():
            result[a].add( plus8 )
        
        minus8 = origin[a] << 8
        if minus8.any():
            result[a].add(minus8)

        plus9 = origin[a] >> 9
        if plus9.any():
            plus9 &= ~column_a 
            result[a].add( plus9 )
        
        minus9 = origin[a] << 9
        if minus9.any():
            minus9 &= ~column_h
            result[a].add(minus9)

        plus7 = origin[a] >> 7
        plus7 &= ~column_h
        if plus7.any():
            result[a].add(plus7)
        
        minus7 = origin[a] << 7
        minus7 &= column_a
        if minus7.any():
            result[a].add(minus7)
    return result