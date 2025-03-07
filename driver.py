import sys
import os
from subprocess import Popen, PIPE


def print_menu():
    """Print the menu of available commands."""
    print("\nAvailable commands:")
    print("  password - Set the encryption password")
    print("  encrypt  - Encrypt a string")
    print("  decrypt  - Decrypt a string")
    print("  history  - Show command history")
    print("  quit     - Exit the program")


def get_history_choice(history):
    """Display history and get user choice."""

    # base case if there is no history
    if not history:
        print("History is empty.")
        return None
    
    print("\nHistory:")
    # we can use enumarate to traverse 2 objects in python
    for i, item in enumerate(history, 1):
        print(f"{i}. {item}")
    
    while True:
        choice = input("\nEnter number to select from history, or 'n' for new input: ").strip().lower()
        if choice == 'n':
            return None
        try:
            index = int(choice) - 1
            if 0 <= index < len(history):
                return history[index]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'n'.")


def main():
    # Check command line argument, only the log file
    if len(sys.argv) != 2:
        print("Usage: python driver.py <log_file>", file=sys.stderr)
        sys.exit(1)
    
    log_file = sys.argv[1]
    
    # Start tjej logger process
    logger = Popen(['python3', 'logger.py', log_file], stdin=PIPE, encoding='utf8')
    
    # Start the encryption process
    encryption = Popen(['python3', 'encryption.py'], stdin=PIPE, stdout=PIPE, encoding='utf8')
    
    # Log driver program startex
    logger.stdin.write("START Driver program started.\n")
    logger.stdin.flush()
    
    # Keep track of history in a list
    history = []
    
    print("Welcome to the Encryption System!")
    print_menu()
    
    while True:
        command = input("\nCommand: ").strip().lower()
        
        # Log the command
        logger.stdin.write(f"COMMAND User entered '{command}' command.\n")
        logger.stdin.flush()
        
        if command == "quit":
            # Send QUIT to logger and encryption
            logger.stdin.write("COMMAND Sending QUIT to encryption program.\n")
            logger.stdin.flush()
            encryption.stdin.write("QUIT\n")
            encryption.stdin.flush()
            
            logger.stdin.write("COMMAND Sending QUIT to logger.\n")
            logger.stdin.flush()
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            
            print("Exiting program. Thank you for using the program!")
            break
            
        elif command == "password":
            # Handle password setting
            choice = get_history_choice(history)
            
            if choice is None:
                password = input("Enter new password (letters only): ").strip()
            else:
                password = choice
                print(f"Using '{password}' from history.")
            
            # Send the password to the encryption program and run it
            encryption.stdin.write(f"PASS {password}\n")
            encryption.stdin.flush()
            
            # read the response from the encryption program
            response = encryption.stdout.readline().strip()
            
            if response == "RESULT":
                print("Password set successfully.")
                logger.stdin.write(f"RESULT Password set successfully.\n")
            else:
                print(response)
                logger.stdin.write(f"ERROR {response}\n")
            
            logger.stdin.flush()
            
        elif command == "encrypt":
            # Handle encryption
            choice = get_history_choice(history)
            
            if choice is None:
                text = input("Enter text to encrypt (letters only): ").strip()
                # Add to history only if it's a new input
                if text.isalpha():
                    history.append(text)
            else:
                text = choice
                print(f"Using '{text}' from history.")
            
            # Validate input
            if not text.isalpha():
                print("Error: Input must contain only letters.")
                logger.stdin.write(f"ERROR Input must contain only letters.\n")
                logger.stdin.flush()
                continue
            
            # Send to the encryption program
            encryption.stdin.write(f"ENCRYPT {text}\n")
            encryption.stdin.flush()
            
            # Get the response response
            response = encryption.stdout.readline().strip()
            
            print(response)
            
            # Add the result to the history if it was successful
            if response.startswith("RESULT"):
                result = response.split(maxsplit=1)[1]
                history.append(result)
                logger.stdin.write(f"RESULT Encrypted '{text}' to '{result}'.\n")
            else:
                logger.stdin.write(f"ERROR {response}\n")
            
            logger.stdin.flush()
            
        elif command == "decrypt":
            # Handle the decryption
            choice = get_history_choice(history)
            
            if choice is None:
                text = input("Enter text to decrypt (letters only): ").strip()
                # Add it to the history only if it's a new input, ignore the old ones
                if text.isalpha():
                    history.append(text)
            else:
                text = choice
                print(f"Using '{text}' from history.")
            
            # Validate the input
            if not text.isalpha():
                print("Error: Input must contain only letters.")
                logger.stdin.write(f"ERROR Input must contain only letters.\n")
                logger.stdin.flush()
                continue
            
            # Send to encryption program
            encryption.stdin.write(f"DECRYPT {text}\n")
            encryption.stdin.flush()
            
            # Get response
            response = encryption.stdout.readline().strip()
            
            print(response)
            
            # Add result to history if successful
            if response.startswith("RESULT"):
                result = response.split(maxsplit=1)[1]
                history.append(result)
                logger.stdin.write(f"RESULT Decrypted '{text}' to '{result}'.\n")
            else:
                logger.stdin.write(f"ERROR {response}\n")
            
            logger.stdin.flush()
            
        elif command == "history":
            # Print the history
            if not history:
                print("History is empty.")
            else:
                print("\nHistory:")
                for i, item in enumerate(history, 1):
                    print(f"{i}. {item}")
            
            logger.stdin.write("COMMAND Displayed command history.\n")
            logger.stdin.flush()
            
        else:
            print("Unknown command. Please try again.")
            print_menu()
            logger.stdin.write(f"ERROR Unknown command '{command}'.\n")
            logger.stdin.flush()
    
    # Wait for processes to terminate
    encryption.wait()
    logger.wait()


if __name__ == "__main__":
    main()