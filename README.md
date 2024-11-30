# Hashed-password-cracker

Introduction


-In modern applications, passwords are usually stored as hashed values to improve security. However, weak or outdated hashing algorithms can make passwords susceptible to attacks. This project provides a way to demonstrate how hashed passwords can be cracked using a dictionary-based attack method, where a set of commonly used passwords is hashed and compared to the target hash.

-The tool supports multiple hashing algorithms, including MD5, SHA-1, and SHA-256.

Features

-Hash Identification: Automatically detects the hashing algorithm (MD5, SHA-1, SHA-256).

-Dictionary Attack: Attempts to crack hashed passwords using a list of common passwords.

-User-friendly Interface: Simple text-based interface for ease of use.


Installation

1.Clone the repository:

    git clone https://github.com/yourusername/hashed-password-cracker.git
    cd hashed-password-cracker
 

2.Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows


3.Install dependencies:

    pip install -r requirements.txt


Usage

1.Run the password cracker:

   After setting up the environment, you can run the script:

    python password_cracker.py

2.Input the hash value when prompted:

   You will be asked to enter the hashed password value you wish to crack.


3.View the result:

   If the hash is successfully cracked, the original password will be displayed. If not, the tool will notify you that the hash could not be cracked.


Supported Hashing Algorithms

  The following hashing algorithms are supported:

   1.MD5: Produces a 32-character hash. Known for its speed, but vulnerable to attacks.
   2.SHA-1: Produces a 40-character hash. Previously popular but now considered weak due to collision vulnerabilities.
   3.SHA-256: Produces a 64-character hash. A more secure alternative to MD5 and SHA-1, but still susceptible to brute force attacks if weak passwords are used.

How It Works

1.Hash Identification: The tool checks the length and pattern of the input hash to identify the algorithm used.

2.Cracking Process: Using a dictionary attack method, the tool hashes a list of common passwords and compares them to the input hash.

3.Result: The original password is displayed if a match is found.


EXAMPLE:

    Hash: 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5

    Identified Algorithm: SHA-256

    Cracked Password: qwerty

Fork the repository
Clone your fork
Make changes and commit them
Create a pull request to the main repository
