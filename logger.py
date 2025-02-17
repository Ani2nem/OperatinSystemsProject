#!/usr/bin/env python3

import sys
from datetime import datetime


class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        
    def log_message(self, message):
        """Log a message with timestamp to the log file"""
        try:
            # Split our message into two peices; action and content using strip method
            parts = message.strip().split(maxsplit=1)
            if len(parts) < 2:
                return
            
            action, content = parts
            
            # Get the current timestamp with datetime lib
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            
            """ Format the log entry
             The log message will be recorded, with a time stamp in 24 hour
            notation, in the log file as a single line using the following
            format:YYYY-MM-DD HH:MM [ACTION] MESSAGE """
            log_entry = f"{timestamp} [{action}] {content}\n"
            
            # Write the content to the log file
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
                f.flush()
                
        except Exception as e:
            print(f"Error logging message: {e}", file=sys.stderr)


def main():
    # Make sure there is an argument for filename in the command line
    if len(sys.argv) != 2:
        print("Usage: python logger.py <log_file>", file=sys.stderr)
        sys.exit(1)
        
    log_file = sys.argv[1]
    logger = Logger(log_file)
    
    # start the logger
    logger.log_message("START Logging Started.")
    
    # Keep reading util we see QUIT in input
    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == "QUIT":
                logger.log_message("STOP Logging Stopped.")
                break
            if line:  # Only processing non-empty lines
                logger.log_message(line)
    except KeyboardInterrupt:
        logger.log_message("STOP Logging Stopped.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
