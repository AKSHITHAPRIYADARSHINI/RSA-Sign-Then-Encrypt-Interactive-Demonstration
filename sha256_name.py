# sha256_name.py
# Computes SHA-256 hash (hex) of a name entered by the user.

import hashlib
import sys

def sha256_hash_name(name: str) -> str:
    h = hashlib.sha256(name.encode('utf-8')).hexdigest()
    return h

def main():
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
    else:
        name = input("Enter your name: ").strip()
    digest = sha256_hash_name(name)
    print(f"SHA-256 hash of '{name}':\n{digest}")

if __name__ == "__main__":
    main()
