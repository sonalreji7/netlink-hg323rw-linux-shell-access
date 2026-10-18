import re
import hashlib
from pathlib import Path

INPUT = Path("rootfs_combined.hex")
OUTPUT = Path("rootfs.squashfs")

START = 0xB4500000
SIZE = 0x521B3F  # Actual SquashFS size
END = START + SIZE

# Match U-Boot md.b output: address followed by 16 hex bytes.
pattern = re.compile(
    r"^\s*([0-9a-fA-F]{8}):\s+"
    r"((?:[0-9a-fA-F]{2}\s+){15}[0-9a-fA-F]{2})"
    r"(?=\s|$)"
)

data = bytearray(SIZE)
seen = bytearray(SIZE)

rows = 0
duplicates = 0
conflicts = 0

with INPUT.open("r", errors="replace") as f:
    for line in f:
        match = pattern.match(line)

        if not match:
            continue

        address = int(match.group(1), 16)
        values = bytes.fromhex(match.group(2))

        if not (START <= address < END):
            continue

        rows += 1

        for i, value in enumerate(values):
            pos = address + i - START

            if pos >= SIZE:
                break

            if seen[pos]:
                duplicates += 1
                if data[pos] != value:
                    conflicts += 1
            else:
                data[pos] = value
                seen[pos] = 1

missing = seen.count(0)

print("\nMissing address ranges:")

ranges = []
start = None

for i, present in enumerate(seen):
    if not present and start is None:
        start = i

    if present and start is not None:
        ranges.append((start, i))
        start = None

if start is not None:
    ranges.append((start, SIZE))

for start, end in ranges:
    print(
        f"0x{START + start:08X} - "
        f"0x{START + end - 1:08X} "
        f"({end - start} bytes)"
    )

print(f"Parsed rows: {rows}")
print(f"Missing bytes: {missing}")
print(f"Duplicate bytes: {duplicates}")
print(f"Conflicting bytes: {conflicts}")

if missing or conflicts:
    print("\nERROR: Dump is incomplete or contains conflicting data.")
    print("Binary was not saved.")
    raise SystemExit(1)

if data[:4] != b"hsqs":
    raise SystemExit("ERROR: Invalid SquashFS signature.")

OUTPUT.write_bytes(data)

sha256 = hashlib.sha256(data).hexdigest()

print("\nConversion successful!")
print(f"Output: {OUTPUT}")
print(f"Size: {len(data):,} bytes")
print(f"SHA-256: {sha256}")
