import uuid
import time

class SwarmTracer:
    def start_span(self, operation_name: str) -> dict:
        return {
            "trace_id": str(uuid.uuid4()),
            "operation": operation_name,
            "start_time": time.time()
        }

    def end_span(self, span: dict) -> float:
        duration = time.time() - span["start_time"]
        return duration

if __name__ == "__main__":
    tracer = SwarmTracer()
    span = tracer.start_span("consensus_calculation")
    time.sleep(0.01)
    duration = tracer.end_span(span)
    print(f"Span '{span['operation']}' finished in {duration:.4f}s")
