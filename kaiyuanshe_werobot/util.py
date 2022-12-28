from passlib.hash import hex_sha256


def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password


def hash_password(password: str) -> str:
    hashed_password = hex_sha256.hash(password)
    return hashed_password
