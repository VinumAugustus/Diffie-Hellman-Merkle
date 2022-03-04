# Variables Used
Prime = 23  # p
Base = 5  # g

# Alice chooses a secret integer a = 4, then sends Bob A = g^a mod p
# A = 5^4 mod 23 = 4

aliceSecret = 4  # A
A = (Base ** aliceSecret) % Prime
print("Alice sends through a public channel: ", A)

# Bob chooses a secret integer b = 3, then sends Alice B = gb mod p
# B = 5^3 mod 23 = 10

bobSecret = 3  # B
B = (Base ** bobSecret) % Prime
print("Bob sends through a public channel: ", B, "\n")


# Alice computes s = B^A mod p
# s = 10^4 mod 23 = 18
aliceSharedSecret = (B ** aliceSecret) % Prime

# Bob computes s = A^B mod p
# s = 4^3 mod 23 = 18
bobSharedSecret = (A ** bobSecret) % Prime

print("Alice and Bob now share a secret.")
print("Alice shared secret = ", aliceSharedSecret)
print("Bob shared secret = ", bobSharedSecret)