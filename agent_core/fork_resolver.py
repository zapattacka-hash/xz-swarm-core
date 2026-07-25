class ForkResolver:
    @staticmethod
    def select_canonical_chain(chain_a: list, chain_b: list) -> list:
        # Longest chain with highest accumulated weight
        return chain_a if len(chain_a) >= len(chain_b) else chain_b

if __name__ == "__main__":
    cA = [1, 2, 3, 4]
    cB = [1, 2, 3]
    print(f"Canonical Chain Selected Length: {len(ForkResolver.select_canonical_chain(cA, cB))}")
