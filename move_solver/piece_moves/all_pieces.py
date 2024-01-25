from bitarray import bitarray 
from game_state import GameState
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.king import get_possible_moves_for_king
from move_solver.piece_moves.knight import get_possible_moves_for_knight
from move_solver.piece_moves.pawn import get_possible_moves_for_black_pawn, get_possible_moves_for_white_pawn
from move_solver.piece_moves.queen import get_possible_moves_for_queen
from move_solver.piece_moves.rook import get_possible_moves_for_rook


def get_all_possible_pair_moves(state:GameState):
    all_moves = list()
    if state.turn:
        # White Pieces
        add_list( state.white_pieces[0].bits, get_possible_moves_for_white_pawn, state, state.turn, all_moves )
        add_list( state.white_pieces[1].bits, get_possible_moves_for_knight, state, state.turn, all_moves )
        add_list( state.white_pieces[2].bits, get_possible_moves_for_bishop, state, state.turn, all_moves )
        add_list( state.white_pieces[3].bits, get_possible_moves_for_rook, state, state.turn, all_moves )
        add_list( state.white_pieces[4].bits, get_possible_moves_for_queen, state, state.turn, all_moves )
        add_list( state.white_pieces[5].bits, get_possible_moves_for_king, state, state.turn, all_moves )
        
    else:
        add_list( state.black_pieces[0].bits, get_possible_moves_for_black_pawn, state, state.turn, all_moves )
        add_list( state.black_pieces[1].bits, get_possible_moves_for_knight, state, state.turn, all_moves )
        add_list( state.black_pieces[2].bits, get_possible_moves_for_bishop, state, state.turn, all_moves )
        add_list( state.black_pieces[3].bits, get_possible_moves_for_rook, state, state.turn, all_moves )
        add_list( state.black_pieces[4].bits, get_possible_moves_for_queen, state, state.turn, all_moves )
        add_list( state.black_pieces[5].bits, get_possible_moves_for_king, state, state.turn, all_moves )
    
    
    return all_moves

def add_list( bits, func_moves, state, color, move_list:list ):
    for ind, bit in enumerate( bits ):
        if bit:
            temp = bitarray(64)
            temp[ind] = True
            moves = func_moves(temp,state,color)
            for move in moves:
                move_list.append((temp,move))
    