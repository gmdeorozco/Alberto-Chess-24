from bitarray import bitarray
from game_state.game_state import GameState
from move_solver.precalculated_moves.utils_precalculated import occupied
from move_solver.piece_moves.knight import get_possible_moves_for_knight
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.rook import get_possible_moves_for_rook
from move_solver.piece_moves.queen import get_possible_moves_for_queen
from move_solver.piece_moves.king import get_possible_moves_for_king


def get_attacked_bits(state:GameState, origin_bit:bitarray):
    # 1. Define origin Color
    attacked_bits=list()
        
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
        moves = get_possible_moves_for_knight(origin_bit=origin_bit,state=state,color=True)
        enemies = occupied(state.black_pieces)
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & white_bishops == origin_bit:
        moves =  get_possible_moves_for_bishop(origin_bit=origin_bit,state=state,color=True)
        enemies = occupied(state.black_pieces)
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & white_rooks == origin_bit:
        moves =   get_possible_moves_for_rook(origin_bit=origin_bit,state=state,color=True)
        enemies = occupied(state.black_pieces)
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & white_queens == origin_bit:
        moves =    get_possible_moves_for_queen(origin_bit=origin_bit,state=state,color=True)
        enemies = occupied(state.black_pieces)
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & white_kings == origin_bit:
        moves =    get_possible_moves_for_king(origin_bit=origin_bit,state=state,color=True)
        enemies = occupied(state.black_pieces)
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & black_pawns == origin_bit:
        pass
    
    if origin_bit & black_knights == origin_bit:
        moves =   get_possible_moves_for_knight(origin_bit=origin_bit,state=state,color=False)
        enemies = occupied(state.white_pieces )
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & black_bishops == origin_bit:
        moves =  get_possible_moves_for_bishop(origin_bit=origin_bit,state=state,color=False)
        enemies = occupied(state.white_pieces )
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & black_rooks == origin_bit:
        moves =  get_possible_moves_for_rook(origin_bit=origin_bit,state=state,color=False)
        enemies = occupied(state.white_pieces )
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & black_queens == origin_bit:
        moves =  get_possible_moves_for_queen(origin_bit=origin_bit,state=state,color=False)
        enemies = occupied(state.white_pieces )
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
    if origin_bit & black_kings == origin_bit:
        moves =   get_possible_moves_for_king(origin_bit=origin_bit,state=state,color=False)
        enemies = occupied(state.white_pieces )
        return list_of_attacked(moves=moves, enemies=enemies, attacked_bits=attacked_bits)
    
def list_of_attacked(moves:list, enemies:bitarray, attacked_bits:list) -> list:
    for move in moves:
        if move & enemies == move:
            attacked_bits.append(move)
             
    return attacked_bits