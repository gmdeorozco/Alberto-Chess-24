
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy

class GameState():
    def __init__(
            self,
            white_pieces=None,
            black_pieces=None,
            turn=True,
            white_castling_kingside=True,
            white_castling_queenside=True,
            black_castling_kingside=True,
            black_castling_queenside=True,  # Fix the parameter name here
            en_passant_target=None,
            half_moves=0,
            full_moves=0,
    ):
        if white_pieces is None:
            self.white_pieces = list()
        else:
            self.white_pieces = white_pieces

        if black_pieces is None:
            self.black_pieces = list()
        else:
            self.black_pieces = black_pieces

        self.turn = turn
        self.white_castling_kingside = white_castling_kingside
        self.white_castling_queenside = white_castling_queenside
        self.black_castling_kingside = black_castling_kingside
        self.black_castling_queenside = black_castling_queenside  # Corrected parameter name
        self.en_passant_target = en_passant_target
        self.half_moves = half_moves
        self.full_moves = full_moves
        
    def __deepcopy__(self, memo):
        # Create a new instance of the class
        new_instance = self.__class__(
            white_pieces=copy.deepcopy(self.white_pieces, memo),
            black_pieces=copy.deepcopy(self.black_pieces, memo),
            turn=self.turn,
            white_castling_kingside=self.white_castling_kingside,
            white_castling_queenside=self.white_castling_queenside,
            black_castling_kingside=self.black_castling_kingside,
            black_castling_queenside=self.black_castling_queenside,
            en_passant_target=copy.deepcopy(self.en_passant_target, memo),
            half_moves=self.half_moves,
            full_moves=self.full_moves
        )
        
        # Add the new instance to memo
        memo[id(self)] = new_instance

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

        
