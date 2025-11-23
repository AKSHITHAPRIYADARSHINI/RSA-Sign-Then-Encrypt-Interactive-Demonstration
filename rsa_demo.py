# rsa_sign_encrypt_interactive.py
# Interactive RSA sign-then-encrypt demonstration with visible calculations
# Users can input their own RSA parameters and see step-by-step calculations

from math import gcd

def egcd(a, b):
    """Extended Euclidean Algorithm for finding modular inverse"""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    """Compute modular inverse of a mod m"""
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m

def get_positive_integer(prompt, min_val=1, max_val=None):
    """
    Get a positive integer input from user with validation
    
    Args:
        prompt: Message to display to user
        min_val: Minimum acceptable value (default: 1)
        max_val: Maximum acceptable value (default: None for no upper limit)
    
    Returns:
        Valid integer input from user
    """
    while True:
        try:
            value = input(prompt).strip()
            
            # Check if input is empty
            if not value:
                print(f"❌ Error: Input cannot be empty. Please enter a number.")
                continue
            
            # Check if input contains only digits (no alphabets or special chars)
            if not value.isdigit():
                print(f"❌ Error: Please enter only numbers (no letters or special characters).")
                continue
            
            num = int(value)
            
            # Check range
            if num < min_val:
                if max_val:
                    print(f"❌ Error: Value must be between {min_val} and {max_val}. You entered {num}.")
                else:
                    print(f"❌ Error: Value must be at least {min_val}. You entered {num}.")
                continue
            
            if max_val and num > max_val:
                print(f"❌ Error: Value must be between {min_val} and {max_val}. You entered {num}.")
                continue
            
            return num
        
        except Exception as e:
            print(f"❌ Error: Invalid input. Please try again.")

def get_rsa_parameters():
    """Collect RSA parameters from user with validation"""
    print("\n" + "="*70)
    print("RSA PARAMETERS INPUT - BOB (Signer)")
    print("="*70)
    
    while True:
        print("\nEnter Bob's RSA modulus (N = p × q)")
        print("Tip: Use small primes for demonstration (e.g., N = 143 = 11×13)")
        print("     Recommended: N between 10 and 1000 for testing")
        Bob_N = get_positive_integer("Bob's modulus N: ", min_val=2, max_val=100000)
        
        print(f"\nEnter Bob's Euler's totient φ(N) = (p-1)×(q-1)")
        print(f"For N = {Bob_N}, enter the corresponding φ(N)")
        print(f"Tip: φ(N) should be less than N and typically much smaller")
        print(f"     For N=143 (11×13): φ(N) = 10×12 = 120")
        Bob_phi = get_positive_integer(f"Bob's φ(N): ", min_val=1, max_val=Bob_N-1)
        
        # Check if φ(N) is large enough
        if Bob_phi < 3:
            print(f"❌ Error: φ(N) must be at least 3 for RSA to work. You entered {Bob_phi}.")
            print(f"   Please use larger prime factors.")
            continue
        
        print(f"\nEnter Bob's public exponent e")
        print(f"Constraint: 1 < e < φ(N) = {Bob_phi}, and gcd(e, φ(N)) = 1")
        print(f"Valid range: 2 to {Bob_phi-1}")
        print(f"Typical values: 3, 5, 7, 17, 65537")
        Bob_e = get_positive_integer(f"Bob's public exponent e: ", min_val=2, max_val=Bob_phi-1)
        
        # Check if gcd(e, phi) = 1
        if gcd(Bob_e, Bob_phi) != 1:
            print(f"❌ Error: gcd({Bob_e}, {Bob_phi}) ≠ 1. These are not coprime.")
            print(f"   Please choose a different e value.")
            continue
        
        # Check if modular inverse exists
        try:
            Bob_d = modinv(Bob_e, Bob_phi)
            print(f"✓ Bob's parameters are valid!")
            print(f"  Public exponent e = {Bob_e}")
            print(f"  Private exponent d = {Bob_d}")
            break
        except ValueError as e:
            print(f"❌ Error: {e}. Please try again.")
    
    print("\n" + "="*70)
    print("RSA PARAMETERS INPUT - ALICE (Recipient)")
    print("="*70)
    
    while True:
        print("\nEnter Alice's RSA modulus (N = p × q)")
        print("Tip: Use different small primes (e.g., N = 39 = 3×13)")
        print("     Recommended: N between 10 and 1000 for testing")
        Alice_N = get_positive_integer("Alice's modulus N: ", min_val=2, max_val=100000)
        
        print(f"\nEnter Alice's Euler's totient φ(N) = (p-1)×(q-1)")
        print(f"For N = {Alice_N}, enter the corresponding φ(N)")
        print(f"Tip: For N=39 (3×13): φ(N) = 2×12 = 24")
        Alice_phi = get_positive_integer(f"Alice's φ(N): ", min_val=1, max_val=Alice_N-1)
        
        # Check if φ(N) is large enough
        if Alice_phi < 3:
            print(f"❌ Error: φ(N) must be at least 3 for RSA to work. You entered {Alice_phi}.")
            print(f"   Please use larger prime factors.")
            continue
        
        print(f"\nEnter Alice's public exponent e")
        print(f"Constraint: 1 < e < φ(N) = {Alice_phi}, and gcd(e, φ(N)) = 1")
        print(f"Valid range: 2 to {Alice_phi-1}")
        print(f"Typical values: 3, 5, 7, 17, 65537")
        Alice_e = get_positive_integer(f"Alice's public exponent e: ", min_val=2, max_val=Alice_phi-1)
        
        # Check if gcd(e, phi) = 1
        if gcd(Alice_e, Alice_phi) != 1:
            print(f"❌ Error: gcd({Alice_e}, {Alice_phi}) ≠ 1. These are not coprime.")
            print(f"   Please choose a different e value.")
            continue
        
        # Check if modular inverse exists
        try:
            Alice_d = modinv(Alice_e, Alice_phi)
            print(f"✓ Alice's parameters are valid!")
            print(f"  Public exponent e = {Alice_e}")
            print(f"  Private exponent d = {Alice_d}")
            break
        except ValueError as e:
            print(f"❌ Error: {e}. Please try again.")
    
    print("\n" + "="*70)
    print("MESSAGE INPUT")
    print("="*70)
    print(f"\nEnter message M to be signed")
    print(f"Constraint: M must be less than Bob's modulus N = {Bob_N}")
    print(f"Valid range: 1 to {Bob_N-1}")
    M = get_positive_integer(f"Message M: ", min_val=1, max_val=Bob_N-1)
    
    return {
        'Bob_N': Bob_N,
        'Bob_phi': Bob_phi,
        'Bob_e': Bob_e,
        'Bob_d': Bob_d,
        'Alice_N': Alice_N,
        'Alice_phi': Alice_phi,
        'Alice_e': Alice_e,
        'Alice_d': Alice_d,
        'M': M
    }

