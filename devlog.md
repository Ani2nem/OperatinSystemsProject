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






# Feb 20th 2025 - 9:00 am

## Thoughts so fars
- The Logger is done and its working well now
- The Encryption code is done is working fine as of now
- We might need to optimize and recheck this code, but let' start on Driver Program
- Driver program should accept a single command line argument, it will run two NEW processes
- It is the program that brings everything together, we have to use the logger and the encryption programs we built before.
- Need to learn how to do the streams and what pipes are and how to use them in python.
- Our Driver should print a menu of commands and prompt the user
for commands – looping until the quit command is received.
- Every command and its result should be logged too.
-All strings entered to be encrypted or decrypted should be saved in a history
that lasts only for this run.
- The driver program should accept:
   - password - Logger
   - encrypt - Logger
   - decrypt - Logger
   - history - IDK (Show the history)
   - quit - Logger

## Plan for this session
1. Learn about creating new process and what streams are and how to use them in Python.
2. Create and start the implementation for Driver Program:
   - Look above in the thoughts for the reqs. 
3. Try and test the code and check if its valid. 
4. Troubleshoot any integration between program (we might need to fix some encryption and logger code).
5. Once fixed, do another layer of testing to ensure everything is working properly together. (do it unit testing  and integration testing style so we don't miss any cases).
6. Record the progress as you go.
7. Check and ensure it's following and completing all project reqs.
7. Hopefully, get it turned in this session.


## Session Progress

I was not able to make any progress that day, just started learning about creating a new processes and streams in python




# March 7th 2025 - 11:00 am

## Thoughts so fars
- They are on the previous session plans, just follow them

## Plan for this session (from last time)
1. Review the concepts about creating new process and what streams are and how to use them in Python.
2. Create and start the implementation for Driver Program:
   - Look above in the thoughts for the reqs. 
3. Try and test the code and check if its valid. 
4. Troubleshoot any integration between program (we might need to fix some encryption and logger code).
5. Once fixed, do another layer of testing to ensure everything is working properly together. (do it unit testing  and integration testing style so we don't miss any cases).
6. Record the progress as you go.
7. Check and ensure it's following and completing all project reqs.
7. Hopefully, get it turned in this session.

# Learning as I was coding
We can use enumarate to traverse 2 objects in python!
Note to the grader, my mac uses the Python3 commmand and to run on your machine you might have to change it to python (line52 and line55 in driver.py)
My encrpyt is working but the decrypt is giving me a hard time, it's encrypting again, doing a double encrypt
I need to research this problem and I will come back, I'll commit  before I do that
Never mind that was not an issue, I was tweaking
Nope I was not tweaking, it is an issue with decrypt
It was doing that because of the > char.
I don't want to change encryption, so i handled it here.
Added a new parse_encryption_response() function that removes the '>' character from encryption responses
for_decrypt parameter to the get_history_choice() function that shows helpful tips when selecting items for decryption



## Session Progress
1. Ran final tests on the program with different inputs:
- Verified password setting works correctly
- Tested encryption/decryption with various strings
- Confirmed history feature works as expected
- Checked error handling for invalid inputs


2. Created comprehensive README.md with:
- File descriptions and roles
- Running instructions
- Note about python3 vs python command
- Command guide and usage notes


3. Fixed a few minor issues:
- Improved error handling
- Enhanced user feedback for decrypt operations


4. Verified that all project requirements are met:
- Logger formats timestamps correctly
- Encryption implements Vigenère cipher properly
- Driver handles user interaction and history
- All components communicate via pipes


# March 12th 2025 - 1:00 pm

## Thoughts so fars
The Project due date got pushed back but I will complete it now anyway.
Need to do a final check on the code and and the assignment, been a while since I opened this up.

## Plan for this session
Check the assignment instructions and turn in the assignment


## Session Progress
Created a readme file for the TA
Final Test before submission to make sure nothing is broken

## GitHub Link to Repo - 
https://github.com/Ani2nem/OperatinSystemsProject


### DONE!