from bitarray import bitarray
from move_solver.precalculated_moves.utils_precalculated import get_row, is_white

def get_rook_precalculated():
    result = dict()
    for a in range(64):
        result[a] = set()

        for b in range(a+8,64,8):
            result[a].add(b)

        for c in range(a-8,-1,-8):
            result[a].add(c)

        for d in range(a+1,get_row(a)*8,1):
            result[a].add(d)

        for e in range(a-1,(get_row(a)-1)*8-1,-1):
            result[a].add(e)
        
    return result
