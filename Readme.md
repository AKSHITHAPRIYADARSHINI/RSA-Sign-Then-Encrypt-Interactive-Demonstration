# **RSA Sign-Then-Encrypt Demo**

---

## **Overview**

This project demonstrates the **RSA digital signature and encryption protocol** in action. It shows how Bob can sign a message with his private key, encrypt the signature under Alice's public key, and how Alice can decrypt and verify the signature's authenticity.

This is a **non-interactive demonstration** with pre-calculated small RSA parameters that clearly shows every step of the cryptographic process.

---

## **What This Program Does**

The program simulates a real-world scenario where:

1. **Bob** wants to send a signed and encrypted message to **Alice**
2. **Bob** signs the message using his private key
3. **Bob** encrypts the signature using Alice's public key
4. **Alice** receives the encrypted signature
5. **Alice** decrypts it using her private key
6. **Alice** verifies the signature using Bob's public key
7. **Alice** confirms the message is authentic and from Bob

All mathematical calculations are displayed in detail so you can follow the complete cryptographic workflow.

---

## **Algorithm Explanation**

### **RSA Sign-Then-Encrypt Protocol**

#### **Step 1: Key Generation (Pre-computed)**

Both Bob and Alice have their RSA key pairs generated:

**Bob's Keys:**
```
Modulus: N_B = p × q = 11 × 13 = 143
Private Exponent: d_B = 103 (computed from φ(N) and e)
Public Exponent: e_B = 7
Euler's Totient: φ(N_B) = (11-1) × (13-1) = 10 × 12 = 120
```

**Alice's Keys:**
```
Modulus: N_A = p × q = 3 × 13 = 39
Private Exponent: d_A = 5 (computed from φ(N) and e)
Public Exponent: e_A = 5
Euler's Totient: φ(N_A) = (3-1) × (13-1) = 2 × 12 = 24
```

#### **Step 2: Bob Signs the Message**

**Formula:**
```
s = M^(d_B) mod N_B
```

**What happens:**
- Bob takes the message M and his private exponent d_B
- He raises M to the power of d_B
- He takes the result modulo his modulus N_B
- This produces a unique signature that only Bob can create

**Example Calculation:**
```
Message: M = 3
Bob's private exponent: d_B = 103
Bob's modulus: N_B = 143

s = 3^103 mod 143 = 16

✓ Signature produced: s = 16
```

**Why this works:**
- Only Bob has his private key d_B
- Therefore, only Bob can produce this signature
- This proves the message came from Bob (AUTHENTICITY)

#### **Step 3: Bob Encrypts the Signature**

**Formula:**
```
c = s^(e_A) mod N_A
```

**What happens:**
- Bob takes the signature s
- He raises it to the power of Alice's public exponent e_A
- He takes the result modulo Alice's modulus N_A
- This encrypts the signature so only Alice can read it

**Example Calculation:**
```
Signature: s = 16
Alice's public exponent: e_A = 5
Alice's modulus: N_A = 39

c = 16^5 mod 39 = 22

✓ Ciphertext produced: c = 22
```

**Why this works:**
- Bob uses Alice's public key (publicly known)
- Only Alice has the corresponding private key d_A
- Only Alice can decrypt this ciphertext
- This provides CONFIDENTIALITY (only Alice can read the signature)

#### **Step 4: Bob Sends the Ciphertext to Alice**

```
Bob → Network → Alice
       c = 22
```

The ciphertext c = 22 is transmitted to Alice over any channel (email, internet, etc.).
- Even if intercepted, no one can decrypt it without Alice's private key

#### **Step 5: Alice Decrypts the Ciphertext**

**Formula:**
```
s' = c^(d_A) mod N_A
```

**What happens:**
- Alice receives the ciphertext c
- She raises it to the power of her private exponent d_A
- She takes the result modulo her modulus N_A
- This reveals the original signature

