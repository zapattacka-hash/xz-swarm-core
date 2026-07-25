class OTELCollectorPipeline:
    def __init__(self, service_name: str = "xz-swarm-core"):
        self.service_name = service_name

    def export_span(self, trace_id: str, name: str) -> dict:
        return {"service": self.service_name, "trace_id": trace_id, "span": name}

if __name__ == "__main__":
    otel = OTELCollectorPipeline()
    print("OTEL Export:", otel.export_span("tr-100", "mesh_consensus"))
