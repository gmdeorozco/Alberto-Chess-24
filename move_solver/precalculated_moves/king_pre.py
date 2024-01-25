from bitarray import bitarray
from board_cells import column_a, column_h

def get_king_precalculated():
    result = dict()
    for a in range(64):
        result[a] =list()
        origin = bitarray(64)
        origin[a] = True

        plus1 = origin >> 1
        plus1 &= ~column_a 
        if plus1.any():
            result[a].append( plus1 )

        minus1 = origin << 1
        minus1 &= ~column_h
        if minus1.any():
            result[a].append(minus1)

        plus8 = origin >> 8
        if plus8.any():
            result[a].append( plus8 )
        
        minus8 = origin << 8
        if minus8.any():
            result[a].append(minus8)

        plus9 = origin >> 9
        plus9 &= ~column_a 
        if plus9.any():
            result[a].append( plus9 )
        
        minus9 = origin << 9
        minus9 &= ~column_h
        if minus9.any():
            result[a].append(minus9)

        plus7 = origin >> 7
        plus7 &= ~column_h
        if plus7.any():
            result[a].append(plus7)
        
        minus7 = origin << 7
        minus7 &= ~column_a
        if minus7.any():
            result[a].append(minus7)
    return result

