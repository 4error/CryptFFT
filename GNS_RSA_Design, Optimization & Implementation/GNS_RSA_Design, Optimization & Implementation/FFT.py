# RSA Algorithm


from cmath import exp
from math import pi

# A simple class to simulate n-th root of unity
# This class is by no means complete and is implemented merely for FFT and FPM algorithms
# Using concept of class as done in OOP Lectures
class NthRootOfUnity:
    def __init__(self, n, k = 1):
        # Assertions: n and k are defined
        self.k = k
        self.n = n

    def __pow__(self, other):
        # Assertions: other is defined
        if type(other) is int:
            n = NthRootOfUnity(self.n, self.k * other)
            return n

    def __eq__(self, other):
        # Assertions: other is defined
        if other == 1:
            return abs(self.n) == abs(self.k)

    def __mul__(self, other):
        # Assertions: other is defined
        return exp(2*1j*pi*self.k/self.n)*other

    def __repr__(self):
        # Assertions: other is defined
        return str(self.n) + "-th root of unity to the " + str(self.k)

    @property
    def th(self):
        # Assertions: other is defined
        return abs(self.n // self.k)

# =======================================================================================
# The Fast Fourier Transform Algorithm
# Input: A, An array of integers of size n representing a polynomial.
# Omega: a root of unity
# Output: [A(omega), A(omega^2), ..., A(omega^(n-1))]
# Complexity: O(n logn)
def FFT(A, omega):
    # Input Assertion: array A and integer omega are defined
    if omega == 1:
        return [sum(A)]
    o2 = omega**2
    # Assert: C1 array of even coeffecients
    C1 = FFT(A[0::2], o2)
    # Assert: C2 array of odd coeffecients
    C2 = FFT(A[1::2], o2)
    # Assert: C3 array of complex coeffecients
    C3 = [None]*omega.th
    # INV: (0 <= i < omega.th//2)  
    for i in range(omega.th//2):
        C3[i] = C1[i] + omega**i * C2[i]
        C3[i+omega.th//2] = C1[i] - omega**i * C2[i]
    # Output Assertion: Array C3 of complex coffecients
    return C3

# ============================================================================================
# The Fast Polynomial Multiplication Algorithm
# Input: A,B, two arrays of integers representing polynomials
# The length is in O(n)
# Output: Coefficient representation of AB
# Complexity: O(n logn)
def FPM(A,B):
    # Input Assertion: Array A and B are defined 
    n = 1<<(len(A)+len(B)-2).bit_length()
    o = NthRootOfUnity(n)
    AT = FFT(A, o)
    BT = FFT(B, o)
    # Assert: Array C of multiplication of coeffecients of Array A and B
    C = [AT[i]*BT[i] for i in range(n)]
    # nm = (len(A)+len(B)-1)
    # Assert: Array D of multiplication of coeffecients of Array A and B using complex roots and FFT
    D = [round((a/n).real) for a in FFT(C, o ** -1)]
    # INV: (len(D) > 0) AND (D[-1] == 0:) 
    while len(D) > 0 and D[-1] == 0:
        del D[-1]
    # Output Assertion: Array D of multiplication of coeffecients of Array A and B using complex roots and FFT.
    return D


def fft_mult(A,B):
	# Input Assertion: Integer A and B are defined.
	p_arr = []
	q_arr = []
    # Assert: Array of individual digits
	for i in range(0,len(A)):
		p_arr.append(ord(A[i])-48)
	for i in range(0,len(B)):
		q_arr.append(ord(B[i])-48)
	# Multiplying A*B using FFT such that it returns cofferient array
	r = FPM(p_arr,q_arr)
	# Reversing the Coffecient Array so to convert it back to integer 
	r_rev = r[::-1]
	final_sum = 0
    # Calculating sum of all coffecient 
	for i in range(len(r_rev)):
		final_sum = final_sum + (r_rev[i])*(10**i)
	# Output Assertion: Integer final_sum such that final_sum = A*B
	return int(final_sum)


################################## ROUGH ################################## 


