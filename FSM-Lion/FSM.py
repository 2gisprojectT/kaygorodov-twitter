class FSM:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.transitions = {}
        self.prev_state = None
        self.action = None

    def add_transition(self, input_word, state, action, next_state=None):
        if next_state is None:
            next_state = state
        self.transitions[(input_word, state)] = (action, next_state)

    def execute(self, input_word):
        if (input_word, self.current_state) not in self.transitions:
            raise Exception("Transition not found")
        else:
            self.prev_state = self.current_state
            (self.action, self.current_state) = self.transitions[input_word, self.current_state]
