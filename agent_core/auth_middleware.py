import hmac
import hashlib

def generate_simple_token(user_id: str, secret: str) -> str:
    signature = hmac.new(secret.encode('utf-8'), user_id.encode('utf-8'), hashlib.sha256).hexdigest()
    return f"{user_id}.{signature}"

def verify_simple_token(token: str, secret: str) -> bool:
    try:
        user_id, signature = token.split('.')
        expected = hmac.new(secret.encode('utf-8'), user_id.encode('utf-8'), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature)
    except Exception:
        return False

if __name__ == "__main__":
    sec = "xz-master-secret"
    tok = generate_simple_token("zachariah", sec)
    print(f"Generated Auth Token: {tok}")
    print(f"Token Valid Check  : {verify_simple_token(tok, sec)}")
