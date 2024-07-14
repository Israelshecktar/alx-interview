#!/usr/bin/python3
import sys
import signal
import re

# Global variables to hold total file size and status code counts
total_file_size = 0
status_code_counts = {}

# Regular expression to match the input format
log_pattern = re.compile(
    r"^\d{1,3}(?:\.\d{1,3}){3} - \[\S+ \S+\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$"
)


# Function to print statistics
def print_statistics():
    global total_file_size, status_code_counts
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))


# Signal handler for keyboard interrupt
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin, process and compute metrics
line_count = 0
for line in sys.stdin:
    match = log_pattern.match(line.strip())
    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        else:
            status_code_counts[status_code] = 1
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

# Print remaining statistics at the end (EOF)
print_statistics()
