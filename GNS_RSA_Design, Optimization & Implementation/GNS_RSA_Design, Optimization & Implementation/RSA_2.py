# RSA Algorithm
 
# Everthing made from scratch
# Bignumber Package, Modular Multiplication and Exponentiation, Division Algorithm


# ================== Importing Libraries and Packages ================== #

from FFT import *
import random 
import json


# ================== Functions for Big Multiplication & Modular Multiplying ================== #

# ------------ Big Multiplication ------------ #
def big_mult(A,B):
    p = str(A)
    q = str(B)
    return fft_mult(p,q)
    # Time Complexity: O(nlogn)
    # Space Complexity: S(logn) 
# ------------ Modular Multiplication ------------ #
def multmod(a,b,mod):
    # Input Assertion: Integers a, b, and mod are defined
	# Invariant: (p*q)%n can be simplefied as ((p%n)*(q%n))%n
    p = ((a%mod)*(b%mod))%mod
	# Output Assertion: returns (a*b)%mod
    return p
    # Time Complexity: O(nlogn)
    # Space Complexity: S(1)

# ================== Functions for Prime Numbers, Modular Exponentiation ================== #

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

# ------------ Miller Rabin Prime Test ------------ #

def miller_rabin(num, rounds): #miller rabin better than fermat from 7-8 digit onwards
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # End up with trying about 300 values with Miller-Rabin before hitting a prime (on average).
    # When the value is non-prime, Miller-Rabin will detect it with probability 3/4 at each round, so the number of Miller-Rabin rounds you will run on average for a single non-prime value is 1+(1/4)+(1/16)+... = 4/3. For the 300 values, this means about 400 rounds of Miller-Rabin, regardless of what you choose for n.
    # So if you select n to be, e.g., 40, then the cost implied by n is less than 10% of the total computational cost
    # The probability that a random 1024-bit integer is prime is about 1/900.
    # If number is even, it's a composite number
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    if num % 5 == 0:
        return False
    r = 0
    exp = num - 1
    #INVARIANTs:	
    # 0 <= r <= n where n is the number of leftmost 0s before the first 1 in the binary representation of exp
    # for example, exp = 800 in binary is 1100100000. Here n is 5 since 5 leftmost 0s before the first 1
    # n is also the number of times exp can be divided by 2 until it becomes odd
    # m <= exp <= num-1 where exp goes down by half each time 
    # where m is the first odd value of exp whose binary representation is the same as the
    # original value of exp without the leftmost 0s. 
    # exp = 800, m would be 25 which in binary is 11001
    #https://stackoverflow.com/questions/21816610/how-many-times-can-an-even-number-be-divided-by-two-before-it-becomes-odd#:~:text=I.E.,before%20it%20becomes%20odd.
    
    while exp % 2 == 0:  #while exp is even, divide it by 2 and increase r by 1
        #precondition assertion: initially exp is even
        r = r + 1
        exp = exp//2
        #postcondition assertion: exp = m which is odd and r = n
        #INV:  0 <= i < rounds 
    for i in range(rounds):  #rounds is the number of times miller-rabin test is done to reduce error
        a = random.randrange(2, num - 1) #random number between 2 and num-2 both inclusive to be chosen as base every time the for loop runs
        x = expomod_efficient_itr(a, exp, num)     #modular exponentiation (a^exp) mod num
        if x!= 1:
            i = 0
            #INV: expomod_efficient_itr(a, exp, num) <= x != num - 1
            while x!= num - 1:
                if i == r - 1:
                    return False
                else:
                    i = i+1
                    x = expomod_efficient_itr(x, 2, num)
    return True 
    # Time Complexity Worst: O(round*(log(num))^3)
    # Time Complexity Average: O(round*(log(log(num))))
    # Space Complexity: S(1)
# ------------ Prime Number Test ------------ #

def isprime(n):
    # INput Assertion: n is defined
    # Output Assertion: True if n is a prime. False Otherwise
	return miller_rabin(n,40)
    # Time Complexity Worst: O(40*(log(n))^3)
    # Time Complexity Average: O(40*(log(log(n))))
    # Space Complexity: S(1)

# ================== Functions for Extended Euclidian GCD ================== #

def gcd(a,b):
    #Input Assertion: a and b are defined
    #Let a0 and b0 be the initial values of a and b respectively
	#INV: (gcd(a, b) = gcd(a0, b0)) AND (a > 0) AND (b >= 0)
	while(b):
		a, b = b, a%b  
    # returns gcd of a,b
	return a
    # Time Compleity: O(max(a,b))
    # Space Compleity: S(1)

