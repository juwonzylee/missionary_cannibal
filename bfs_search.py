from collections import deque
from state import State
from graph import Node 


def bfs_search(root):
    queue = deque([root])
    test_list = []
    while True:
        if not queue:
            return None
        curr_node = queue.popleft()
        if str(curr_node) in test_list:
            continue
        test_list.append(str(curr_node))

        if curr_node.state.check_answer():
            return curr_node.backchaining()

        for c in curr_node.childrens():
            queue.append(c)

def main():
    start_state = State(3,3,1,"Initial state")
    root = Node(parent=None, state=start_state, depth=0)
    for state in bfs_search(root):
        print(state)

if __name__ == '__main__':
    main()