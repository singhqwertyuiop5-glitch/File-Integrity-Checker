COMPANY   : CODTECH IT SOLUTIONS
NAME      : ADITYA SINGH
INTERN ID : CT04DR3144
DOMAIN    : CYBER SECURITY & ETHICAL HACKING
DURATION  : 4 WEEKS
MENTOR    : NEELA SANTOSH


## File Integrity Checker (Python)
The File Integrity Checker is a simple yet practical Python project that demonstrates how file integrity verification works using cryptographic hashing. This script helps determine whether a file has been modified, intentionally or unintentionally, by comparing its current hash value with a previously stored hash.

File integrity checking is an important concept in cybersecurity, data validation, and software development. It is commonly used to detect unauthorized changes, data corruption, or tampering. This project is designed purely for educational purposes, making it ideal for students, beginners, and anyone learning Python or basic security concepts.

## How It Works
The script uses the SHA-256 hashing algorithm, which produces a fixed-length 256-bit hash value for any input file. Even a tiny change in the file—such as adding or removing a single character—will result in a completely different hash.

The process works in two main steps:
# Hash Generation
The script reads the file in binary mode.
It calculates the SHA-256 hash of the file.
The hash is saved into a separate file (usually with a .hash extension).
# Integrity Verification
When run again, the script recalculates the file’s hash.
It compares the new hash with the saved hash.
If both hashes match, the file is unchanged.
If they differ, the file has been modified.

## Features
Generates a secure SHA-256 hash for any file
Stores the hash in a separate file for future verification
Detects any modification in file content
Simple and clear command-line usage
Uses only Python’s standard library (no external dependencies)
Easy to understand and modify for learning or extension

## Requirements
Python 3.7 or higher
Works on Windows, macOS, and Linux
No additional libraries required

## Project Structure
- file-integrity-checker/
├── file_integrity.py      # Main Python script for integrity checking
├── README.md              # Project documentation
├── test.txt               # Sample file for testing
