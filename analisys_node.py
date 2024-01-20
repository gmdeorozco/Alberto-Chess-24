from bitarray import bitarray

class AnalysisNode:
    def __init__(self, origin, target, parent_node:'AnalysisNode' = None, value:float=0.0, color = True, depth=0) -> None:
        self.origin = origin
        self.target = target
        self.parent_node = parent_node
        self.value = value
        self.color = color
        self.depth = depth
    
    def parent_up(self, children_value):
        if self.color:
            if children_value < self.value:
                self.value = children_value
        else:
            if children_value > self.value:
                self.value = children_value
                
    def __eq__(self, other):
        # Define the equality comparison logic based on your attributes
        if isinstance(other, AnalysisNode):
            return (
                self.origin == other.origin and
                self.target == other.target and
                self.parent_node == other.parent_node and
                self.value == other.value and
                self.color == other.color and 
                self.depth == other.depth
            )
        return False
    
    
    def __hash__(self):
        # Define the hash function based on your attributes
        return hash((self.origin, self.target, self.parent_node, self.value, self.color, self.depth))
        