**Example Calculation:**
```
Ciphertext: c = 22
Alice's private exponent: d_A = 5
Alice's modulus: N_A = 39

s' = 22^5 mod 39 = 16

✓ Signature recovered: s' = 16
```

**Why this works:**
- Only Alice has her private key d_A
- The decryption reverses the encryption
- Alice recovers the original signature

#### **Step 6: Alice Verifies the Signature**

**Formula:**
```
verification = (s')^(e_B) mod N_B
```

**What happens:**
- Alice takes the recovered signature s'
- She raises it to the power of Bob's public exponent e_B
- She takes the result modulo Bob's modulus N_B
- If the result equals the original message M, the signature is valid

**Example Calculation:**
```
Recovered signature: s' = 16
Bob's public exponent: e_B = 7
Bob's modulus: N_B = 143

verification = 16^7 mod 143 = 3

✓ Verification result: 3
```

**Comparison:**
```
Original message M = 3
Verification result = 3

✅ SUCCESS! They match!
The signature is authentic and came from Bob.
```

**Why this works:**
- Bob's public key (e_B, N_B) is publicly known
- If Bob signed the message, then verification will recover the original message
- If the signature was forged or tampered with, verification will produce a different value
- This proves the message hasn't been altered (INTEGRITY)

---

## **Mathematical Foundation**

### **RSA Property (The Magic)**

The key property that makes RSA work:

```
For any message M and RSA key pair (e, d, N):

(M^e mod N)^d mod N = M
(M^d mod N)^e mod N = M

Exponentiation order doesn't matter!
```

**This is why verification works:**

```
Step 2: s = M^(d_B) mod N_B        [Bob signs]
Step 3: c = s^(e_A) mod N_A        [Bob encrypts]
Step 5: s' = c^(d_A) mod N_A       [Alice decrypts]
Step 6: verification = (s')^(e_B) mod N_B  [Alice verifies]

Substituting:
verification = ((s^(e_A) mod N_A)^(d_A) mod N_A)^(e_B) mod N_B
             = (s^(e_A × d_A) mod N_A)^(e_B) mod N_B
             = s^(e_B) mod N_B         [because e_A × d_A ≡ 1 (mod N_A)]
             = (M^(d_B))^(e_B) mod N_B
             = M^(d_B × e_B) mod N_B
             = M                        [because d_B × e_B ≡ 1 (mod φ(N_B))]
```

### **Euler's Totient Function**

For composite N = p × q (where p, q are distinct primes):

```
φ(N) = (p - 1) × (q - 1)
```

**Example:**
```
N = 143 = 11 × 13
φ(N) = (11 - 1) × (13 - 1) = 10 × 12 = 120
```

### **Modular Inverse**

The private exponent d is the modular inverse of e modulo φ(N):

```
(e × d) mod φ(N) = 1
```

**Example for Bob:**
```
e = 7, φ(N) = 120
Find d such that: (7 × d) mod 120 = 1
Solution: d = 103
Verification: (7 × 103) mod 120 = 721 mod 120 = 1 ✓
```

---

## **Requirements and Imports**

### **Python Version**
- Python 3.6 or higher

### **Required Libraries**

```python
from math import gcd
```

That's it! No external dependencies needed. The program uses only Python's built-in `math` module.

### **Installation**

Simply have Python 3.6+ installed:

```bash
python rsa_demo.py
```

---

## **How to Run**

### **Basic Usage**

Simply execute the script:

```bash
python rsa_demo.py
```

### **Expected Output**

