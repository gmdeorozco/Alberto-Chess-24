from bitarray import bitarray

class Piece():
    def __init__(self, bits:bitarray, type:str = 'pawn', color:bool=True ) :
        self.type = type
        self.bits = bits
        self.color = color

