from bitarray import bitarray

def get_row(i):
    if i==0:
        return 1
    return i//8 + 1

def is_white( bits ):
    whites = bitarray('0101010110101010010101011010101001010101101010100101010110101010')
    return whites & bits == bits
    

def bitarray_out_of_collection(col:dict,type:str):
    dict_of_bits = dict()
    for key, value in col.items():
        bit = bitarray(64)
        for n in value:
            if key in dict_of_bits:
                dict_of_bits[key][n] = True
            else:
                dict_of_bits[key] = bit
                bit[n] = True
    return dict_of_bits



def occupied( pieces ) -> bitarray:
    combined = bitarray(64)
    for piece in pieces:
        combined |= piece.bits
    return combined
