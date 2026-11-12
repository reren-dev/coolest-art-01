#!/usr/bin/env python3
import os
import shutil
import sys

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("Error: MAKEFUN_OUTPUT_DIR environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)
    
    src = os.path.join(os.path.dirname(__file__) or ".", "entry.png")
    dst = os.path.join(output_dir, "entry.png")
    
    # The copy is byte-identical by design
    shutil.copyfile(src, dst)
    
    if os.path.getsize(src) != os.path.getsize(dst):
        print(f"Error: Destination file size does not match source file size.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
