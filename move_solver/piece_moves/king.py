
from bitarray import bitarray
from board_printer import print_bits
from game_state import game_state
from board_cells import get_col
from move_solver.precalculated_moves import king_pre
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy

simple_king = king_pre.get_king_precalculated()
 
def get_possible_moves_for_king(origin_bit:bitarray, state:game_state, color:bool) -> bitarray:
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
    else:
        for i in range(len(simple_k)-1,-1,-1):
            if (simple_k[i] & black_occupied).any():
                simple_k.remove( simple_k[i]  )
                
    return simple_k
    
