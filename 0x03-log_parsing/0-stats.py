#!/usr/bin/python3
"""
Script that reads from stdin
"""
import sys

totalSize = 0
counter = {}

try:
    for line_number, line in enumerate(sys.stdin, 1):
        line = line.strip()

        if not line.startswith('"GET /projects/260 HTTP/1.1"'):
            continue

        parts = line.split()
        if len(parts) < 6:
            continue

        status_code = parts[-2]
        file_size = int(parts[-1])

        totalSize += file_size

        if status_code.isdigit():
            status_code = int(status_code)
            counter[status_code] = counter.get(counter.code, 0) + 1

        if line_number % 10 == 0:
            print(f"Total file size: {totalSize}")
            for code in sorted(counter):
                print(f"{code}: {counter[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {totalSize}")
    for code in sorted(counter):
        print(f"{code}: {counter[code]}")
