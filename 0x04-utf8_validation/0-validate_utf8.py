#!/usr/bin/python3

"""a method that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    def get_num_bytes_for_next_char(byte):
        # Count the number of leading '1's in the byte to determine
        # the number of bytes in the next character

        if byte & 0x80 == 0:  # If the most significant bit is 0,
            return 1          # it's a 1-byte character

        elif byte & 0xE0 == 0xC0:  # If the three most significant
            return 2               # bits are '110', it's a 2-byte character

        elif byte & 0xF0 == 0xE0:  # If the four most significant
            return 3               # bits are '1110', it's a 3-byte character

        elif byte & 0xF8 == 0xF0:  # If the five most significant
            return 4               # bits are '11110', it's a 4-byte character
        else:
            return 0  # Invalid byte for the start of a character

    i = 0
    while i < len(data):
        num_bytes = get_num_bytes_for_next_char(data[i])

        if num_bytes == 0:
            return False  # Invalid byte found
        elif i + num_bytes > len(data):
            return False  # Incomplete character at the end of the data
        else:
            # Check the continuation bytes
            # (if any) are in the right format (10xxxxxx)
            for j in range(i + 1, i + num_bytes):
                if data[j] & 0xC0 != 0x80:
                    return False  # Invalid continuation byte

        i += num_bytes

    return True
