import hashlib

# Function to identify the hash algorithm based on the hash length and format
def identify_hash_algorithm(hash_value):
    # Check length and pattern of the hash
    if len(hash_value) == 32:
        return "MD5"
    elif len(hash_value) == 40:
        return "SHA-1"
    elif len(hash_value) == 64:
        return "SHA-256"
    elif len(hash_value) == 128:
        return "SHA-512"
    elif hash_value.startswith('$2b$'):
        return "bcrypt"
    else:
        return "Unknown or unsupported hash"

# Function to crack MD5 hashes
def crack_md5_hash(hash_value, wordlist):
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == hash_value:
            return word
    return None

# Function to crack SHA-1 hashes
def crack_sha1_hash(hash_value, wordlist):
    for word in wordlist:
        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
            return word
    return None

# Function to crack SHA-256 hashes
def crack_sha256_hash(hash_value, wordlist):
    for word in wordlist:
        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
            return word
    return None

# Main function to handle the cracking process
def crack_hash(hash_value, wordlist):
    # Identify hash algorithm
    hash_type = identify_hash_algorithm(hash_value)
    print(f"Hash type identified as: {hash_type}")

    # Proceed with cracking based on the identified hash type
    if hash_type == "MD5":
        return crack_md5_hash(hash_value, wordlist)
    elif hash_type == "SHA-1":
        return crack_sha1_hash(hash_value, wordlist)
    elif hash_type == "SHA-256":
        return crack_sha256_hash(hash_value, wordlist)
    else:
        return "Hash type is unsupported or unknown."

# Example usage:
if __name__ == "__main__":
    # Sample hash and wordlist
    hash_value = input("Enter hash to crack: ")  # User inputs the hash they want to crack
    wordlist = ["qwerty", "password", "123456", "admin", "letmein"]  # Example wordlist
    
    # Crack the hash
    result = crack_hash(hash_value, wordlist)
    
    if result:
        print(f"Cracked password: {result}")
    else:
        print("Password not found in wordlist.")
