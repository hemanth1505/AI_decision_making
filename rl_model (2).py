import numpy as np

class ReinforcementLearningAgent:
    def __init__(self):
        self.q_table = {}  # Store learned Q-values

    def choose_action(self, state):
        """Choose action based on learned Q-values or exploration"""
        if state not in self.q_table:
            self.q_table[state] = np.random.rand(2)  # Random Q-values
        return np.argmax(self.q_table[state])  # Choose best action

    def update_q_value(self, state, action, reward):
        """Update Q-values based on experience"""
        if state in self.q_table:
            self.q_table[state][action] += 0.1 * (reward - self.q_table[state][action])

# Example usage
if __name__ == "__main__":
    agent = ReinforcementLearningAgent()
    state = "IntrusionDetected"
    action = agent.choose_action(state)
    print(f"Selected Action: {action}")
