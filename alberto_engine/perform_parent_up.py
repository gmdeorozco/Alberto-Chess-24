from alberto_engine.get_moves_out_of_node import get_the_moves_out_of_node
from alberto_engine.analisys_node import AnalysisNode
from alberto_engine.engine_logger import append_to_logs

def perform_parent_up():
    
    for depth in sorted(AnalysisNode.all_nodes.keys(), reverse=True):
        nodes_at_depth = AnalysisNode.all_nodes[depth]

        for node in nodes_at_depth:
            if  len(node.children) > 0:
                selector = min if node.color else max
                
                selected_value = selector([child.value for child in node.children])

                for child in node.children:
                    if child.value == selected_value:
                        node.best_child = child
                        node.value = selected_value
                    
                assert not node.best_child == None,'can not be none best child'
            
    
    
    root = AnalysisNode.all_nodes[0][0]
    append_to_logs('PPU '+root.name)
    rev = False if root.color else True
    
    root_children = root.children
    
    sorted_root_children = sorted(root_children, key=lambda x: x.value, reverse=rev )
    
    for ch in sorted_root_children:
        append_to_logs(get_the_moves_out_of_node(ch)+' '+str(ch.value))


        
            
      