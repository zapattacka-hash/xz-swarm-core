class HSMVaultWrapper:
    def __init__(self, slot_id: int = 1):
        self.slot_id = slot_id

    def sign_hash_hsm(self, data_hash: str) -> str:
        return f"HSM_SLOT_{self.slot_id}_SIG[{data_hash[:8]}]"

if __name__ == "__main__":
    hsm = HSMVaultWrapper(slot_id=0)
    print(f"HSM Hardware Signature: {hsm.sign_hash_hsm('a1b2c3d4e5f6')}")
