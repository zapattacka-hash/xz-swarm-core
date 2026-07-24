class GossipMesh:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.peers = set()

    def add_peer(self, peer_id: str):
        if peer_id != self.node_id:
            self.peers.add(peer_id)

    def gossip_state(self) -> dict:
        return {"sender": self.node_id, "known_peers": list(self.peers)}

if __name__ == "__main__":
    node = GossipMesh("node-1")
    node.add_peer("node-2")
    print("Gossip Vector:", node.gossip_state())
