from move_solver.precalculated_moves.utils_precalculated import get_row, is_white

def get_black_pawn_precalculated():
    result = dict()
    for a in range(64):
        result[a] = set()

        if a - 8 >= 0:
            result[a].add(a - 8)
        
        if get_row(a) == 7:
            result[a].add(a - 16)
    return result

def get_black_pawn_attack():
    result = dict()
    for a in range(64):
        result[a] = set()
        color = is_white(a)

        if a - 9 >= 0 and color == is_white(a-9):
            result[a].add(a-9)

        if a - 7 >= 0 and color == is_white(a-7):
            result[a].add(a-7)
    return result