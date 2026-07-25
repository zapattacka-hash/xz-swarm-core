import random

def obfuscate_packet(payload: bytes) -> bytes:
    pad_len = random.randint(4, 16)
    padding = bytes([random.randint(0, 255) for _ in range(pad_len)])
    return bytes([pad_len]) + padding + payload

def deobfuscate_packet(packet: bytes) -> bytes:
    pad_len = packet[0]
    return packet[1 + pad_len:]

if __name__ == "__main__":
    raw = b"TELEMETRY_PACKET"
    obf = obfuscate_packet(raw)
    recovered = deobfuscate_packet(obf)
    print(f"Obfuscated Size: {len(obf)} | Recovered Match: {recovered == raw}")
