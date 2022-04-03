import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class EncryptionManager:
    @staticmethod
    def encrypt(message:str, password:str, salt:str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=64,
            salt=salt.encode(),
            iterations=390000
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        encrypt_func = Fernet(key)
        return encrypt_func.encrypt(message.encode())