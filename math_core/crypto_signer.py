import hmac
import hashlib
import json

class TelemetrySigner:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key.encode('utf-8')

    def sign_payload(self, payload: dict) -> str:
        data = json.dumps(payload, sort_keys=True).encode('utf-8')
        return hmac.new(self.secret_key, data, hashlib.sha256).hexdigest()

    def verify_signature(self, payload: dict, signature: str) -> bool:
        expected = self.sign_payload(payload)
        return hmac.compare_digest(expected, signature)

if __name__ == "__main__":
    signer = TelemetrySigner("xz-labs-secret-key")
    data = {"agent_id": "node-alpha", "state": [1.0, 0.0, 0.0, 0.0]}
    sig = signer.sign_payload(data)
    print(f"Payload Signature: {sig}")
    print(f"Verification Check: {signer.verify_signature(data, sig)}")
