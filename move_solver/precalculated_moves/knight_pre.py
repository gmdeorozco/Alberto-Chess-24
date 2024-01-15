from bitarray import bitarray
from move_solver.precalculated_moves.utils_precalculated import get_row, is_white

def get_knight_precalculated_b():
    result = dict()
    for a in range(64):
        result[a] = set()
        color = is_white(a)

        if 0 <= a - 10 <= 63 and color != is_white(a-10):
            result[a].add(a-10)

        if 0 <= a + 10 <= 63 and color != is_white(a+10):
            result[a].add(a+10)

        if 0 <= a + 6 <= 63 and color != is_white(a+6):
            result[a].add(a+6)

        if 0 <= a - 6 <= 63 and color != is_white(a-6):
            result[a].add(a-6)

        if 0 <= a - 15 <= 63 and color != is_white(a-15):
            result[a].add(a-15)

        if 0 <= a + 15 <= 63 and color != is_white(a+15):
            result[a].add(a+15)

        if 0 <= a - 17 <= 63 and color != is_white(a-17):
            result[a].add(a-17)

        if 0 <= a + 17 <= 63 and color != is_white(a+17):
            result[a].add(a+17)
    return result

def get_knight_precalculated():
    result = dict()
    for a in range(64):
        
        origin = bitarray(64)
        origin[a] = True
        color = is_white(origin)
        result[a] = list()
        
        plus17 = bitarray(64) 
        plus17 = origin >> 17
        
        minus17 = bitarray(64)
        minus17 = origin << 17
        
        plus15 = bitarray(64)
        plus15 = origin >> 15
        
        minus15 = bitarray(64)
        minus15 = origin << 15
        
        plus10 = bitarray(64)
        plus10 = origin >> 10
        
        minus10 = bitarray(64)
        minus10 = origin << 10
        
        plus6 = bitarray(64)
        plus6 = origin >> 6
        
        minus6 = bitarray(64)
        minus6 = origin << 6
        
        if any(plus17) and is_white(plus17) != color:
            result[a].append( plus17 )
        
        if any(minus17)and is_white(minus17) != color:
            result[a].append( minus17)
        
        if any(plus15)and is_white(plus15) != color:
            result[a].append( plus15 )
            
        if any(minus15)and is_white(minus15) != color:
            result[a].append( minus15)
        
        if any(plus10)and is_white(plus10) != color:
            result[a].append( plus10)
        
        if any(minus10)and is_white(minus10) != color:
            result[a].append( minus10)
            
        if any(plus6)and is_white(plus6) != color:
            result[a].append( plus6)
        
        if any(minus6)and is_white(minus6) != color:
            result[a].append( minus6)
        
    return result