def display_keys(params):
    """Display all keys and parameters"""
    print("\n" + "="*70)
    print("GENERATED KEYS AND PARAMETERS")
    print("="*70)
    print("\nBob's RSA Key Pair:")
    print(f"  Public Key:  (N = {params['Bob_N']}, e = {params['Bob_e']})")
    print(f"  Private Key: (N = {params['Bob_N']}, d = {params['Bob_d']})")
    print(f"  φ(N) = {params['Bob_phi']}")
    
    print("\nAlice's RSA Key Pair:")
    print(f"  Public Key:  (N = {params['Alice_N']}, e = {params['Alice_e']})")
    print(f"  Private Key: (N = {params['Alice_N']}, d = {params['Alice_d']})")
    print(f"  φ(N) = {params['Alice_phi']}")
    
    print(f"\nMessage to be signed: M = {params['M']}")

def demonstrate_signing(params):
    """Demonstrate Bob signing the message"""
    print("\n" + "="*70)
    print("STEP 1: BOB SIGNS THE MESSAGE")
    print("="*70)
    
    M = params['M']
    Bob_d = params['Bob_d']
    Bob_N = params['Bob_N']
    
    print(f"\nBob computes: s = M^d mod N")
    print(f"             s = {M}^{Bob_d} mod {Bob_N}")
    
    s = pow(M, Bob_d, Bob_N)
    
    print(f"\nCalculation:")
    print(f"  {M}^{Bob_d} mod {Bob_N} = {s}")
    print(f"\n✓ Signature generated: s = {s}")
    
    return s

def demonstrate_encryption(s, params):
    """Demonstrate Bob encrypting the signature under Alice's public key"""
    print("\n" + "="*70)
    print("STEP 2: BOB ENCRYPTS SIGNATURE UNDER ALICE'S PUBLIC KEY")
    print("="*70)
    
    Alice_e = params['Alice_e']
    Alice_N = params['Alice_N']
    
    print(f"\nBob encrypts: c = s^e_A mod Alice_N")
    print(f"              c = {s}^{Alice_e} mod {Alice_N}")
    
    c = pow(s, Alice_e, Alice_N)
    
    print(f"\nCalculation:")
    print(f"  {s}^{Alice_e} mod {Alice_N} = {c}")
    print(f"\n✓ Ciphertext generated: c = {c}")
    print(f"\n→ Bob sends ciphertext c = {c} to Alice")
    
    return c

def demonstrate_decryption(c, params):
    """Demonstrate Alice decrypting the ciphertext"""
    print("\n" + "="*70)
    print("STEP 3: ALICE DECRYPTS THE CIPHERTEXT")
    print("="*70)
    
    Alice_d = params['Alice_d']
    Alice_N = params['Alice_N']
    
    print(f"\nAlice decrypts: s' = c^d_A mod Alice_N")
    print(f"                s' = {c}^{Alice_d} mod {Alice_N}")
    
    s_recovered = pow(c, Alice_d, Alice_N)
    
    print(f"\nCalculation:")
    print(f"  {c}^{Alice_d} mod {Alice_N} = {s_recovered}")
    print(f"\n✓ Recovered signature: s' = {s_recovered}")
    
    return s_recovered

