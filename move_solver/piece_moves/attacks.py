from bitarray import bitarray
from game_state import GameState
from move_solver.precalculated_moves.utils_precalculated import occupied

def get_attacked_bits(state:GameState, origin_bit:bitarray):
    # 1. Define origin Color
        
    white_pawns = state.white_pieces[0].bits
    white_knights = state.white_pieces[1].bits
    white_bishops = state.white_pieces[2].bits
    white_rooks = state.white_pieces[3].bits
    white_queens = state.white_pieces[4].bits
    white_kings = state.white_pieces[5].bits
    
    black_pawns = state.black_pieces[0].bits
    black_knights = state.black_pieces[1].bits
    black_bishops = state.black_pieces[2].bits
    black_rooks = state.black_pieces[3].bits
    black_queens = state.black_pieces[4].bits
    black_kings = state.black_pieces[5].bits
    
    if origin_bit & white_pawns == origin_bit:
        pass
    
    if origin_bit & white_knights == origin_bit:
        pass
    
    if origin_bit & white_bishops == origin_bit:
        pass
    
    if origin_bit & white_rooks == origin_bit:
        pass
    
    if origin_bit & white_queens == origin_bit:
        pass
    
    if origin_bit & white_kings == origin_bit:
        pass
    
    if origin_bit & black_pawns == origin_bit:
        pass
    
    if origin_bit & black_knights == origin_bit:
        pass
    
    if origin_bit & black_bishops == origin_bit:
        pass
    
    if origin_bit & black_rooks == origin_bit:
        pass
    
    if origin_bit & black_queens == origin_bit:
        pass
    
    if origin_bit & black_kings == origin_bit:
        pass