#!/usr/bin/python3
import sys
from typing import Dict


def print_statistics(total_size: int, status_codes: Dict[str, int]) -> None:
    print(f"File size: {total_size}")

    for key, val in sorted(status_codes.items(), key=lambda x: x[0]):
        print(f"{key}: {val}")


def main():
    total_file_size = 0
    status_codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    count_read = 0

    try:
        for line in sys.stdin:
            try:
                infos = line[:-1].split()
                curr_size = int(infos[-1])
                total_file_size += curr_size
                code = int(infos[-2])
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1

            except BaseException:
                pass

            count_read += 1

            if count_read == 10:
                print_statistics(total_file_size, status_codes)
                count_read = 0

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes)
        raise

    print_statistics(total_file_size, status_codes)


if __name__ == "__main__":
    main()
