from state import State

class Node(object):
    def __init__(self, parent, state, depth):
        self.parent = parent
        self.state = state
        self.depth = depth

    def __str__(self):
       return self.state.__str__()
    
    def childrens(self):
        for state in self.state.next_states():
            yield Node(parent=self, state=state, depth=self.depth+1)
    
    def backchaining(self):
        sol = []
        node = self
        sol.append(node)

        while node.parent is not None:
            sol.append(node.parent)
            node = node.parent
        sol.reverse()
        return sol