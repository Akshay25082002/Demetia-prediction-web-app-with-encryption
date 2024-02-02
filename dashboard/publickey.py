# publickey.py

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os

def generate_and_save_public_key():
    # Generate a key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Get the public key in PEM format
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the public key to a file
    public_key_path = os.path.join(os.path.dirname(__file__), 'public_key.pem')
    with open(public_key_path, 'wb') as f:
        f.write(public_key_bytes)

    return public_key_path
