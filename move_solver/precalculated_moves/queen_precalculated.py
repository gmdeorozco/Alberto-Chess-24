from bitarray import bitarray
from move_solver.precalculated_moves.bishop_precalculated import get_bishop_precalculated
from move_solver.precalculated_moves.rook_precalculated import get_rook_precalculated

def get_queen_precalculated():
    result = dict()

    for n in range(64):
        bishop = get_bishop_precalculated()
        rook = get_rook_precalculated() 
        combined_set = bishop[n].union(rook[n])
        result[n] = combined_set

    return result

assert len (get_queen_precalculated()[63]) == 21, f'Incorrect it should be 21 targets'