from bitarray import bitarray
from alberto_engine.engine_logger import append_to_logs, empty_logs
from alberto_engine.get_moves_out_of_node import get_the_moves_out_of_node
from alberto_engine.value_position import value_position
from board_representation.board_printer import print_bits, print_board
from board_representation.initial_board import get_initial_board
from move_solver.piece_moves.pawn import get_possible_moves_for_white_pawn, get_possible_moves_for_black_pawn
from move_solver.piece_moves.knight import get_possible_moves_for_knight
from move_solver.piece_moves.rook import get_possible_moves_for_rook
from move_solver.piece_moves.bishop import get_possible_moves_for_bishop
from move_solver.piece_moves.queen import get_possible_moves_for_queen
from move_solver.piece_moves.king import get_possible_moves_for_king
from move_solver.piece_moves.all_pieces import get_all_possible_pair_moves
from board_representation.board_cells import center_1, center_2, border_1, border_2, cells
from move_solver.perform_move import move
from game_state.game_state import GameState
from alberto_engine.analisys_node import AnalysisNode
import time
import copy
import random
from move_solver.precalculated_moves.king_pre import get_king_precalculated
from move_solver.precalculated_moves.pawn_pre import get_black_pawn_attack, get_white_pawn_attack
from move_solver.precalculated_moves.utils_precalculated import occupied
from move_solver.precalculated_moves.knight_pre import get_knight_precalculated
from alberto_engine.increase_tree import increase_tree
from alberto_engine.perform_parent_up import perform_parent_up

class Alberto_Engine:
    
    def __init__(self, color:bool=True):
        self.root = AnalysisNode(origin=None,target=None,parent_node=None,value=0.0, color=True,depth=0,name='root')
        self.color = color
        self.node_analized_list =dict()
    
    # SELECT
    def select_move(self, state:GameState):
        empty_logs()
        n_state = copy.deepcopy(state)
        ini = time.time()
        
        self.root.children.clear()
        self.root.color = not n_state.turn
        val = value_position(n_state)
        self.root.value = val 
        self.build_move_tree(self.root, n_state, ini, n_state)
        
        return self.root.best_child.origin, self.root.best_child.target, self.root.best_child.value
    
    
    def build_move_tree(self,node:AnalysisNode,state:GameState, ini,original_state):
        end = time.time()
        if end-ini>30:
            return 
        
        
        append_to_logs('calling evaluate node children')
        increase_tree(state=state,
                    depth=1,
                    parent_node=node,
                    max_depth=2, 
                    is_capture_response=False,
                    lines=1)
        perform_parent_up()
     
        node_path = list()
        self.find_best_node_path(self.root, node_path)

        n_state, node = self.move_move_list(node_path, original_state)
        append_to_logs(f'Best node: {get_the_moves_out_of_node(node)} -> {round(node.value,2)}')
        print('')
        print(f'Best node: {get_the_moves_out_of_node(node)} -> {round(node.value,2)}',end='\r')
        self.build_move_tree(node,n_state, ini,original_state)
        
        
    
    def move_move_list(self, move_list:list, state:GameState):
        state = copy.deepcopy(state)
        for m in move_list:
            state, catured = move(state,m.origin,m.target)
        return state, move_list[-1]
   
    def find_best_node_path(self, node:AnalysisNode, node_list)->list:
        if len(node.children) == 0:
            return node_list
        
        node_list.append(node.best_child)
        self.find_best_node_path(node.best_child,node_list)        
    
    
    
    



