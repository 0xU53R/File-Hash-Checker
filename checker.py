import hashlib

def get_hash(file_path, algo="sha256"):
    h = hashlib.new(algo)

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)

    return h.hexdigest()


# simple local "malicious hash" database
KNOWN_BAD_HASHES = {
    "e3b0c44298fc1c149afbf4c8996fb924..." : "Test Malware"
}

def check_hash(file_hash):
    if file_hash in KNOWN_BAD_HASHES:
        return f"[MALICIOUS] {KNOWN_BAD_HASHES[file_hash]}"
    return "[OK] File not in local database"
