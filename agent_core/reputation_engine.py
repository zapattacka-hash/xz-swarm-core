class ReputationEngine:
    def __init__(self):
        self.scores = {}

    def update_score(self, agent_id: str, is_valid: bool):
        current = self.scores.get(agent_id, 1.0)
        self.scores[agent_id] = min(1.0, current + 0.05) if is_valid else max(0.0, current - 0.2)

if __name__ == "__main__":
    rep = ReputationEngine()
    rep.update_score("node-1", True)
    rep.update_score("node-bad", False)
    print(f"Node Scores: {rep.scores}")
