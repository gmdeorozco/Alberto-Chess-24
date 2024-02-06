
from bitarray import bitarray
from board_representation.board_printer import print_bits
from game_state.game_state import GameState
from board_representation.board_cells import get_col, get_diag, diagonals
from move_solver.precalculated_moves import bishop_pre
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy

simple_bishop = bishop_pre.get_bishop_precalculated()
 
def get_possible_moves_for_bishop(origin_bit:bitarray, state:GameState,color:bool) -> bitarray:
    """
    Calculate possible moves for a Chess Bishop based on the origin bitarray and the current board.

    Parameters:
    - origin_bit: The bitarray representing the position of the Bishop.
    - board: The current state of the chessboard.

    Returns:
    - A list bitarrays representing possible moves for the Bishop.
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
    
    
    simple_b = copy.deepcopy(simple_bishop[ index ])
    diagonals = get_diag(origin_bit)
    
    for i in range(len(simple_b)-1,-1,-1):
        if simple_b[i] & diagonals [0] == simple_b[i]:
            relevant_diagonal = diagonals[0]
            
        if simple_b[i] & diagonals [1] == simple_b[i]:
            relevant_diagonal = diagonals[1]
            
        if (
                (simple_b[i] & friends).any() or  
                ( 
                    obstacled_diag(friends, enemy, origin_bit, simple_b[i], relevant_diagonal, color=color )
                    
                )
            
            ):
           
            simple_b.remove( simple_b[i]  )
    
    return simple_b
    
    
def obstacled_diag(friends_occupied_bits, enemy_occupied_bits, origin:bitarray, target:bitarray, diagonal:bitarray, color:bool):

    obstacled_cells = friends_occupied_bits | enemy_occupied_bits
    if diagonal is None:
        return True

    inter_cells = bitarray(64)
    origin_index = origin.index(True)
    target_index = target.index(True)
    
    if origin_index < target_index:
        for i in range( origin_index + 1, target_index ):
            inter_cells[i]=True
    else:
        for i in range( target.index( True ) + 1 ,origin.index( True )  ):
            inter_cells[i]=True
    
    
    inter_cells &= diagonal
    
        
    if (inter_cells & obstacled_cells).any():
        return True
    return False

