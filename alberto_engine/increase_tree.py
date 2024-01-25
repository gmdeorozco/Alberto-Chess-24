from alberto_engine.engine_logger import append_to_logs
from alberto_engine.get_moves_out_of_node import get_the_moves_out_of_node
from alberto_engine.value_position import value_position
from chess_game import move
from game_state import GameState
from alberto_engine.analisys_node import AnalysisNode
import copy
from move_solver.piece_moves.all_pieces import get_all_possible_pair_moves
from alberto_engine.define_best_lines import define_best_lines

def increase_tree( state:GameState, 
                       depth=1, 
                    parent_node:AnalysisNode=None, 
                    max_depth = 2,
                    is_capture_response = False,
                    lines=6

                    ):
      
        if depth > max_depth:
            return
       
        best_moves_pairs = define_best_lines(state=state,parent_node=parent_node,lines=lines)
        for movement in best_moves_pairs:
            
            origin = movement.origin
            target = movement.target 
            
            n_state = copy.deepcopy(state)
            n_state, captured = move(n_state, origin, target)
            
            val = value_position(n_state)
            this_node = AnalysisNode(origin,target,parent_node,val, not n_state.turn,depth=depth )
            parent_node.children.append(this_node)
            king_captured = False
            valio_la_pena = True
            
            if abs(this_node.value - parent_node.value) >= 500:
                append_to_logs('King Captured, do not analyse more')
                king_captured = True
            
            if is_capture_response and depth >= 2 and captured:
                if this_node.color:
                    if parent_node.parent_node.value - this_node.value > 1:
                        valio_la_pena = False
                else: 
                    if this_node.value - parent_node.parent_node.value > 1:
                        valio_la_pena = False
            
            if not valio_la_pena:
                append_to_logs('No valio la pena, dejar de analizar')
                            
            if captured and depth==max_depth and not king_captured and valio_la_pena and depth<10:
                if depth >= 2: append_to_logs('VALIO LA PENA!!! ' 
                                              + str(round(this_node.value,2)) 
                                              +' vs '
                                              + str(round(parent_node.parent_node.value,2) ))
                
                append_to_logs('Found capture, increasing depth')
                increase_tree(state=n_state,
                               depth = depth+1,
                               parent_node=this_node,
                               max_depth=max_depth+1,
                               is_capture_response= True)
            
            
            if depth == max_depth:
                append_to_logs(get_the_moves_out_of_node(this_node)+ ' eval '+ str(this_node.value) + 'depth='+ str(depth))
            
            
            increase_tree(state=n_state,
                               depth = depth+1,
                               parent_node=this_node,
                               max_depth=max_depth,
                               is_capture_response= False)
           