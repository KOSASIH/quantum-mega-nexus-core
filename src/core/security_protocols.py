from cryptography.fernet import Fernet

class SecurityProtocols:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, message):
        """Encrypt a message using Fernet symmetric encryption."""
        return self.cipher.encrypt(message.encode())

    def decrypt(self, encrypted_message):
        """Decrypt a message using Fernet symmetric encryption."""
        return self.cipher.decrypt(encrypted_message).decode()

    def get_key(self):
        """Return the encryption key."""
        return self.key

# Example usage
if __name__ == "__main__":
    protocol = SecurityProtocols()
    message = "Hello, Quantum World!"
    encrypted_message = protocol.encrypt(message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = protocol.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)
