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
from board_cells import center_1, center_2, border_1, border_2, cells
from chess_game import move
from game_state import game_state
from analisys_node import AnalysisNode
import time
import copy

class Alberto_Engine:
    def __init__(self):
        pass

    def value_position(self, state:game_state):
        value=0.0
        white_pieces = state.white_pieces
        black_pieces = state.black_pieces
        

        value += white_pieces[5].bits.count(True)*1000
        value += white_pieces[4].bits.count(True)*9
        
        value -= black_pieces[4].bits.count(True)*9
        value -= black_pieces[5].bits.count(True)*1000
        
        
        w_pawn_bits = white_pieces[0].bits
        value += self.center_value( w_pawn_bits, True)
        
        w_knight_bits = white_pieces[1].bits
        #value += self.space_value(w_knight_bits,get_possible_moves_for_knight,state,True)
        value += self.center_value( w_knight_bits, True)*3
        
        w_bishop_bits = white_pieces[2].bits
        value += self.space_value(w_bishop_bits,get_possible_moves_for_bishop,state,True)
        #value += self.center_value( w_bishop_bits, True)
        
        w_rook_bits = white_pieces[3].bits
        value += self.space_value(w_rook_bits,get_possible_moves_for_rook,state,True)
        #value += self.center_value( w_rook_bits, True)
        
        w_queen_bits = white_pieces[4].bits
        #value += self.space_value(w_queen_bits,get_possible_moves_for_queen,state,True)
        #value += self.center_value( w_queen_bits, True)
    
        
        # Black Space
        b_pawn_bits = black_pieces[0].bits
        value += self.center_value( b_pawn_bits, False)
        
        b_knight_bits = black_pieces[1].bits
        #value -= self.space_value(b_knight_bits,get_possible_moves_for_knight,state,False)
        value += self.center_value( b_knight_bits, False)*3
        
        b_bishop_bits = black_pieces[2].bits
        value -= self.space_value(b_bishop_bits,get_possible_moves_for_bishop,state,False)
        #value += self.center_value( b_bishop_bits, False)
        
        b_rook_bits = black_pieces[3].bits
        value -= self.space_value(b_rook_bits,get_possible_moves_for_rook,state,False)
        #value += self.center_value( b_rook_bits, False)
        
        b_queen_bits = black_pieces[4].bits
        #value -= self.space_value(b_queen_bits,get_possible_moves_for_queen,state,False)
        #value += self.center_value( b_queen_bits, False)

        
        return value
    
    def space_value(self, bits_of_piece, func_moves, state, color):
        val = 0
        for index, piece_bit in enumerate(bits_of_piece):
            if piece_bit == True:
                temp = bitarray(64)
                temp[index] = True
                val += len(func_moves(temp,state,color))*0.15
        return val

    def center_value(self, bits_of_piece, color):
        value = 0
        if color:
            fact = 1
        else:
            fact =-1
        
        value += (bits_of_piece & center_1).count()*0.75 * fact
        value += (bits_of_piece & center_2).count()*0.5 * fact
        value += (bits_of_piece & border_2).count()*0.12 * fact
        return value


    def get_ancestor(self,node:AnalysisNode, color):
        if node.parent_node is None:
            return node.value
        if node.parent_node.parent_node is None and not node.parent_node.color is None and node.parent_node.color == color:
            return node.parent_node.value
        
        return self.get_ancestor(node.parent_node,color)
    

    def recursive_move(self, state:game_state, 
                       depth=1, 
                    parent_node:AnalysisNode=None, 
                    already = [], 
                    count_cropped=0, 
                    list_of_max_depth = [],
                    max_depth = 7,
                    first_chance_done = False,
                    init = None
                    
                    ):
        
        all_moves_pairs = get_all_possible_pair_moves(state)
        for movement in all_moves_pairs:
            
            origin, target = movement
            n_state = copy.deepcopy(state)
            n_state, captured = move(n_state, origin, target)
            
            if n_state not in already:
                already.append(n_state)
            else:
                continue
           
            val = self.value_position(n_state)
            this_node = AnalysisNode(origin,target,parent_node,val, not n_state.turn,depth=depth ) 
            
                       
            if not captured or depth >= max_depth:
                if first_chance_done:   
                    if this_node not in list_of_max_depth:
                        list_of_max_depth.append(this_node)
                        elapsed = time.time()-init
                        print(f'time elapsed: { round(elapsed,3)}',end='\r') 
                        if elapsed > 180:
                            break
                        
                        continue
                else:
                    #print_board(n_state)
                    self.recursive_move(n_state,depth+1,this_node,already, count_cropped, list_of_max_depth, max_depth,True, init)
            else:
                #print('found capture')
                #print_board(n_state)
                self.recursive_move(n_state,depth+1,this_node,already, count_cropped, list_of_max_depth, max_depth,False, init)
        return list_of_max_depth  
        
    def perform_parent_up(self, node:AnalysisNode ):
        if node.depth==1:
            return node
        node.parent_node.parent_up(node.value)
        return self.perform_parent_up(node.parent_node)
    
    def select_move(self, state):
       
        n_state = copy.deepcopy(state)
   
        
        root = AnalysisNode(origin=None,target=None,parent_node=None,value=0.0, color=True,depth=0)
        list_of_max_depth = []
        self.recursive_move(
            state=n_state, 
            depth=1,
            parent_node=root,
            list_of_max_depth=list_of_max_depth,
            max_depth=5,
            first_chance_done = False,
            init=time.time()
            )
        
        list_min_d =[]
            
        for node in list_of_max_depth: 
            min_node = self.perform_parent_up(node)
            '''
            str_max_depth = self.get_string_max_depth(node)
            smd = str_max_depth.split(',')
            
            print(','.join(smd[::-1]))
            '''
            if min_node not in list_min_d:
                list_min_d.append(min_node)
        print(f'tree of {len(list_of_max_depth)} elements')
        if n_state.turn:
            selector = max
        else:
            selector = min
            
        selected_node = selector(list_min_d, key=lambda node: node.value)
        return selected_node.origin, selected_node.target, selected_node.value
    
    def get_string_max_depth(self, node:AnalysisNode )-> str:
        if node.depth == 1:
            return self.get_move(node.origin, node.target)
        return self.get_move(node.origin, node.target) + ',' + self.get_string_max_depth(node.parent_node)
        
        
    def get_move(self, origin:bitarray, target:bitarray):
        return (self.find_key(cells,origin) + ' ' + self.find_key(cells,target))
        
    
    def find_key(self,dictionary, target_value):
        for key, value in dictionary.items():
            if value == target_value:
                return key
        return None




