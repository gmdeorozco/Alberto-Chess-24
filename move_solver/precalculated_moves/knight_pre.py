from bitarray import bitarray
from move_solver.precalculated_moves.utils_precalculated import  is_white

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
        
        if plus17.any() and is_white(plus17) != color:
            result[a].append( plus17 )
        
        if minus17.any() and is_white(minus17) != color:
            result[a].append( minus17)
        
        if plus15.any() and is_white(plus15) != color:
            result[a].append( plus15 )
            
        if minus15.any() and is_white(minus15) != color:
            result[a].append( minus15)
        
        if plus10.any() and is_white(plus10) != color:
            result[a].append( plus10)
        
        if minus10.any() and is_white(minus10) != color:
            result[a].append( minus10)
            
        if plus6.any() and is_white(plus6) != color:
            result[a].append( plus6)
        
        if minus6.any() and is_white(minus6) != color:
            result[a].append( minus6)
        
    return result