
from move_solver.precalculated_moves.utils_precalculated import occupied


class game_state():
    def __init__(
            self,
            white_pieces:list,
            black_pieces:list,
            turn=True,
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
        self.white_castling_kingside = white_castling_kingside
        self.white_castling_queenside = white_castling_queenside
        self.black_castling_kingside = black_castling_kingside
        self.black_queenside_kingside = black_queenside_kingside
        self.en_passant_target = en_passant_target
        self.half_moves = half_moves
        self.full_moves = full_moves
        
    def __copy__(self):
        # Creating a new instance and copying the attributes
        new_instance = type(self).__new__(self.__class__)
        new_instance.__dict__.update(self.__dict__)
        return new_instance
    
    def __eq__(self, other):
        # Define the equality comparison logic based on your requirements
        return (
            self.black_pieces[0].bits == other.black_pieces[0].bits and
            self.black_pieces[1].bits == other.black_pieces[1].bits and
            self.black_pieces[2].bits == other.black_pieces[2].bits and
            self.black_pieces[3].bits == other.black_pieces[3].bits and
            self.black_pieces[4].bits == other.black_pieces[4].bits and
            self.black_pieces[5].bits == other.black_pieces[5].bits and
            
            self.white_pieces[0].bits == other.white_pieces[0].bits and
            self.white_pieces[1].bits == other.white_pieces[1].bits and
            self.white_pieces[2].bits == other.white_pieces[2].bits and
            self.white_pieces[3].bits == other.white_pieces[3].bits and
            self.white_pieces[4].bits == other.white_pieces[4].bits and
            self.white_pieces[5].bits == other.white_pieces[5].bits 
            
    
        )

        
