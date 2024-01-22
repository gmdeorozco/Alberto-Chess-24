from bitarray import bitarray

class AnalysisNode:
    def __init__(self, 
                 origin, target, 
                 parent_node:'AnalysisNode' = None, 
                 value:float=0.0, color = True, 
                 depth=0, open=True, children:list=None, first_chance_done=False) -> None:
        
        self.origin = origin
        self.target = target
        self.parent_node = parent_node
        self.value = value
        self.color = color
        self.depth = depth
        self.open = open
        self.children = children if children is not None else []
        self.first_chance_done = first_chance_done
    
    def parent_up(self, children_value):
        if self.color:
            if children_value < self.value:
                self.value = children_value
                return True
        else:
            if children_value > self.value:
                self.value = children_value
                return True
        return False
                
    def __eq__(self, other):
        # Define the equality comparison logic based on your attributes
        if isinstance(other, AnalysisNode):
            return (
                self.origin == other.origin and
                self.target == other.target and
                self.parent_node == other.parent_node and
                self.value == other.value and
                self.color == other.color and 
                self.depth == other.depth and
                self.open == other.open and
                self.first_chance_done == other.first_chance_done
            )
        return False
    
    
    def __hash__(self):
        # Define the hash function based on your attributes
        return hash((self.origin, self.target, self.parent_node, self.value, self.color, self.depth,self.open,self.first_chance_done))
        