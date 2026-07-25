class AnomalyAggregator:
    @staticmethod
    def calculate_threat_score(drift_rad: float, packet_loss: float, auth_failures: int) -> float:
        score = (drift_rad * 0.5) + (packet_loss * 0.3) + (auth_failures * 0.2)
        return min(1.0, score)

if __name__ == "__main__":
    score = AnomalyAggregator.calculate_threat_score(0.2, 0.05, 1)
    print(f"Aggregated Threat Score: {score:.4f}")
