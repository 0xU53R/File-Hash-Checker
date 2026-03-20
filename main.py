import sys
from checker import get_hash, check_hash

if len(sys.argv) != 2:
    print("Usage: python main.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

print("[*] Calculating hashes...")

md5 = get_hash(file_path, "md5")
sha256 = get_hash(file_path, "sha256")

print(f"MD5: {md5}")
print(f"SHA256: {sha256}")

result = check_hash(sha256)
print(result)
