from bitarray import bitarray
from game_state.game_state import GameState
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.knight import get_possible_moves_for_knight
from move_solver.piece_moves.queen import get_possible_moves_for_queen
from move_solver.piece_moves.rook import get_possible_moves_for_rook 
from move_solver.piece_moves.pawn import get_possible_moves_for_black_pawn, get_possible_moves_for_white_pawn
from move_solver.precalculated_moves.pawn_pre import get_black_pawn_attack, get_white_pawn_attack
from move_solver.precalculated_moves.utils_precalculated import occupied
from board_representation.board_cells import center_1, center_2, border_2

def value_position( state:GameState):
        value=0.0
        white_pieces = state.white_pieces
        black_pieces = state.black_pieces
        
        value += white_pieces[0].bits.count(True)*1
        value += white_pieces[1].bits.count(True)*3
        value += white_pieces[2].bits.count(True)*3.5
        value += white_pieces[3].bits.count(True)*5
        value += white_pieces[4].bits.count(True)*9
        value += white_pieces[5].bits.count(True)*1000
        
        
        value -= black_pieces[0].bits.count(True)*1
        value -= black_pieces[1].bits.count(True)*3
        value -= black_pieces[2].bits.count(True)*3.5
        value -= black_pieces[3].bits.count(True)*5
        value -= black_pieces[4].bits.count(True)*9
        value -= black_pieces[5].bits.count(True)*1000
        
        
        w_pawn_bits = white_pieces[0].bits
        value += center_value( w_pawn_bits, True)
        value += space_value(w_pawn_bits,get_possible_moves_for_white_pawn,state,True)
        
        w_knight_bits = white_pieces[1].bits
        value += space_value(w_knight_bits,get_possible_moves_for_knight,state,True)
        value += center_value( w_knight_bits, True)
        
        w_bishop_bits = white_pieces[2].bits
        value += space_value(w_bishop_bits,get_possible_moves_for_bishop,state,True)
        value += center_value( w_bishop_bits, True)
        
        w_rook_bits = white_pieces[3].bits
        value += space_value(w_rook_bits,get_possible_moves_for_rook,state,True)
        value += center_value( w_rook_bits, True)
        
        w_queen_bits = white_pieces[4].bits
        #value += space_value(w_queen_bits,get_possible_moves_for_queen,state,True)
        #value += center_value( w_queen_bits, True)
    
        
        # Black Space
        b_pawn_bits = black_pieces[0].bits
        value -= center_value( b_pawn_bits, False)
        value -= space_value(w_pawn_bits,get_possible_moves_for_black_pawn,state,False)
        
        b_knight_bits = black_pieces[1].bits
        value -= space_value(b_knight_bits,get_possible_moves_for_knight,state,False)
        value -= center_value( b_knight_bits, False)
        
        
        b_bishop_bits = black_pieces[2].bits
        value -= space_value(b_bishop_bits,get_possible_moves_for_bishop,state,False)
        value -= center_value( b_bishop_bits, False)

        
        b_rook_bits = black_pieces[3].bits
        value -= space_value(b_rook_bits,get_possible_moves_for_rook,state,False)
        value -= center_value( b_rook_bits, False)
        
        b_queen_bits = black_pieces[4].bits
        #value -= space_value(b_queen_bits,get_possible_moves_for_queen,state,False)
        #value -= center_value( b_queen_bits, False)

        value += hanging_pieces_white(white_pieces,state)
        value -= hanging_pieces_black(black_pieces,state)
        
        return value
    
def space_value( bits_of_piece, func_moves, state, color):
    val = 0
    for index, piece_bit in enumerate(bits_of_piece):
        if piece_bit == True:
            temp = bitarray(64)
            temp[index] = True
            val += len(func_moves(temp,state,color))*0.05
            
    return val

def center_value( bits_of_piece, color):
    value = 0
    
    
    value += (bits_of_piece & center_1).count()*0.15
    value += (bits_of_piece & center_2).count()*0.10 
    value += (bits_of_piece & border_2).count()*0.05
    return value


def hanging_pieces_white( white_pieces,state ):
    white_occupied = occupied(white_pieces)
    white_defended = bitarray(64)
    
    wp_att = get_white_pawn_attack()
    for list_bits in wp_att.values():
        for bit in list_bits:
            if bit & white_occupied == bit:
                white_defended |= bit
    
    return white_occupied.count() - white_defended.count() * 0.10

def hanging_pieces_black( black_pieces,state ):
    black_occupied = occupied(black_pieces)
    black_defended = bitarray(64)
    
    bp_att = get_black_pawn_attack()
    for list_bits in bp_att.values():
        for bit in list_bits:
            if bit & black_occupied == bit:
                black_defended |= bit
    
    return black_occupied.count() - black_defended.count() * 0.10