```
======================================================================
Keys and parameters:
 Bob public key: (N=143, e=7)
 Bob phi(N) = 120, Bob private d = 103
 Alice public key: (N=39, e=5)
 Alice phi(N) = 24, Alice private d = 5

======================================================================
STEP 1: BOB SIGNS THE MESSAGE
======================================================================

Message: M = 3
Bob's Signature Formula: s = M^d mod N

s = 3^103 mod 143 = 16

✓ Bob creates signature: s = 16

======================================================================
STEP 2: BOB ENCRYPTS SIGNATURE UNDER ALICE'S PUBLIC KEY
======================================================================

Signature: s = 16
Bob Encrypts Formula: c = s^(e_A) mod N_A

c = 16^5 mod 39 = 22

✓ Bob encrypts signature: c = 22
→ Bob sends ciphertext to Alice: c = 22

======================================================================
STEP 3: ALICE DECRYPTS THE CIPHERTEXT
======================================================================

Ciphertext: c = 22
Alice Decrypts Formula: s' = c^d_A mod N_A

s' = 22^5 mod 39 = 16

✓ Alice recovers signature: s' = 16

======================================================================
STEP 4: ALICE VERIFIES THE SIGNATURE
======================================================================

Recovered Signature: s' = 16
Alice Verifies Formula: verification = (s')^(e_B) mod N_B

verification = 16^7 mod 143 = 3

Original Message: M = 3
Verification Result: 3

✅ Signature verification SUCCESSFUL: verification == M
   The message is authentic and came from Bob.

======================================================================
Summary of numeric values:
 M = 3
 s (computed by Bob) = 16
 c (sent to Alice) = 22
 s_recovered (after Alice decrypt) = 16
 verification = 3
======================================================================
```

---

## **Security Properties**

### **1. Authentication** 🔐
- Only Bob can create the signature with his private key
- When verification succeeds, Alice knows the message came from Bob
- No one else can create a valid signature

### **2. Non-Repudiation** ✋
- Bob cannot deny having signed the message
- Bob alone has his private key d_B
- The signature is proof of his involvement

### **3. Confidentiality** 🔒
- Only Alice can decrypt the signature
- Alice has the only private key d_A
- Encrypted signature c cannot be read by anyone else

### **4. Integrity** ✔️
- Any modification to the message or signature is detected
- If message is tampered with, verification will fail
- Even one bit change in M will produce wrong verification result

---

## **Program Functions**

### **`egcd(a, b)`**
```python
def egcd(a, b):
    """Extended Euclidean Algorithm"""
```
- Computes the greatest common divisor and coefficients
- Used to find the modular inverse d
- Returns (gcd, x, y) where a*x + b*y = gcd

### **`modinv(a, m)`**
```python
def modinv(a, m):
    """Compute modular inverse of a mod m"""
```
- Finds d such that (a × d) mod m = 1
- Used to calculate private exponent d from public exponent e
- Raises ValueError if modular inverse doesn't exist

### **`demo()`**
```python
def demo():
    """Main demonstration function"""
```
- Sets up pre-calculated RSA parameters
- Performs all four steps of sign-then-encrypt protocol
- Displays all calculations and results
- Verifies the signature

---

## **Step-by-Step Execution Flow**

```
START
  ↓
1. Initialize RSA Parameters
   - Bob: N=143, e=7, d=103, φ(N)=120
   - Alice: N=39, e=5, d=5, φ(N)=24
   - Message: M=3
  ↓
2. Bob Signs: s = 3^103 mod 143 = 16
  ↓
3. Bob Encrypts: c = 16^5 mod 39 = 22
  ↓
4. Transmit: c = 22 to Alice
  ↓
5. Alice Decrypts: s' = 22^5 mod 39 = 16
  ↓
6. Alice Verifies: verification = 16^7 mod 143 = 3
  ↓
7. Check: verification (3) == M (3) ?
   YES → ✅ Signature Valid
   NO  → ❌ Signature Invalid
  ↓
END
```

---

## **Complete Workflow Diagram**

