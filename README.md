# El-Rayan-Password-Generator

Secure, user-friendly password generator built in Python using secrets, string, and SystemRandom for maximum security.
This tool is designed to guide users toward creating strong, safe passwords while offering a clean, interactive experience.

---

Features:

Cryptographically secure password generation
Customizable character counts:
Letters
Digits
Symbols
Built-in input validation
Guarantees at least one uppercase, one lowercase, one digit, and one symbol (when requested)
Secure shuffle using random.SystemRandom()
Friendly guidance for creating strong passwords
Simple and clean Python logic — secure enough for real use.

---

How It Works:

1. User chooses how many:
Letters
Numbers
Symbols

2. The script ensures valid input (only whole numbers).

3. The generator uses:

secrets.choice() for safe randomness
A “guaranteed characters” system for password diversity

4. The password is securely shuffled and displayed.

5. The script reminds the user to store it safely.

---

Example Output

Welcome to the El Rayan Password Generator

Tip: Strong passwords are typically 16 characters or longer!

Your new password is: H4@tW#9pM!

Please store your new password in a secure and private location.

---

( Security Notes )

Passwords are generated using Python’s secrets module, which is designed for security-critical operations.
The script avoids weak randomness like random.choice() during generation.
Users are advised not to store the password using a secure method (encrypted notes, password managers, etc.).

---

🛠 Requirements

Python 3.10+
No external libraries required

---
Credits

Created by Abdallah Elsayed.
License
MIT License - Non-Commercial.
