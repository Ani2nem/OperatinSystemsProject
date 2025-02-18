# Feb 17th 2025 - 12:00 pm

## Thoughts so far, Started the project
- Project needs three components: logger, encryption program, and driver program
- I am deciding to do this in python because it's the easiest way to do it and I;m confortable in python already
- Because it is python I have to use the Subprocess module
- All components will communicate with the use of pipes in Python's subprocess module
- Logger needs to formatted in a certain way for this thing to come out correctly.
- We probably need to format some the messages and stuff.
- We need the current time so we need to use the datetime lib in python.
- Need to ensure proper error handling and file management with try catch so we handle IOExceptions gracefully.

## Plan for this session
1. Check the git repository setup again
2. Download the required python files from blackboard
1. Learn about the functions and how to implement this logger
2. Implement the logger code
3. Test the logger and see if it's valid
4. Plan next steps for encryption program

## Session Progress
- Implemented basic logger program with timestamp formatting
- Testing logging functionality with sample messages, works great!
- Verifying proper file handling and QUIT behavior, perfect!
- Had some problems understanding the datetime functions and had to research how the argv stuff works for command line arguments
- Push the code up to remote



# Feb 18th 2025 - 10:00 am

## Thoughts so far
- Logger is done and we now need to do the Encryption program
- Encryption nees to use Vigenère cipher
- Encryption program needs to handle the commands like PASS, ENCRYPT, DECRYPT, and QUIT
- All encryption/decryption should be case insensitive
- Also need to ensure proper error handling for cases when password isn't set

## Plan for this session
1. Learn about Vigenère cipher implementation
2. Start implementing the encryption program with the following features:
   - First we need to do command parsing (PASS, ENCRYPT, DECRYPT, QUIT)
   - Second we need to do the basic input/output handling
   - Finally we can get error handling for missing password
3. Create basic test cases for the encryption program
4. Do the documentation for it

## Session Progress
- Password setting works smoothly
- Properly warns about missing passwords
- Vigenère encryption/decryption is solid
- Handles all commands and formats responses per spec

Still need to do:
1. Need to build the driver program and it needs to, handle both logger and encryption programs, deal with user interactions, keep track of string history
2. Should test some edge cases (super long strings, weird inputs, etc.)
3. Make sure the pipe communication works perfectly between everything






