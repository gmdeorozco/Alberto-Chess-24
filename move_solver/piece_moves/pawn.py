
from bitarray import bitarray
from board_printer import print_bits
from game_state import game_state
from board_cells import get_col
from move_solver.precalculated_moves import pawn_pre
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy

simple_white_pawn = pawn_pre.get_white_pawn_precalculated()
simple_white_pawn_attack = pawn_pre.get_white_pawn_attack()
simple_black_pawn = pawn_pre.get_black_pawn_precalculated()
simple_black_pawn_attack = pawn_pre.get_black_pawn_attack()
 
def get_possible_moves_for_white_pawn(origin_bit:bitarray, state:game_state) -> bitarray:
    """
    Calculate possible moves for a white pawn based on the origin bitarray and the current board.

    Parameters:
    - origin_bit: The bitarray representing the position of the pawn.
    - board: The current state of the chessboard.

    Returns:
    - A list bitarrays representing possible moves for the white pawn.
    """
    white_occupied = occupied( state.white_pieces )
    black_occupied = occupied( state.black_pieces )
    all_occupied = white_occupied | black_occupied
        
    index = origin_bit.index(True)
    simple_wp = copy.deepcopy(simple_white_pawn[ index ])
    for i in range(len(simple_wp)-1,-1,-1):
        if (
            any (simple_wp[i] & all_occupied) 
            | obstacled_col(white_occupied, black_occupied, origin_bit, simple_wp[i], color=True )
            ):
            simple_wp.remove( simple_wp[i]  )
    
    return simple_wp
    


def get_possible_moves_for_black_pawn(origin_bit:bitarray, state:game_state) -> bitarray:
    """
    Calculate possible moves for a black pawn based on the origin bitarray and the current board.

    Parameters:
    - origin_bit: The bitarray representing the position of the pawn.
    - board: The current state of the chessboard.

    Returns:
    - A list of bitarrays representing possible moves for the black pawn.
    """
    white_occupied = occupied( state.white_pieces )
    black_occupied = occupied( state.black_pieces )
    all_occupied = white_occupied | black_occupied
        
    index = origin_bit.index(True)
    simple_wp = copy.deepcopy(simple_black_pawn[ index ])
    for i in range(len(simple_wp)-1,-1,-1):
        if (
            (simple_wp[i] & all_occupied).any()
            | obstacled_col(black_occupied, white_occupied, origin_bit, simple_wp[i],color=False )
            ):
            simple_wp.remove( simple_wp[i]  )
    
    return simple_wp
    
    
def obstacled_col(friends_occupied_bits, enemy_occupied_bits, origin, target, color):

    obstacled_cells = friends_occupied_bits | enemy_occupied_bits
    ind_col, col = get_col(origin | target)

    inter_cells = bitarray(64)
    if color:
        for i in range( origin.index( True ) + 1, target.index( True ) ):
            inter_cells[i]=True
    else:
        for i in range( target.index( True ) +1 ,origin.index( True )  ):
            inter_cells[i]=True
    
    inter_cells &= col
    
    if any(inter_cells & obstacled_cells):
        return True
    return False