from bitarray import bitarray
from alberto_engine.analisys_node import AnalysisNode
from board_cells import cells


def get_the_moves_out_of_node( node:AnalysisNode):
        node_list = list()
        get_node_list(node,node_list)
        
        move_list = [get_move(x.origin, x.target) for x in node_list]
        
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
    
def get_move( origin:bitarray, target:bitarray):
    return (find_key(cells,origin) + ' ' + find_key(cells,target))
    

def find_key(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None

def get_node_list(node:AnalysisNode, node_list:list):
        if node.depth==1:
            node_list.append(node)
            return node_list.reverse()
        node_list.append(node)
        get_node_list(node.parent_node, node_list)
    