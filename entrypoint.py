#!/usr/bin/env python3
"""Control Flow Flatten — real mini-challenge (control-flow-flatten)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'state-machine-key')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    key = CHALLENGE_KEY or "flat-key"
    flat = f"""# Control-flow flattening state machine
# Correct edge sequence: 0 -> 3 -> 1 -> 4 -> 2 -> 5 (prints key)

STATES = {{
    0: (3, None),
    3: (1, None),
    1: (4, None),
    4: (2, None),
    2: (5, None),
    5: (-1, "{key}"),
}}

def run(path):
    s = 0
    out = []
    for nxt in path:
        if nxt != s:
            return None
        s, val = STATES[s]
        if val:
            return val
    return None

if __name__ == "__main__":
    print(run([0, 3, 1, 4, 2, 5]))
"""
    with open("/challenge/flatten.py", "w") as f:
        f.write(flat)
    obf = " ".join(f"{ord(c):02x}" for c in key)
    with open("/challenge/states.txt", "w") as f:
        f.write(f"# follow states.txt hex after correct path\nKEY_HEX={obf}\n")
    print("Control Flow Flatten: trace flatten.py states; hex in states.txt confirms key.")


if __name__ == "__main__":
    main()
