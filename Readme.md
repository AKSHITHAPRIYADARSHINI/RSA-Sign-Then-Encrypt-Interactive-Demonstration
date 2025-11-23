# **SHA-256 Name Hash Generator**
---

## **📌 Overview**
The **SHA-256 Name Hash Generator** is a simple Python script that demonstrates the use of cryptographic hashing.  
It prompts the user to enter their name, converts the input into bytes, and applies the **SHA-256 hash algorithm** using Python’s built-in `hashlib` module.  
The final output is a **256-bit (64-character) hexadecimal digest**, representing the cryptographically secure hash of the provided input.

---

## **⚙️ Features**
- Accepts user input (name or any text).
- Converts input into bytes for hashing.
- Computes SHA-256 hash using `hashlib.sha256()`.
- Outputs a 64-character hexadecimal string.
- Demonstrates fundamental cryptographic hashing concepts.

---

## **📘 Algorithm Description (SHA-256)**
The program uses the **SHA-256 (Secure Hash Algorithm, 256-bit)**, a member of the SHA-2 family developed by the NSA.

### **Key Properties of SHA-256:**
- **Deterministic:** Same input always produces the same output.
- **Fixed Output Size:** Always generates a 256-bit hash regardless of input length.
- **One-Way Function:** Infeasible to reverse the hash to retrieve the original input.
- **Collision Resistance:** Extremely unlikely for two different inputs to produce identical hashes.
- **Avalanche Effect:** A small change in input drastically changes the hash.

### **Algorithm Steps (As Per Program Implementation):**
1. User enters a name or string.
2. The input string is encoded into bytes using UTF-8.
3. The byte string is passed to `hashlib.sha256()`.
4. The SHA-256 hashing algorithm processes the input.
5. The resulting hash is converted to a readable hexadecimal string using `.hexdigest()`.
6. The hash is displayed to the user.

---

## **📂 File Description**
### **`sha256_name.py`**
A Python script that:
- Requests user input
- Generates the SHA-256 hash
- Prints the hash in hexadecimal format

---

## **▶️ How to Run**
Follow these steps to execute the program on your machine:

### **1. Install Python**
Download from: https://www.python.org/downloads/

Ensure **Add Python to PATH** is selected during installation.

### **2. Open Command Prompt / Terminal**
Windows:
Win + R → type: cmd → Enter

Copy code

### **3. Navigate to the Script Location**
Example:
```bash
cd C:\Users\Dowloads
4. Run the Program
bash
Copy code
python sha256_name.py
5. Enter Your Input
The program will prompt:

yaml
Copy code
Enter your name:
Example Output:

📎 Dependencies
No additional libraries required.
The script uses only Python’s built-in hashlib.

📜 License
This project is created for educational and academic purposes.
You may modify or extend the code as needed.
