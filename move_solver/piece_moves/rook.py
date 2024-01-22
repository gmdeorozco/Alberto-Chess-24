
from bitarray import bitarray
from board_printer import print_bits
from game_state import game_state
from board_cells import get_col, get_row
from move_solver.precalculated_moves import rook_pre
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy

simple_rook = rook_pre.get_rook_precalculated()
 
def get_possible_moves_for_rook(origin_bit:bitarray, state:game_state,color:bool) -> bitarray:
    """
    Calculate possible moves for a Chess Rook based on the origin bitarray and the current board.

    Parameters:
    - origin_bit: The bitarray representing the position of the Rook.
    - board: The current state of the chessboard.

    Returns:
    - A list bitarrays representing possible moves for the Rook.
    """
    white_occupied = occupied( state.white_pieces )
    black_occupied = occupied( state.black_pieces )
    
    if color:
        enemy = black_occupied
        friends = white_occupied
    else:
        enemy = white_occupied
        friends = black_occupied
        
    all_occupied = white_occupied | black_occupied
        
    index = origin_bit.index(True)
    
    
    simple_r = copy.deepcopy(simple_rook[ index ])
    for i in range(len(simple_r)-1,-1,-1):
        ind, col_target = get_col(simple_r[i])
        ind, row_target = get_row(simple_r[i])
        
        if (simple_r[i] & friends).any():
            simple_r.remove(simple_r[i])
        else:
        
            if col_target & origin_bit == origin_bit:
                if  obstacled_col(friends, enemy, origin_bit, simple_r[i], color=color):
                    simple_r.remove( simple_r[i]  )
            
            if row_target & origin_bit == origin_bit:
                if obstacled_row(friends, enemy, origin_bit, simple_r[i], color=color ):
                    simple_r.remove( simple_r[i]  )
    
    return simple_r
    
    
def obstacled_col(friends_occupied_bits, enemy_occupied_bits, origin:bitarray, target:bitarray, color:bool):

    obstacled_cells = friends_occupied_bits | enemy_occupied_bits
    result = get_col(origin | target)
    
    if result is not None:
        ind_col, col = result
        # Now you can safely use ind_col and col
    else:
        return True        

    inter_cells = bitarray(64)
    origin_index = origin.index(True)
    target_index = target.index(True)
    
    if origin_index < target_index:
        for i in range( origin.index( True ) + 1, target.index( True ) ):
            inter_cells[i]=True
    else:
        for i in range( target.index( True ) +1 ,origin.index( True )  ):
            inter_cells[i]=True
    
    inter_cells &= col
    
    if (inter_cells & obstacled_cells).any():
        return True
    return False

def obstacled_row(friends_occupied_bits, enemy_occupied_bits, origin:bitarray, target:bitarray, color:bool):

    obstacled_cells = friends_occupied_bits | enemy_occupied_bits
    result = get_row(origin | target)
    if result is not None:
        ind_col, row = result
        # Now you can safely use ind_col and col
    else:
        return True        

    inter_cells = bitarray(64)
    origin_index = origin.index(True)
    target_index = target.index(True)
    
    if origin_index < target_index:
        for i in range( origin.index( True ) + 1, target.index( True ) ):
            inter_cells[i]=True
    else:
        for i in range( target.index( True ) +1 ,origin.index( True )  ):
            inter_cells[i]=True
    
    inter_cells &= row
    
    if (inter_cells & obstacled_cells).any():
        return True
    return False