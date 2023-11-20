import copy
"""
Usage:
decision = GameDecision(state, agent=agent)
res_state = decision.res_state
terminate = decision.isSuccess(decision.state, agent=agent) >= 1
"""

class GameDecision:
    def __init__(self, state, agent=1, n=3, turns=8):
        """
        :param state: matrix providing state
        :param agent: 1 on behalf of 'x' while 2 on behalf of 'o'
        :param n:  number of rows/cols
        :param turns: turns to terminate
        """
        self.state = state
        self.res_state = None
        self.agent = agent
        self.enemy = 1 if agent == 2 else 2
        self.n = n
        self.turns = turns
        self.nextStep()

    def getNeighbors(self, state, agent):
        """
        :param state: current state
        :param agent: agent in his turn
        :return: all neighbor states
        """
        neighbors = []
        for row in range(self.n):
            for col in range(self.n):
                if state[row][col] == 0:
                    neighbor = copy.deepcopy(state)
                    neighbor[row][col] = agent
                    neighbors.append(neighbor)
        return neighbors

    def isSuccess(self, state, agent):
        val = 0
        # check rows
        for row in range(self.n):
            flag = True
            for col in range(self.n):
                if state[row][col] != agent:
                    flag = False
            if flag:
                val += 1
        # check cols
        for col in range(self.n):
            flag = True
            for row in range(self.n):
                if state[row][col] != agent:
                    flag = False
            if flag:
                val += 1
        # check diagonals
        flag1 = True
        flag2 = True
        for i in range(self.n):
            if state[i][i] != agent:
                flag1 = False
            if state[self.n - 1 - i][i] != agent:
                flag2 = False
        if flag1:
            val += 1
        if flag2:
            val += 1
        return val

    def evaluation(self, state):
        # check success or not
        val = 0
        if state[1][1] == self.agent:
            val += 5
        for row in range(self.n):
            for col in range(self.n):
                if state[row][col] == 0:
                    state[row][col] = self.agent
        val += self.isSuccess(state, self.agent)
        return val
        # if self.successConditions(state, self.enemy) >= 1:
        #     val -= 5
        # if self.successConditions(state, self.agent) >= 1:
        #     val += 10
        # # fill the checkerboard with agent
        # for row in range(self.n):
        #     for col in range(self.n):
        #         if state[row][col] == 0:
        #             state[row][col] = self.agent
        # val += self.successConditions(state, self.agent)

    def filled(self, state):
        flag = True
        for row in range(self.n):
            for col in range(self.n):
                if state[row][col] == 0:
                    flag = False
        return flag

    def min_value(self, state, turns=1):
        if turns == self.turns or self.filled(state):
            return state, self.evaluation(state)
        min_state = []
        min_val = float("inf")
        for neighbor in self.getNeighbors(state, agent=self.enemy):
            if self.isSuccess(neighbor, self.agent):
                return neighbor, 10
            if self.isSuccess(neighbor, self.enemy):
                return neighbor, -10
            neighbor_state, neighbor_val = self.max_value(neighbor, turns + 1)
            if neighbor_val < min_val:
                # print(neighbor_state)
                # print(neighbor_val)
                min_state = neighbor
                min_val = neighbor_val
        return min_state, min_val

    def max_value(self, state, turns=1):
        if turns == self.turns or self.filled(state):
            return state, self.evaluation(state)
        max_state = []
        max_val = float("-inf")
        for neighbor in self.getNeighbors(state, agent=self.agent):
            if self.isSuccess(neighbor, self.agent):
                return neighbor, 10
            if self.isSuccess(neighbor, self.enemy):
                return neighbor, -10
            neighbor_state, neighbor_val = self.min_value(neighbor, turns + 1)
            if neighbor_val > max_val:
                # print(neighbor_state)
                # print(neighbor_val)
                max_state = neighbor
                max_val = neighbor_val
        return max_state, max_val

    def nextStep(self):
        self.res_state, temp = self.max_value(self.state)

    def __str__(self):
        return (str(self.res_state[0])+'\n'
                + str(self.res_state[1])+'\n'
                + str(self.res_state[2])+'\n')


# currentState = [[0, 0, 0],
#                 [0, 0, 0],
#                 [0, 0, 0]]
# cnt = 0
# while cnt < 9:
#     agent = 1 if cnt % 2 == 0 else 2
#     AI = GameDecision(currentState, agent=agent)
#     if AI.isSuccess(AI.state, agent=agent):
#         break
#     currentState = AI.res_state
#     print(AI)
#     cnt += 1

