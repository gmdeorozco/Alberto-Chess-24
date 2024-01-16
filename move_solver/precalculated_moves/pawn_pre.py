from bitarray import bitarray
from move_solver.precalculated_moves.utils_precalculated import get_row, is_white
from board_cells import column_h, column_a

def get_white_pawn_precalculated():
    result = dict()
    for a in range(8,64):
        result[a] = list()
        origin = bitarray(64)
        origin[a] = True
        
        if 8 <= a < 16:
            result[a].append( origin >> 16 )
        result[a].append( origin >> 8 )
    return result

def get_white_pawn_attack():
    result = dict()
    for a in range(8,64):
        result[a] = list()
        origin = bitarray(64)
        origin[a] = True
        
        res_7 = bitarray(64)
        res_7 |= origin >> 7
        res_7 &= ~column_h
        
        res_9 = bitarray(64)
        res_9 |= origin >> 9
        res_9 &= ~column_a
        
        if res_7.any():
            result[a].append( res_7 )
        
        if res_9.any():
            result[a].append( res_9 )
    return result

def get_black_pawn_precalculated():
    result = dict()
    for a in range(56):
        result[a] = list()
        origin = bitarray(64)
        origin[a] = True
        
        if 48 <= a < 56:
            result[a].append( origin << 16 )
        result[a].append( origin << 8 )
    return result


def get_black_pawn_attack():
    result = dict()
    for a in range(56):
        result[a] = list()
        origin = bitarray(64)
        origin[a] = True
        
        res_7 = bitarray(64)
        res_7 |= origin << 7
        res_7 &= ~column_a
        
        res_9 = bitarray(64)
        res_9 |= origin << 9
        res_9 &= ~column_h
        
        if res_7.any():
            result[a].append( res_7 )
        
        if res_9.any():
            result[a].append( res_9 )
    return result
