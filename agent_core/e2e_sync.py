import base64

def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

if __name__ == "__main__":
    key = b"xz_secret_key"
    msg = b"QUATERNION_STATE_SYNC"
    enc = xor_encrypt_decrypt(msg, key)
    dec = xor_encrypt_decrypt(enc, key)
    print(f"Decrypted Matches Original: {dec == msg}")
