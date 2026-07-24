class PrometheusExporter:
    @staticmethod
    def generate_metrics(node_count: int, consensus_norm: float, quarantine_count: int) -> str:
        metrics = [
            "# HELP xz_swarm_active_nodes Number of operational nodes in the cluster.",
            "# TYPE xz_swarm_active_nodes gauge",
            f"xz_swarm_active_nodes {node_count}",
            "# HELP xz_swarm_consensus_norm Magnitude of cluster consensus spinor.",
            "# TYPE xz_swarm_consensus_norm gauge",
            f"xz_swarm_consensus_norm {consensus_norm:.6f}",
            "# HELP xz_swarm_quarantined_nodes Number of Byzantine isolated nodes.",
            "# TYPE xz_swarm_quarantined_nodes gauge",
            f"xz_swarm_quarantined_nodes {quarantine_count}"
        ]
        return "\n".join(metrics) + "\n"

if __name__ == "__main__":
    print(PrometheusExporter.generate_metrics(node_count=3, consensus_norm=1.0000, quarantine_count=0))
