from bitarray import bitarray

class AnalysisNode:
    def __init__(self, origin, target, parent_node:'AnalysisNode' = None, value:float=0.0, color = True) -> None:
        self.origin = origin
        self.target = target
        self.parent_node = parent_node
        self.value = value
        self.color = color
    
    def parent_up(self, children_value):
        if self.color:
            if children_value < self.value:
                self.value = children_value
        else:
            if children_value > self.value:
                self.value = children_value
                