```
BOB'S SIDE                          ALICE'S SIDE
═══════════════════════════════════════════════════════════════

Message: M = 3
        ↓
Sign with private key d_B
s = M^(d_B) mod N_B = 16
        ↓
Encrypt with Alice's public key e_A
c = s^(e_A) mod N_A = 22
        ↓
        ════════ SEND: c = 22 ════════>
                                        ↓
                              Decrypt with private key d_A
                              s' = c^(d_A) mod N_A = 16
                                        ↓
                              Verify with Bob's public key e_B
                              verification = (s')^(e_B) mod N_B = 3
                                        ↓
                              Check: verification == M ?
                              3 == 3? YES ✓
                                        ↓
                              Message Authenticated!
```

---

## **Example Values and Calculations**

### **Given Parameters**

| Parameter | Bob | Alice |
|-----------|-----|-------|
| Prime 1 (p) | 11 | 3 |
| Prime 2 (q) | 13 | 13 |
| Modulus N | 143 | 39 |
| φ(N) | 120 | 24 |
| Public Exponent e | 7 | 5 |
| Private Exponent d | 103 | 5 |

### **Message**
- M = 3

### **Calculations**

| Step | Formula | Calculation | Result |
|------|---------|-------------|--------|
| 1 | s = M^(d_B) mod N_B | 3^103 mod 143 | 16 |
| 2 | c = s^(e_A) mod N_A | 16^5 mod 39 | 22 |
| 3 | s' = c^(d_A) mod N_A | 22^5 mod 39 | 16 |
| 4 | V = (s')^(e_B) mod N_B | 16^7 mod 143 | 3 |
| 5 | Verify: V == M | 3 == 3 | ✅ PASS |

---

## **Key Concepts**

### **Public Key vs Private Key**

| Aspect | Public Key | Private Key |
|--------|-----------|------------|
| Contains | (N, e) | (N, d) |
| Shared | YES - Given to everyone | NO - Kept secret |
| Can Encrypt | YES | YES |
| Can Decrypt | NO | YES |
| Can Sign | NO | YES |
| Can Verify | YES | NO |

### **Why RSA Works**

```
1. One-way function: Easy to compute M^e, hard to invert without d
2. Trapdoor: Having d makes inversion easy
3. Public/Private split: e is public, d is secret
4. Mathematical property: (M^d)^e ≡ M (mod N)
```

---

## **Real-World Applications**

- **Email Signing**: Digital signatures verify email authenticity
- **Code Signing**: Software publishers sign code to prove origin
- **SSL/TLS**: Web certificates use RSA for secure communication
- **Banking**: Financial transactions use digital signatures
- **Government**: Official documents and records
- **Smart Cards**: Secure authentication and signing

---

## **Limitations of This Demo**

1. **Small Key Size**: 143 is tiny (real RSA uses 2048+ bit keys)
2. **Predictable**: With small N, attacks like factoring are trivial
3. **No Padding**: Real RSA uses padding schemes (OAEP, PKCS#1)
4. **Educational Only**: For learning purposes only
5. **Not Secure**: Never use for actual security applications

---

## **How to Make It More Secure**

For real-world use:
- Use **2048-bit or 4096-bit keys** instead of 8-bit keys
- Use **padding schemes** like OAEP or PKCS#1 v1.5
- Use **cryptographic libraries** (cryptography.io, PyCryptodome)
- Use **proper random number generation** for key generation
- Use **established protocols** like TLS instead of rolling your own

---

## **Author**

AKSHITHAPRIYADARSHINI

---

## **References**

- **RSA Original Paper**: Rivest, Shamir, and Adleman (1978)
- **NIST Guidelines**: https://nvlpubs.nist.gov/
- **RFC 3447**: PKCS #1: RSA Cryptography Specifications
- **Applied Cryptography**: Bruce Schneier

---

## **License**

This project is provided for educational purposes only.

---

## **Quick Start**

```bash
# Run the demo
python rsa_demo.py

# See the output showing:
# 1. Bob signs the message
# 2. Bob encrypts the signature
# 3. Alice decrypts the signature
# 4. Alice verifies it's authentic
# 5. Signature verification succeeds ✅
```

**That's it! Now you understand RSA digital signatures!** 🎓
