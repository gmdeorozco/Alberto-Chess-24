from bitarray import bitarray
from board_printer import print_bits, print_board
from initial_board import get_initial_board
from move_solver.piece_moves.pawn import get_possible_moves_for_white_pawn, get_possible_moves_for_black_pawn
from move_solver.piece_moves.knight import get_possible_moves_for_knight
from move_solver.piece_moves.rook import get_possible_moves_for_rook
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.queen import get_possible_moves_for_queen
from move_solver.piece_moves.king import get_possible_moves_for_king
from move_solver.piece_moves.all_pieces import get_all_possible_pair_moves
from board_cells import center_1, center_2, border_1, border_2
from chess_game import move
from game_state import game_state
from analisys_node import AnalysisNode
import time
import copy

def value_position( state:game_state):
    value=0.0
    white_pieces = state.white_pieces
    black_pieces = state.black_pieces
    

    value += white_pieces[5].bits.count(True)*1000
    value += white_pieces[4].bits.count(True)*9
    
    value -= black_pieces[4].bits.count(True)*9
    value -= black_pieces[5].bits.count(True)*1000
    
    
    w_pawn_bits = white_pieces[0].bits
    value += center_value( w_pawn_bits, True)
    
    w_knight_bits = white_pieces[1].bits
    #value += space_value(w_knight_bits,get_possible_moves_for_knight,state,True)
    value += center_value( w_knight_bits, True)*3
    
    w_bishop_bits = white_pieces[2].bits
    value += space_value(w_bishop_bits,get_possible_moves_for_bishop,state,True)
    #value += center_value( w_bishop_bits, True)
    
    w_rook_bits = white_pieces[3].bits
    value += space_value(w_rook_bits,get_possible_moves_for_rook,state,True)
    #value += center_value( w_rook_bits, True)
    
    w_queen_bits = white_pieces[4].bits
    #value += space_value(w_queen_bits,get_possible_moves_for_queen,state,True)
    #value += center_value( w_queen_bits, True)
 
    
    # Black Space
    b_pawn_bits = black_pieces[0].bits
    value += center_value( b_pawn_bits, False)
    
    b_knight_bits = black_pieces[1].bits
    #value -= space_value(b_knight_bits,get_possible_moves_for_knight,state,False)
    value += center_value( b_knight_bits, False)*3
    
    b_bishop_bits = black_pieces[2].bits
    value -= space_value(b_bishop_bits,get_possible_moves_for_bishop,state,False)
    #value += center_value( b_bishop_bits, False)
    
    b_rook_bits = black_pieces[3].bits
    value -= space_value(b_rook_bits,get_possible_moves_for_rook,state,False)
    #value += center_value( b_rook_bits, False)
    
    b_queen_bits = black_pieces[4].bits
    #value -= space_value(b_queen_bits,get_possible_moves_for_queen,state,False)
    #value += center_value( b_queen_bits, False)

    
    return value
    
def space_value(bits_of_piece, func_moves, state, color):
    val = 0
    for index, piece_bit in enumerate(bits_of_piece):
        if piece_bit == True:
            temp = bitarray(64)
            temp[index] = True
            val += len(func_moves(temp,state,color))*0.15
    return val

def center_value(bits_of_piece, color):
    value = 0
    if color:
        fact = 1
    else:
        fact =-1
    
    value += (bits_of_piece & center_1).count()*0.75 * fact
    value += (bits_of_piece & center_2).count()*0.5 * fact
    value += (bits_of_piece & border_2).count()*0.12 * fact
    return value


def get_ancestor(node:AnalysisNode, color):
    if node.parent_node is None:
        return node.value
    if node.parent_node.parent_node is None and not node.parent_node.color is None and node.parent_node.color == color:
        return node.parent_node.value
    
    return get_ancestor(node.parent_node,color)
    

def recursive_move(state:game_state, depth=1, 
                   parent_node:AnalysisNode=None, 
                   already = [], 
                   count_cropped=0, 
                   min_to_eval = 4,
                   max_depth = 8,
                   list_of_max_depth = []):
    
   
    
    all_moves_pairs = get_all_possible_pair_moves(state)
    for movement in all_moves_pairs:
        origin, target = movement
        n_state = copy.deepcopy(state)
        n_state, captured = move(n_state, origin, target)
        if depth == 1 or depth ==2 or depth > min_to_eval:
            val = value_position(n_state)
        else:
            val = 0
        
        this_node = AnalysisNode(origin,target,parent_node,val, not n_state.turn )     
      
        if n_state not in already and depth > min_to_eval:
            already.append(n_state)
        elif depth > min_to_eval:
            #print(len(already), end='\r')
            #print('found --------------------------------------------------------------------', end ='\r')
            count_cropped+=1
            continue
       
        ancestor = get_ancestor(this_node,this_node.color)
        th = 0.60
        
       
            
        if depth == max_depth or not captured:
            if this_node not in list_of_max_depth:
                list_of_max_depth.append(this_node)
            print_board(n_state)
            print(this_node.value)
        else:
            recursive_move(n_state,depth+1,this_node,already, count_cropped, min_to_eval,max_depth, list_of_max_depth)
    return list_of_max_depth  
    
def perform_parent_up( node:AnalysisNode ):
    if node.parent_node.parent_node is None:
        node.parent_node.parent_up(node.value)
        return node
    node.parent_node.parent_up(node.value)
    return perform_parent_up(node.parent_node)
    
ini = time.time()

root = AnalysisNode(origin=None,target=None,parent_node=None,value=0.0, color=True)
state = get_initial_board()

origin = bitarray(64)
origin[11]=True
target = bitarray(64)
target[27] = True

state, captured = move(state,origin,target)

list_max_d = []
list_max_d = recursive_move(state=state, depth=1, parent_node=root, already=list(),min_to_eval=1, max_depth=6, list_of_max_depth=list_max_d)

list_min_d =[]
for node in list_max_d:
    min_node = perform_parent_up(node)
    if min_node not in list_min_d:
        list_min_d.append(min_node)
   
for n in list_min_d:
    print_bits(n.origin,'origin')
    print_bits(n.target,'target')
    print('value:',n.value)
end = time.time()
print('time taken', end-ini)




