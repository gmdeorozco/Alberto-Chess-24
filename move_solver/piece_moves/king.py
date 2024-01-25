
from bitarray import bitarray
from board_printer import print_bits
from game_state import GameState
from board_cells import get_col, cells
from move_solver.precalculated_moves import king_pre
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy

simple_king = king_pre.get_king_precalculated()
 
def get_possible_moves_for_king(origin_bit:bitarray, state:GameState, color:bool) -> bitarray:
    """
    Calculate possible moves for a King based on the origin bitarray and the current board.

    Parameters:
    - origin_bit: The bitarray representing the position of the King.
    - board: The current state of the chessboard.

    Returns:
    - A list bitarrays representing possible moves for the King.
    """
    white_occupied = occupied( state.white_pieces )
    black_occupied = occupied( state.black_pieces )
    all_occupied = white_occupied | black_occupied
    
        
    index = origin_bit.index(True)
    simple_k = copy.deepcopy(simple_king[ index ])
    
    if color:
        for i in range(len(simple_k)-1,-1,-1):
            if (simple_k[i] & white_occupied).any():
                simple_k.remove( simple_k[i]  )
        
        if index == 4:
            cells_between_castle_kingside = cells['F1'] | cells['G1']
            if not (cells_between_castle_kingside & all_occupied).any() and state.white_castling_kingside:
                simple_k.append(cells['G1'])    
        
            cells_between_castle_queenside = cells['B1'] | cells['C1'] | cells['D1']
            if not (cells_between_castle_queenside & all_occupied).any() and state.white_castling_queenside:
                simple_k.append(cells['C1'])    
            
    else:
        for i in range(len(simple_k)-1,-1,-1):
            if (simple_k[i] & black_occupied).any():
                simple_k.remove( simple_k[i]  )
        
        if index == 60:
            cells_between_castle_kingside = cells['F8'] | cells['G8']
            if not (cells_between_castle_kingside & all_occupied).any() and state.black_castling_kingside:
                simple_k.append(cells['G8'])    
        
            cells_between_castle_queenside = cells['B8'] | cells['C8'] | cells['D8']
            if not (cells_between_castle_queenside & all_occupied).any() and state.black_castling_queenside:
                simple_k.append(cells['C8'])
                
    return simple_k
    
