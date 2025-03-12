# Encryption System Project README
This is my encryption system project that has three main parts: a logger for keeping track of what's happening, an encryption program that uses the Vigenère cipher, and a driver program that ties everything together. The programs talk to each other using pipes in Python's subprocess module.

## Files in this Project

- **driver.py**: This is the main program you'll run. It handles user interaction, keeps a history of what you've typed, and sends stuff to the other programs.

- **encryption.py**: This handles the actual encryption and decryption using the Vigenère cipher. It takes commands from the driver program and sends back results.

- **logger.py**: This writes all the important stuff that happens to a log file with timestamps.

- **mem.py**: Just a simple memory simulator for testing, not really part of the main project.

- **cpu.py**: Goes with mem.py for testing, also not part of the main project.

- **mylog.log**: This is a sample log file showing previous runs of the program.

- **test.log**: Another test log file I used when testing the logger.

## How to Run It

Just run this command:
```
python driver.py <log_file>
```

**NOTE TO GRADER**: My Mac uses the `python3` command instead of just `python`. So if you get errors running it, you might need to change lines 52 and 55 in driver.py from `python3` to `python`. 

## Commands You Can Use

When you run the program, you can use these commands:

- **password** - Set the encryption password
  You can type a new password or pick one from history.
  Passwords must only have letters.

- **encrypt** - Encrypt some text
  You can type new text or use something from history.
  Results get added to history.

- **decrypt** - Decrypt some text
  Works like encrypt but in reverse.

- **history** - See stuff you've used before
  Shows everything you've entered or created.

- **quit** - Exit the program
  Closes everything properly.

## Other Stuff to Know

- The encryption only works with letters (no numbers or spaces)
- Everything is case insensitive
- The program checks for errors and won't let you use invalid inputs
- The history feature is pretty handy for reusing strings
- All important actions get logged with timestamps
- I had to add a parser to handle the '>' character that comes back from the encryption program

I documented my whole development process in the devlog.md file if you want to see how I built this step by step.