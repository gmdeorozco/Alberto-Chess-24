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
import random
from move_solver.precalculated_moves.pawn_pre import get_black_pawn_attack, get_white_pawn_attack
from move_solver.precalculated_moves.utils_precalculated import occupied
from move_solver.precalculated_moves.knight_pre import get_knight_precalculated

class Alberto_Engine:
    
    def __init__(self, color:bool=True):
        self.root = AnalysisNode(origin=None,target=None,parent_node=None,value=0.0, color=True,depth=0)
        self.color = color
        self.node_analized_list =dict()

    def value_position(self, state:game_state):
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
        value += self.center_value( w_pawn_bits, True)
        
        w_knight_bits = white_pieces[1].bits
        #value += self.space_value(w_knight_bits,get_possible_moves_for_knight,state,True)
        value += self.center_value( w_knight_bits, True)
        
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
        value -= self.center_value( b_pawn_bits, False)
        
        b_knight_bits = black_pieces[1].bits
        #value -= self.space_value(b_knight_bits,get_possible_moves_for_knight,state,False)
        value -= self.center_value( b_knight_bits, False)
        
        
        b_bishop_bits = black_pieces[2].bits
        value -= self.space_value(b_bishop_bits,get_possible_moves_for_bishop,state,False)
        #value += self.center_value( b_bishop_bits, False)

        
        b_rook_bits = black_pieces[3].bits
        value -= self.space_value(b_rook_bits,get_possible_moves_for_rook,state,False)
        
        #value += self.center_value( b_rook_bits, False)
        
        b_queen_bits = black_pieces[4].bits
        #value -= self.space_value(b_queen_bits,get_possible_moves_for_queen,state,False)
        #value += self.center_value( b_queen_bits, False)

        value += self.hanging_pieces_white(white_pieces,state)
        value -= self.hanging_pieces_black(black_pieces,state)
        
        return value
    
    def space_value(self, bits_of_piece, func_moves, state, color):
        val = 0
        for index, piece_bit in enumerate(bits_of_piece):
            if piece_bit == True:
                temp = bitarray(64)
                temp[index] = True
                val += len(func_moves(temp,state,color))*0.10
                
        return val

    def center_value(self, bits_of_piece, color):
        value = 0
        
        
        value += (bits_of_piece & center_1).count()*0.30
        value += (bits_of_piece & center_2).count()*0.20 
        value += (bits_of_piece & border_2).count()*0.10
        return value
    
    
    def hanging_pieces_white(self, white_pieces,state ):
        white_occupied = occupied(white_pieces)
        white_defended = bitarray(64)
        
        wp_att = get_white_pawn_attack()
        for list_bits in wp_att.values():
            for bit in list_bits:
                if bit & white_occupied == bit:
                    white_defended |= bit
       
        return white_occupied.count() - white_defended.count() * 0.25

    def hanging_pieces_black(self, black_pieces,state ):
        black_occupied = occupied(black_pieces)
        black_defended = bitarray(64)
        
        bp_att = get_black_pawn_attack()
        for list_bits in bp_att.values():
            for bit in list_bits:
                if bit & black_occupied == bit:
                    black_defended |= bit
       
        return black_occupied.count() - black_defended.count() * 0.25

    def evaluate_node_children(self, state:game_state, 
                       depth=1, 
                    parent_node:AnalysisNode=None, 
                    ):
        
        all_moves_pairs = get_all_possible_pair_moves(state)
        for movement in all_moves_pairs:
            
            origin, target = movement
            n_state = copy.deepcopy(state)
            n_state, captured = move(n_state, origin, target)
            
            val = self.value_position(n_state)
            this_node = AnalysisNode(origin,target,parent_node,val, not n_state.turn,depth=depth )
            
            if not captured:
                if this_node.first_chance_done: 
                    this_node.open = False  
                else:
                    this_node.first_chance_done = True
                    
            if parent_node is self.root:
                self.append_to_file('adding children to root')
            parent_node.children.append(this_node)
            self.append_to_file(self.get_the_moves_out_of_node(this_node)+ ' eval '+ str(this_node.value))
        self.perform_parent_up(parent_node)
                                   
            
        
        
        
    def perform_parent_up(self, node:AnalysisNode ):
        if node is None:
            return
        
        children = node.children
        if children[0].color:selector = max
        else:selector = min

        selected_val = selector(node.value for node in children )
        node.value = selected_val
        self.perform_parent_up(node.parent_node)
    
    # SELECT
    def select_move(self, state):
        self.empty_file()
        n_state = copy.deepcopy(state)
        ini = time.time()
        
        self.root.children.clear()
        
        self.evaluate_node_children(
            state=state, 
            depth=1,
            parent_node=self.root,
            )
        
        best = self.determine_best_node()
        self.append_to_file('BEST Original '+self.get_move(best.origin, best.target)+ ' eval '+ str(best.value)) 
        #print_bits(best.origin,'first check origin')
        #print_bits(best.target, 'first check target')
        
        
        
        self.search_best(n_state, best, ini,1,8,best,n_state)
        
        
        final_best = self.determine_best_node()
        self.append_to_file('Selected move '+ self.get_the_moves_out_of_node(final_best))
        
        return final_best.origin, final_best.target, final_best.value
    
    def search_best(self, state:game_state,  best:AnalysisNode , ini, rec, max_rec, original_node:AnalysisNode,original_state):
        if time.time() - ini > 30 :
            self.append_to_file('time over')
            return 
        
        if not best.open:
            print('BRANCH ALREADY CALCULATED')
            return 
       
        n_state, captured = move(copy.deepcopy(state),best.origin,best.target)
        print('mimicate movement:')
        print_board(n_state)
        
        self.evaluate_node_children(
            state=n_state, 
            depth=best.depth+1,
            parent_node=best,
            )
         
        if rec >= max_rec: 
            self.append_to_file('reached max REC')
            return
        
        root_best_node = self.determine_best_node(parent_node=self.root)
        if (root_best_node is original_node):
            self.append_to_file('kept original best node '+ str(original_node.value))
            self.append_to_file(self.get_the_moves_out_of_node(original_node))
            
            
            if self.determine_best_node(parent_node=best.parent_node) is best:
                self.append_to_file('kept regular best move')
                n_best = self.determine_best_node(parent_node=best)
                
                self.append_to_file('BEST Kept eval '+str(n_best.value))
                self.append_to_file(self.get_the_moves_out_of_node(n_best))
                self.search_best(n_state,n_best,ini, rec+1, max_rec, original_node,original_state)
                
            else:
                self.append_to_file('did not keep regular best node')
                n_best = self.determine_best_node(parent_node=best.parent_node)
                self.append_to_file('BEST INSTEAD eval '+ str(n_best.value))
                self.append_to_file(self.get_the_moves_out_of_node(n_best))
                self.search_best(state,n_best,ini, rec, max_rec, original_node,original_state)
                
        else:
            self.append_to_file('Did not keep original best node')
            self.append_to_file('BEST Original instead eval '+ str(root_best_node.value))
            self.append_to_file(self.get_the_moves_out_of_node(root_best_node))
            self.search_best(original_state,root_best_node,ini, 1, max_rec, root_best_node,original_state)
            
    
        
    
    def determine_best_node(self, parent_node:AnalysisNode=None) -> AnalysisNode:
        
            
        if parent_node is None:
            self.append_to_file('working with root')
            parent_node = self.root
            
        else: self.append_to_file('normal')
        
        
        children = parent_node.children
        
        if children[0].color:selector = max
        else:selector = min
        
        selected_val = selector(node.value for node in children )
        selected_nodes =  [sel_node for sel_node in children if sel_node.value == selected_val]
        if parent_node is self.root:
            for child in children:
                self.append_to_file(self.get_move(child.origin, child.target) + ' ' + str(child.value))
        
        #return random.choice(selected_nodes)
        return selected_nodes[0]
    
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
    
    def get_node_list(self,node:AnalysisNode, node_list:list):
        if node.depth==1:
            node_list.append(node)
            return node_list.reverse()
        node_list.append(node)
        self.get_node_list(node.parent_node, node_list)
    
    def get_the_moves_out_of_node(self, node:AnalysisNode):
        node_list = list()
        self.get_node_list(node,node_list)
        
        move_list = [self.get_move(x.origin, x.target) for x in node_list]
        
        move_string = ''
        num = 1
        
        if node_list[0].color:
            move_string = move_string + str(num) + '.'+move_list[0].lower() + ' ' + move_list[1].lower() +' '
            num += 1
        else:
            move_string = move_string + str(num) + '. ... '+move_list[0].lower()+' '
           
        
        
        for i in range(num, len(move_list),2):
            num += 1 
            if i+1 < len(move_list):
                move_string = move_string + ' '+str(num) + '.'+move_list[i].lower() + ' ' + move_list[i+1].lower()
            else:
                move_string = move_string + ' '+str(num) + '.'+move_list[i].lower() + '  ...'
                   
        return move_string
    
    def append_to_file( self,text):
        file_path = 'logs.txt'
        try:
            # Try to open the file in append mode
            with open(file_path, 'a') as file:
                # Append a new line with the provided text
                file.write(text + '\n')
        except Exception as e:
            print(f"Error: {e}")
    
    def empty_file(self):
        file_path = 'logs.txt'
        try:
            # Open the file in write mode, which truncates the file
            with open(file_path, 'w'):
                pass  # Using 'with' automatically closes the file
            print(f"The file {file_path} has been emptied.")
        except Exception as e:
            print(f"Error: {e}")