# ================== Functions for Prime Numbers Generator ================== #

def prime_generate(a,b):
    # Input Assertion: integers a and b are defined 
	p = random.randint(a,b)
    # INV: Return p if it is a prime. Else p = p + 1 
	while(1>0):
		if isprime(p):
            # Output Assertion: p is a prime number
			return p
		else:
			p=p+1
    # Time Complexity: O(p) + O(40*(log(log(p)))) =  O(40*(log(log(p))))
    # Space Complexity: S(1)

# ================== Functions for Generating Random e ================== #

def random_e(phi_N, n):
    # Input Assertion: Integers phi_N and n are defined.
	e=random.randint(1,phi_N)
    # INV: Return e if gcd(e,phi_N) == 1 AND gcd(e, n) == 1. Else e = e + 1
	while (1>0):
		if gcd(e,phi_N) == 1 and gcd(e, n) == 1:
            # Output Assertions: e such that  gcd(e,phi_N) == 1 AND gcd(e, n) == 1.
			return e
		else:
			e = e+1
    # Time Complexity: O(max(e,phi_N)) + O(e) = O(n)
    # Space Complexity: S(1)

# ================== Functions for Modular Inverse of e Modulo phi_N => d ================== #

def modular_inverse(e, phi_N):  # modular inverse of e modulo phi_N
    # Input Assertion: Integers e and phi_N are defined.
    # We piched e randomly in the range 0 < e < phi_N.
    # Calculate the gcd of e and phi_N using Euclid's algorithm. 
    # If the gcd is not 1, we pick again. 
    # The number d falls out as a by-product of this computation.
    # Time Complexity = O(logn)
    # Space Complexity = S(1)
    phi_N0 = phi_N
    y = 0
    x = 1
    if phi_N == 1:
        return 0
    # INV: (e > 1) AND (e = x - e // phi_N * y) 
    while e > 1:
        quot = e // phi_N
        temp = phi_N
        phi_N = e % phi_N
        e = temp
        temp = y
        y = x - quot * y
        x = temp
    if x < 0:
        x = x + phi_N0
    # Output Assertion:  Return Modular Inverse of e Modulo phi_N
    return x
    # Time Complexity: O(log(e))
    # Space Complexity: S(1)


# ================== Encrypter and Implementing RSA ================== #

def RSA_encrypt(M):
	N_arr=[]
	# Converting Message to ASCII Numbers integers and do operations on them
	for i in range(0,len(M)):
		p = ord(M[i]) 
		N_arr.append(p)

	# Choosing Random Primes, p and q
	p = prime_generate(1,2**1024)
	q = prime_generate(1,2**1024)
	
	# Calculating N = p*q
	N = big_mult(p,q)
	
	#Calculating Phi(N)
	phi_N = big_mult(p-1,q-1)
	
	# Choosing Random e 
	e = random_e(phi_N, N)
	
	# Choosing Random d
	d = modular_inverse(e,phi_N)
	
	c = []
	# output encrypted message as elements of array
	for i in range(0, len(N_arr)):
		c.append(expomod_efficient_itr(N_arr[i], e, N))
	

	with open('keys.json', 'w+') as fp:
		json.dump({'c': c, 'e': e, 'd': d, 'N': N}, fp)

    # Time Complexity: O(len(M)) + O(len(M)) + O(log(e)) + O(max(e,phi_N)) + O(40*(log(log(p)))) + O(nlogn) + O(log(m)^2*log(n)) + ...
    #                = O(nlogn)
    # Space Complexity: S(1) + S(1) + S(1) + S(1) + S(logn)
    #                 = S(logn)



################################## ROUGH ################################## 



# ==================================== #

# M = "Nistha Singh"
# RSA_encrypt(M)

# =============================================================

# M = "Nistha Singh"
# c, e, d, N = RSA_encrypt(M)
# print(f"Encrypted Message: {c}, Public Key: {e}, Private Key: {d}, N: {N}")

# # =============================================================
# with open('keys.json', 'w+') as fp:
#     json.dump({'c': c, 'e': e, 'd': d, 'N': N}, fp)
# # ==============================================================
# ==============================================================

# def RSA_decrypt(c,d,N):
# 	M = []
# 	# decrypting the ASCII integers
# 	for i in range(0, len(c)):
# 		M.append(expomod_efficient_itr(c[i], d, N))
# 	M_decrypt=""
# 	#obtaining characters back from the decrypted ASCII integers
# 	for i in range(0,len(M)):
# 		M_decrypt = M_decrypt + chr(M[i])
# 	print(f"Decrypted Message: {M_decrypt}")


# RSA_decrypt(c,d,N)


