from FSM import FSM


class Lion:
    def __init__(self, initial_state):
        self.FSM = FSM(initial_state)

        self.FSM.add_transition("Antelope", "Hungry", "Eat", "Fed")
        self.FSM.add_transition("Antelope", "Fed", "Sleep", "Hungry")
        self.FSM.add_transition("Hunter", "Hungry", "Run away")
        self.FSM.add_transition("Hunter", "Fed", "Run away", "Hungry")
        self.FSM.add_transition("Tree", "Hungry", "Sleep")
        self.FSM.add_transition("Tree", "Fed", "Look", "Hungry")

    def meet(self, who):
        self.FSM.execute(who)
