class KademliaDHT:
    @staticmethod
    def xor_distance(node_id1: int, node_id2: int) -> int:
        return node_id1 ^ node_id2

if __name__ == "__main__":
    dht = KademliaDHT()
    dist = dht.xor_distance(0b1010, 0b1100)
    print(f"Kademlia XOR Metric Distance: {dist}")
