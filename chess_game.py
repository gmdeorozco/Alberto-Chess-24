import copy
from game_state import GameState
from bitarray import bitarray
from board_printer import print_bits, print_board
from move_solver.piece_moves.pawn import get_possible_moves_for_white_pawn, get_possible_moves_for_black_pawn
from move_solver.piece_moves.knight import get_possible_moves_for_knight
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.rook import get_possible_moves_for_rook
from move_solver.piece_moves.queen import get_possible_moves_for_queen
from move_solver.piece_moves.king import get_possible_moves_for_king
from move_solver.precalculated_moves.utils_precalculated import occupied
from board_cells import row_1, row_8, cells

def move(state:GameState, origin:bitarray, target:bitarray ):
    white_pieces = state.white_pieces
    black_pieces = state.black_pieces
    
    white_occupied = occupied(white_pieces)
    black_occupied = occupied(black_pieces)
    
    if state.turn:
        pawns = white_pieces[0].bits
        knights = white_pieces[1].bits
        bighops = white_pieces[2].bits
        rooks = white_pieces[3].bits
        queens = white_pieces[4].bits
        kings = white_pieces[5].bits
        enemy = black_occupied
    else:
        pawns = black_pieces[0].bits
        knights = black_pieces[1].bits
        bighops = black_pieces[2].bits
        rooks = black_pieces[3].bits
        queens = black_pieces[4].bits
        kings = black_pieces[5].bits
        enemy = white_occupied
    

    #print_bits(knights,'knights')
    if check(bits = origin, piece_bits = pawns):
        moved, g_state, captured = move_attempt(
            origin=origin,
            piece_bits=pawns,
            target=target,
            state=state,
            moves_function = (
                get_possible_moves_for_white_pawn 
                if state.turn
                else get_possible_moves_for_black_pawn 
                ),
            color=state.turn,
                enemy=enemy
            )
        if moved:
            g_state.turn = not g_state.turn
            return g_state, captured
        
    elif check(bits = origin, piece_bits = knights):
        #print('found knight')
        moved, g_state, captured = move_attempt(origin=origin,
                     piece_bits=knights,
                     target=target,
                     state=state,
                     moves_function = get_possible_moves_for_knight,
                    color=state.turn,
                    enemy=enemy)
        if moved:
            g_state.turn = not g_state.turn
            return g_state, captured
        
    
    elif check(bits = origin, piece_bits = bighops):
        moved, g_state, captured = move_attempt(origin=origin,
                     piece_bits=bighops,
                     target=target,
                     state=state,
                     moves_function = get_possible_moves_for_bishop,
                    color=state.turn,
                    enemy=enemy)
        if moved:
            g_state.turn = not g_state.turn
            return g_state, captured
    
    elif check(bits = origin, piece_bits = rooks):
        moved, g_state, captured = move_attempt(origin=origin,
                     piece_bits=rooks,
                     target=target,
                     state=state,
                     moves_function = get_possible_moves_for_rook,
                    color=state.turn,
                    enemy=enemy)
        if moved:
            if g_state.turn:
                if origin & cells['H1'] == origin:
                    g_state.white_castling_kingside = False
                elif origin & cells['A1'] == origin:
                    g_state.white_castling_queenside = False
            else:
                if origin & cells['H8'] == origin:
                    g_state.black_castling_kingside = False
                elif origin & cells['A8'] == origin:
                    g_state.black_castling_queenside = False
                    
            g_state.turn = not g_state.turn
            return g_state, captured
    
    elif check(bits = origin, piece_bits = queens):
        moved, g_state, captured = move_attempt(origin=origin,
                     piece_bits=queens,
                     target=target,
                     state=state,
                     moves_function = get_possible_moves_for_queen,
                    color=state.turn,
                    enemy=enemy)
        if moved:
            g_state.turn = not g_state.turn
            return g_state, captured
    
    elif check(bits = origin, piece_bits = kings):
       
        moved, g_state, captured = move_attempt(origin=origin,
                     piece_bits=kings,
                     target=target,
                     state=state,
                     moves_function = get_possible_moves_for_king,
                    color=state.turn,
                    enemy=enemy)
        if moved:
            #g_state = copy.deepcopy(g_state)
            if g_state.turn:
                if target & cells['G1'] == target:
                    index_h1 = cells['H1'].index(True)
                    index_f1 = cells['F1'].index(True)
                    g_state.white_pieces[3].bits[index_h1] = False
                    g_state.white_pieces[3].bits[index_f1] = True
                elif target & cells['C1'] == target:
                    index_a1 = cells['A1'].index(True)
                    index_d1 = cells['D1'].index(True)
                    g_state.white_pieces[3].bits[index_a1] = False
                    g_state.white_pieces[3].bits[index_d1] = True
                g_state.white_castling_kingside = False
                g_state.white_castling_queenside = False
            else:
                if target & cells['G8'] == target:
                    index_h8 = cells['H8'].index(True)
                    index_f8 = cells['F8'].index(True)
                    g_state.black_pieces[3].bits[index_h8] = False
                    g_state.black_pieces[3].bits[index_f8] = True
                elif target & cells['C8'] == target:
                    index_a8 = cells['A8'].index(True)
                    index_d8 = cells['D8'].index(True)
                    g_state.black_pieces[3].bits[index_a8] = False
                    g_state.black_pieces[3].bits[index_d8] = True
                g_state.black_castling_kingside = False
                g_state.black_castling_queenside = False
                
            g_state.turn = not g_state.turn
            
            return g_state, captured
    
        
def move_attempt(
    
    origin:bitarray, 
    piece_bits:bitarray,
    target:bitarray, 
    state:GameState, 
    moves_function,
    color:bool,
    enemy:bitarray ): 
        
    possible_moves = moves_function( origin_bit=origin,state=state,color=color )
    captured = False
    for move in possible_moves:
        if check(target, move):
            piece_bits[origin.index(True)] = False 
            piece_bits[target.index(True)] = True
            if target & enemy == target:
                captured = True
                remove(target,state)
            
            white_crown = state.white_pieces[0].bits & row_8
            if white_crown.any():
                index = white_crown.index(True)
                state.white_pieces[0].bits[index]=False
                state.white_pieces[4].bits[index]=True
            
            black_crown = state.black_pieces[0].bits & row_1
            if black_crown.any():
                index = black_crown.index(True)
                state.black_pieces[0].bits[index]=False
                state.black_pieces[4].bits[index]=True
                
            return True, state, captured
    return False
    
def check( bits:bitarray, piece_bits:bitarray)-> bool:
        if bits & piece_bits == bits:
            return True
        else:
            return False
        
def remove( bit:bitarray, state:GameState):
    if state.turn:
        for piece in state.black_pieces:
            piece.bits = piece.bits &~ bit
    else:
        for piece in state.white_pieces:
            piece.bits = piece.bits &~ bit
        