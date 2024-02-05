
from bitarray import bitarray
from board_representation.board_printer import print_bits
from game_state.game_state import GameState
from board_representation.board_cells import get_col, get_diag
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.rook import get_possible_moves_for_rook
from move_solver.precalculated_moves.utils_precalculated import occupied
import copy
 
def get_possible_moves_for_queen(origin_bit:bitarray, state:GameState,color:bool) -> bitarray:
    """
    Calculate possible moves for a Chess Queen based on the origin bitarray and the current board.

    Parameters:
    - origin_bit: The bitarray representing the position of the Queen.
    - board: The current state of the chessboard.

    Returns:
    - A list bitarrays representing possible moves for the Queen.
    - This is based on the results for Rook and Bishop
    """
    rook = get_possible_moves_for_rook(origin_bit,state,color)
    bishop = get_possible_moves_for_bishop(origin_bit,state,color)
    queen = rook + bishop
    
    return queen