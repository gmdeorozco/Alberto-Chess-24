from bitarray import bitarray

class game_state():
    def __init__(
            self,
            white_pieces,
            black_pieces,
            turn=True,
            cells_attacked = bitarray(64),
            white_castling_kingside = True,
            white_castling_queenside = True,
            black_castling_kingside = True,
            black_queenside_kingside = True,
            en_passant_target = None,
            half_moves = 0,
            full_moves = 0,
            ):
        self.white_pieces = white_pieces
        self.black_pieces = black_pieces
        self.turn = turn
        self.cells_attacked = cells_attacked
        self.white_castling_kingside = white_castling_kingside
        self.white_castling_queenside = white_castling_queenside
        self.black_castling_kingside = black_castling_kingside
        self.black_queenside_kingside = black_queenside_kingside
        self.en_passant_target = en_passant_target
        self.half_moves = half_moves
        self.full_moves = full_moves
    

        
