
#2bqk2r/r1p1b2p/2n1pp1n/1p1p2pP/p1PP4/1PN1PN2/PBQ1BPP1/R4K1R w k g6 0 13
from bitarray import bitarray
from board_representation.board_printer import print_board
from game_state.game_state import GameState
from board_representation.board_cells import cells
from board_representation.piece import Piece

def fen_to_state(fen_position:str):
    state = GameState()
    split_by_space = fen_position.split(' ')
    
    active_color = split_by_space[1]
    state.turn = True if active_color=='w' else False
    
    castling_availability = split_by_space[2]
    state.white_castling_kingside = True if 'K' in castling_availability else False
    state.white_castling_queenside = True if 'Q' in castling_availability else False
    state.black_castling_kingside = True if 'k' in castling_availability else False
    state.black_castling_queenside = True if 'q' in castling_availability else False
    
    en_passant_target_square = split_by_space[3]
    if '-' in en_passant_target_square:
        state.en_passant_target = None
    else:
        state.en_passant_target = cells[en_passant_target_square.upper()] 
    
    half_moves = split_by_space[4]
    state.half_moves = half_moves
    
    full_moves = split_by_space[5]
    state.full_moves = full_moves
    
    
    piece_placement = split_by_space[0]
    
    add_pieces(state=state, type='pawn', color=True)
    add_pieces(state=state, type='knight', color=True)
    add_pieces(state=state, type='bishop', color=True)
    add_pieces(state=state, type='rook', color=True)
    add_pieces(state=state, type='queen', color=True)
    add_pieces(state=state, type='king', color=True)
    
    add_pieces(state=state, type='pawn', color=False)
    add_pieces(state=state, type='knight', color=False)
    add_pieces(state=state, type='bishop', color=False)
    add_pieces(state=state, type='rook', color=False)
    add_pieces(state=state, type='queen', color=False)
    add_pieces(state=state, type='king', color=False)
    
    position_pieces(
        fen=piece_placement, 
        state=state
        )
    
        
    return state

def add_pieces(state:GameState, type:str, color:bool):
    bit = bitarray(64)
    piece = Piece(bit,type,color)
    piece_list = state.white_pieces if color else state.black_pieces
    piece_list.append(piece)
    
def position_pieces(fen:str,state:GameState):
    fen_lines = fen.split('/')
    for ind_x, line in enumerate(fen_lines):
        sum_up = 56 - ind_x*8
        pos = sum_up
        for ind_y, char in enumerate(line):
            if char.isdigit():
                pos += int(char)-1
            else:
                #print(f'setting {char} at position {pos}')
                set_piece(piece_str=char,position=pos,state=state)
            pos += 1
            

def set_piece(piece_str:str, position:int,state:GameState):
    if piece_str=='P':
        state.white_pieces[0].bits[position] = True
    elif piece_str=='N':
        state.white_pieces[1].bits[position] = True
    elif piece_str=='B':
        state.white_pieces[2].bits[position] = True
    elif piece_str=='R':
        state.white_pieces[3].bits[position] = True
    elif piece_str=='Q':
        state.white_pieces[4].bits[position] = True
    elif piece_str=='K':
        state.white_pieces[5].bits[position] = True
    elif piece_str=='p':
        state.black_pieces[0].bits[position] = True
    elif piece_str=='n':
        state.black_pieces[1].bits[position] = True
    elif piece_str=='b':
        state.black_pieces[2].bits[position] = True
    elif piece_str=='r':
        state.black_pieces[3].bits[position] = True
    elif piece_str=='q':
        state.black_pieces[4].bits[position] = True
    elif piece_str=='k':
        state.black_pieces[5].bits[position] = True
    

    