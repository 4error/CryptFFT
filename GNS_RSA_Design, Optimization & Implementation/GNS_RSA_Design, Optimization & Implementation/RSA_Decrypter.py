import json

def multmod(a,b,mod):
    # Input Assertion: Integers a, b, and mod are defined
	# Invariant: (p*q)%n can be simplefied as ((p%n)*(q%n))%n
    p = ((a%mod)*(b%mod))%mod
	# Output Assertion: returns (a*b)%mod
    return p
    # Time Complexity: O(nlogn)
    # Space Complexity: S(1)

# =====================================

# ------------ Modular Exponentiation ------------ #
def expomod_efficient_itr(a, n, p):
    # Input Assertion: Integers a,n,p are defined
    # Initialize result = 1
    res = 1
    # Update 'a' if 'a' >= p.  If 'a' is less then p then a % p will return 'a' itself
    a = a % p 
    # INV: (n0 >= n > 0) AND (a^n0)%p = res%p = ((a%p)^(n^(p-1)))%p
    while n > 0:
        # If n is odd, multiply 'a' with result
        if n % 2:
            res = multmod(res,a,p)
            n = n - 1
        else:
            a = multmod(a,a,p)
            # n is even now
            n = n//2
    # Output Assertion: (a^n)%p
    return res % p
    # Time Complexity: O(log(m)^2*log(n)).
    # Space Complexity: S(1)

# ====================================


def RSA_decrypt(fileName):
    #-------------------------------
    with open(fileName, 'r') as fp:
        keys_dict = json.load(fp)
    #-------------------------------
    c = keys_dict['c']
    e = keys_dict['e']
    d = keys_dict['d']
    N = keys_dict['N']
    #-------------------------------
    M = []
    # decrypting the ASCII integers
    for i in range(0, len(c)):
        M.append(expomod_efficient_itr(c[i], d, N))
    M_decrypt=""
    #obtaining characters back from the decrypted ASCII integers
    for i in range(0,len(M)):
        M_decrypt = M_decrypt + chr(M[i])
    print(f"Decrypted Message: {M_decrypt}")

    # Time Complexity: O(len(M)) + O(len(M)) + O(nlogn) + O(log(m)^2*log(n))
    #                = O(nlogn)
    # Space Complexity: S(1) + S(1) + S(1) + S(1) 
    #                 = S(1)

# =========================================

# with open('keys.json', 'r') as fp:
#     keys_dict = json.load(fp)

# c = keys_dict['c']
# e = keys_dict['e']
# d = keys_dict['d']
# N = keys_dict['N']
# RSA_decrypt("keys.json")