class EventSourcingStore:
    def __init__(self):
        self.events = []

    def append_event(self, state: list):
        self.events.append(state)

    def replay_state(self) -> list:
        return self.events[-1] if self.events else [1.0, 0.0, 0.0, 0.0]

if __name__ == "__main__":
    es = EventSourcingStore()
    es.append_event([1.0, 0.0, 0.0, 0.0])
    es.append_event([0.707, 0.707, 0.0, 0.0])
    print("Replayed Current State:", es.replay_state())
