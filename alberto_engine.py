from bitarray import bitarray
from board_printer import print_bits
from initial_board import get_initial_board
from move_solver.piece_moves.pawn import get_possible_moves_for_white_pawn, get_possible_moves_for_black_pawn
from move_solver.piece_moves.knight import get_possible_moves_for_knight
from move_solver.piece_moves.rook import get_possible_moves_for_rook
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.queen import get_possible_moves_for_queen
from move_solver.precalculated_moves.bishop_pre import get_bishop_precalculated
import time

ini = time.time()

state = get_initial_board()
white_pawns = state.white_pieces[0].bits
i = white_pawns.index(True)
origin = bitarray(64)
origin[10]=True
state.black_pieces[0].bits[18]=True

result = get_possible_moves_for_white_pawn( origin_bit=origin,state=state )
#print(len(result))
for res in result:
    #print_bits( res,'white pawn' )
    pass

black_pawns = state.black_pieces[0].bits
i = black_pawns.index(True)
origin = bitarray(64)
origin[49]=True
state.white_pieces[0].bits[41]=True
result = get_possible_moves_for_black_pawn(origin_bit=origin,state=state)
#print(len(result))
for res in result:
    #print_bits( res,'black pawn' )
    pass

origin = bitarray(64)
origin[19]=True
state.white_pieces[0].bits[41]=True

result = get_possible_moves_for_knight(origin_bit=origin,state=state,color=True)
#print(len(result))
for bit in result:
    #print_bits( bit,'knight' )
    pass
    
origin = bitarray(64)
origin[16]=True
result = get_possible_moves_for_rook(origin_bit=origin, state=state,color=True)
#print(len(result))
for bit in result:
    #print_bits( bit,'rook' )
    pass
        

origin = bitarray(64)
origin[16]=True
result = get_possible_moves_for_bishop(origin_bit=origin, state=state,color=True)
#print(len(result))
for bit in result:
    #print_bits( bit,'bishop' )
    pass
    
origin = bitarray(64)
origin[16]=True
result = get_possible_moves_for_queen(origin_bit=origin, state=state,color=True)
print(len(result))
for bit in result:
    print_bits( bit,'queen' )
    pass
end = time.time()
print(end-ini)

