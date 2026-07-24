import numpy as np

class RecoveryEngine:
    def __init__(self, recovery_threshold: float = 0.1):
        self.recovery_threshold = recovery_threshold

    def evaluate_recovery(self, quarantined_nodes: set, current_states: dict, consensus: np.ndarray) -> set:
        recovered = set()
        for agent_id in quarantined_nodes:
            if agent_id in current_states:
                state = current_states[agent_id]
                dot_prod = np.abs(np.dot(state, consensus))
                drift = 1.0 - np.clip(dot_prod, 0.0, 1.0)
                if drift < self.recovery_threshold:
                    recovered.add(agent_id)
        return recovered

if __name__ == "__main__":
    rec = RecoveryEngine(recovery_threshold=0.05)
    quarantine = {"node-beta"}
    states = {"node-beta": np.array([0.999, 0.001, 0.0, 0.0])}
    consensus = np.array([1.0, 0.0, 0.0, 0.0])
    restored = rec.evaluate_recovery(quarantine, states, consensus)
    print(f"Nodes Cleared for Recovery: {list(restored)}")
