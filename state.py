class State(object):
    def __init__(self, missionaries, cannibals, boat, move):
        self.missionary = missionaries
        self.cannibal = cannibals
        self.boat = boat
        self.move = move

    def __str__(self):
        return "%s %s %s %s" %(self.move, self.missionary, self.cannibal, self.boat)
    
    # true 출력시 정답
    def check_answer(self):
        return self.missionary == 0 and self.cannibal == 0 and self.boat == 0

    # true 출력시 가능한 next step
    def possible_answer(self):
        if self.missionary < 0 or self.missionary > 3:
            return False
        if self.cannibal < 0 or self.cannibal > 3:
            return False
        if self.boat > 1 or self.boat < 0:
            return False
        if self.missionary < self.cannibal and self.missionary > 0:
            return False
        if self.missionary > self.cannibal and self.missionary < 3:
            return False 
        return True 

    def next_states(self):
        move = "from left to right"
        if self.boat == 1: # move right, subtract
            op = -1
        else: # move left, add
            op = 1
            move = "from right to left"
        for x in range(3):
            for y in range(3):
                by_move = "Move %s missionaries and %s cannibals %s" %(x, y, move)
                new_state = State(self.missionary + op*x, self.cannibal + op*y, self.boat + op, by_move)
                if x+y >= 1 and x+y <= 2 and new_state.possible_answer():
                    yield new_state