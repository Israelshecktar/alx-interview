#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Check if a list of integers represents a valid UTF-8 encoding.

    Parameters:
    data (list): A list of integers representing bytes.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Extract the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's to determine bytes length
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # Byte pattern rules
            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if byte starts with "10"
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
