
import copy
from alberto_engine.analisys_node import AnalysisNode
from alberto_engine.engine_logger import append_to_logs
from alberto_engine.get_moves_out_of_node import get_move, get_the_moves_out_of_node
from alberto_engine.value_position import value_position
from board_representation.board_printer import print_bits, print_board
from move_solver.perform_move import move
from game_state.game_state import GameState
from move_solver.piece_moves.all_pieces import get_all_possible_pair_moves


def define_best_lines( state:GameState, parent_node:AnalysisNode, lines=2 ):
    list_of_nodes = list()
    all_moves_pairs = get_all_possible_pair_moves(state)
    for movement in all_moves_pairs:
        
        origin, target = movement
        n_state = copy.deepcopy(state)
        n_state, captured = move(n_state, origin, target)
        
        
        val = value_position(n_state)
        this_node = AnalysisNode(origin,target,None,val, not n_state.turn,depth=parent_node.depth+1 )
        list_of_nodes.append(this_node)
    
    sorted_nodes = sorted(list_of_nodes, key=lambda x: x.value, reverse=True)
    for node in sorted_nodes:
        parent_node.children.append(node)
        node.parent_node = parent_node
        #append_to_logs(f'Possible node: {get_the_moves_out_of_node(node)} -> {round(node.value,2)}')
    return sorted_nodes[:lines]
    