def demonstrate_verification(s_recovered, params):
    """Demonstrate Alice verifying the signature"""
    print("\n" + "="*70)
    print("STEP 4: ALICE VERIFIES THE SIGNATURE")
    print("="*70)
    
    M = params['M']
    Bob_e = params['Bob_e']
    Bob_N = params['Bob_N']
    
    print(f"\nAlice verifies: verification = (s')^e_B mod Bob_N")
    print(f"                verification = {s_recovered}^{Bob_e} mod {Bob_N}")
    
    verification = pow(s_recovered, Bob_e, Bob_N)
    
    print(f"\nCalculation:")
    print(f"  {s_recovered}^{Bob_e} mod {Bob_N} = {verification}")
    print(f"\n✓ Verification result: {verification}")
    
    print(f"\nComparing with original message:")
    print(f"  Original message M = {M}")
    print(f"  Verification result = {verification}")
    
    if verification == M:
        print(f"\n✅ SUCCESS! Signature verification passed!")
        print(f"   The message was authenticated and is from Bob.")
    else:
        print(f"\n❌ FAILED! Signature verification failed!")
        print(f"   The message was tampered with or signature is invalid.")
    
    return verification

def display_summary(params, s, c, s_recovered, verification):
    """Display complete summary of all values"""
    print("\n" + "="*70)
    print("COMPLETE SUMMARY")
    print("="*70)
    
    print("\nKey Values:")
    print(f"  Original Message (M)           = {params['M']}")
    print(f"  Bob's Signature (s)            = {s}")
    print(f"  Encrypted Signature (c)        = {c}")
    print(f"  Recovered Signature (s')       = {s_recovered}")
    print(f"  Verification Result            = {verification}")
    
    print("\nBob's RSA Parameters:")
    print(f"  Modulus N_B                    = {params['Bob_N']}")
    print(f"  Public Exponent e_B            = {params['Bob_e']}")
    print(f"  Private Exponent d_B           = {params['Bob_d']}")
    
    print("\nAlice's RSA Parameters:")
    print(f"  Modulus N_A                    = {params['Alice_N']}")
    print(f"  Public Exponent e_A            = {params['Alice_e']}")
    print(f"  Private Exponent d_A           = {params['Alice_d']}")
    
    print("\n" + "="*70)
    print("CRYPTOGRAPHIC OPERATIONS EXPLAINED")
    print("="*70)
    print("""
1. SIGNING (Bob uses his private key):
   - Bob signs message with: s = M^d_B mod N_B
   - Only Bob can create this signature (has private key d_B)
   - Provides AUTHENTICITY: proves Bob sent the message

2. ENCRYPTION (Bob uses Alice's public key):
   - Bob encrypts signature with: c = s^e_A mod N_A
   - Only Alice can decrypt (has private key d_A)
   - Provides CONFIDENTIALITY: only Alice can read the signature

3. TRANSMISSION:
   - Bob sends ciphertext c to Alice over the network

4. DECRYPTION (Alice uses her private key):
   - Alice decrypts: s' = c^d_A mod N_A
   - Recovers the original signature
   - Only Alice can do this (has private key d_A)

5. VERIFICATION (Alice uses Bob's public key):
   - Alice verifies: M' = (s')^e_B mod N_B
   - If M' == M: signature is authentic (came from Bob)
   - If M' ≠ M: signature is invalid (tampering detected)

SECURITY PROPERTIES:
- Authentication: Only Bob can create the signature
- Non-repudiation: Bob cannot deny signing the message
- Confidentiality: Only Alice can read the signature
- Integrity: Any tampering will be detected
    """)

def main():
    """Main demonstration flow"""
    print("\n" + "="*70)
    print("RSA SIGN-THEN-ENCRYPT INTERACTIVE DEMONSTRATION")
    print("="*70)
    print("""
This program demonstrates RSA digital signatures combined with encryption:
- Bob signs a message with his private key
- Bob encrypts the signature with Alice's public key
- Alice decrypts the signature with her private key
- Alice verifies the signature using Bob's public key

Each step shows the mathematical calculation so you can understand how it works.

RECOMMENDED STARTER VALUES:
  Bob's N:  143 (= 11 × 13)
  Bob's φ(N): 120
  Bob's e: 7
  Alice's N: 39 (= 3 × 13)
  Alice's φ(N): 24
  Alice's e: 5
  Message M: 3
    """)
    
    # Get parameters from user
    params = get_rsa_parameters()
    
    # Display all parameters
    display_keys(params)
    
    # Step 1: Sign
    s = demonstrate_signing(params)
    
    # Step 2: Encrypt
    c = demonstrate_encryption(s, params)
    
    # Step 3: Decrypt
    s_recovered = demonstrate_decryption(c, params)
    
    # Step 4: Verify
    verification = demonstrate_verification(s_recovered, params)
    
    # Summary
    display_summary(params, s, c, s_recovered, verification)
    
    print("\n" + "="*70)
    print("Demo Complete!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
