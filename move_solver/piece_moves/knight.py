
from bitarray import bitarray
from board_printer import print_bits
from game_state import game_state
from move_solver.precalculated_moves import knight_pre
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy

simple_knight = knight_pre.get_knight_precalculated()
 
def get_possible_moves_for_knight(origin_bit:bitarray, state:game_state, color:bool) -> list:
    """
    Calculate possible moves for a knight based on the origin bitarray and the current board.

    Parameters:
    - origin_bit: The bitarray representing the position of the knight.
    - board: The current state of the chessboard.

    Returns:
    - A list bitarrays representing possible moves for the knight.
    """
    white_occupied = occupied( state.white_pieces )
    black_occupied = occupied( state.black_pieces )
    all_occupied = white_occupied | black_occupied
        
    index = origin_bit.index(True)
    simple_wp = copy.deepcopy(simple_knight[ index ])
    
    if color:
        for i in range(len(simple_wp)-1,-1,-1):
            if (simple_wp[i] & white_occupied).any():
                simple_wp.remove( simple_wp[i]  )
    else:
        for i in range(len(simple_wp)-1,-1,-1):
            if (simple_wp[i] & black_occupied).any():
                simple_wp.remove( simple_wp[i]  )
                
    return simple_wp
    
