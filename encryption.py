class Encryption:
    # constructor
    def __init__(self):
        self.password = None

    def set_password(self, password):
        """Sets the encryption password. Only alphabetic characters are allowed."""
        if not password.isalpha():
            return False
        self.password = password.upper()
        return True

    def encrypt(self, text):
        """Encrypts the given text using the Vigenère cipher."""
        if not self.password:
            return None

        text = text.upper()
        encrypted_text = []
        password_length = len(self.password)

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.password[i % password_length]) - ord('A')
                encrypted_text.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            else:
                encrypted_text.append(char)

        return ''.join(encrypted_text)

    def decrypt(self, text):
        """Decrypts text that was encrypted using the Vigenère cipher."""
        if not self.password:
            return None

        text = text.upper()
        decrypted_text = []
        password_length = len(self.password)

        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.password[i % password_length]) - ord('A')
                decrypted_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            else:
                decrypted_text.append(char)

        return ''.join(decrypted_text)


def main():
    """Command-line interface for the Vigenère cipher."""
    cipher = Encryption()

    while True:
        try:
            command_line = input("> ").strip()
            if not command_line:
                continue

            parts = command_line.split(maxsplit=1)
            command = parts[0].upper()
            argument = parts[1] if len(parts) > 1 else ""

            if command == "QUIT":
                break

            elif command == "PASS":
                if cipher.set_password(argument):
                    print("RESULT")
                else:
                    print("ERROR: Password must contain only letters.")

            elif command in ("ENCRYPT", "DECRYPT"):
                if not cipher.password:
                    print("ERROR: Password not set.")
                else:
                    result = cipher.encrypt(argument) if command == "ENCRYPT" else cipher.decrypt(argument)
                    print(f"RESULT {result}")

            else:
                print("ERROR: Invalid command.")

        except EOFError:
            break
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
