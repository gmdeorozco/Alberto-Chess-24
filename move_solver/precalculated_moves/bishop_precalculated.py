
from move_solver.precalculated_moves.utils_precalculated import get_row, is_white

def get_bishop_precalculated():
    result = dict()
    for a in range(64):
        result[a] = set()
       
        for row in range(10):
            dist = get_row(a) - row + 1
            if 0 <= a - 9*dist <= 63 and dist!=0 and is_white(a)==is_white(a-9*dist):
                result[a].add(a - 9*dist)
                

            if 0 <= a - 7*dist <= 63 and dist!=0 and is_white(a)==is_white(a-7*dist):
                result[a].add(a - 7*dist)
    
    

    return result




