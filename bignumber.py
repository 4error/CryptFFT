

import math

# To handle big numbers in form of array
# Input as a string, output as an integer

#square and multiply algorithm

# Function for finding sum of larger numbers
# Translated from the SML done in Lecture 
def bigsum(a, b):
	# Input Assertion: strings a and b are defined
	# making sure length of b is larger.
	if (len(a) > len(b)):
		a, b = b, a

	# Take an empty list for storing result sum
	list_sum = ""

	# Reverse both of strings
	a = a[::-1]
	b = b[::-1]

	carry = 0
	# INV: for 0 <= i < len(a) AND current_sum = ((ord(a[i]) - 48) + ((ord(b[i]) - 48) + carry)) AND (initially carry = 0) 
	for i in range(len(a)):
		# Compute current_sum of current digits and carry
		current_sum = ((ord(a[i]) - 48) + ((ord(b[i]) - 48) + carry))
		list_sum = list_sum + chr(current_sum % 10 + 48)
		# Calculate carry for next step
		carry = current_sum//10

	# Add remaining digits of larger number
	# INV: len(a) <= i < len(b)  AND current_sum = ((ord(b[i]) - 48) + carry)
	for i in range(len(a), len(b)):
		current_sum = ((ord(b[i]) - 48) + carry)
		list_sum = list_sum + chr(current_sum % 10 + 48)
		carry = current_sum//10

	# Add remaining carry
	if (carry):
		list_sum = list_sum + chr(carry + 48)

	# reverse resultant list
	list_sum = list_sum[::-1]
	# Return sum of a and b as an integer
	return int(list_sum)


# checking if if a is smaller than b
def big_smaller(a, b):
	# Input Assertion: string a and b are assigned
	if (len(a) < len(b)):
		return True
	if (len(b) < len(a)):
		return False
	# INV: 0 <= i < len(a) AND (True if (a[i] < b[i]), False otherwise)
	for i in range(len(a)):
		if (a[i] < b[i]):
			return True
		elif (a[i] > b[i]):
			return False
	# Output Assertion: Return Bool True/False
	return False

# ================== Functions for Dividing ================== #
def div(x,y):
    # Input Assertion: Integers x, y are defined 
	if x == 0:
		return (0,0)
	else:
		(q,r) = div(x // 2, y)
		q1 = 2*q
		r1 = 2*r
		r2 = r1 + 1     
		if x % 2 == 1:
            # Output Assertion: Quotient of (x/y) and reminder of (x/y)
			if r2 < y:
				return (q1, r2)
			else:
				return (q1+1, r2-y)
		elif r1 < y:
			return (q1, r1)
		else:
			return (q1+1,r1-y)


# Function for finding difference of larger numbers
# input big num a as str, divisor b as int
# Translated from the SML done in Midterm
def bigsub(a, b):
	# Input Assertion: string a and b are defined
	# Before proceeding further, make sure a is not smaller
	if (big_smaller(a, b)):
		a, b = b, a

	# Take an empty string for storing result
	list_sub = ""

	# Reverse both of strings
	a = a[::-1]
	b = b[::-1]

	borrow = 0
	# INV: (0 <= i < len(b)) AND (sub = ((ord(a[i])-48) - (ord(b[i])-48) - borrow)) AND (initially borrow = 0)
	# Run loop till small string length
	# and subtract digit of a to b
	for i in range(len(b)):

		# compute difference of current digits

		sub = ((ord(a[i])-48) - (ord(b[i])-48) - borrow)

		# If subtraction is less then zero
		# we add then we add 10 into sub and
		# take borrow as 1 for calculating next step
		if (sub < 0):

			sub = sub + 10
			borrow = 1

		else:
			borrow = 0

		list_sub = list_sub + str(sub)

	# subtract remaining digits of larger number
	# INV: (len(b) <= i < len(a)) 
	for i in range(len(b), len(a)):

		sub = ((ord(a[i])-48) - borrow)

		# if the sub value is -ve, then make it positive
		if (sub < 0):
			sub = sub + 10
			borrow = 1
		else:
			borrow = 0

		list_sub = list_sub + str(sub)

	# reverse resultant string
	list_sub = list_sub[::-1]
	# Output Assertion: Difference of lists a and b 
	return int(list_sub)


# Multiplies str1 and str2, and prints result.
# Translated from the SML done in Assignment 3 
def bigmult(num1, num2):
	# Input Assertion: Strings num1 and num2 are defined.
	len1 = len(num1)
	len2 = len(num2)
	if len1 == 0 or len2 == 0:
		return "0"

	# Will keep the result number in reverse order
	result = [0] * (len1 + len2)
	
	# Below two indexes are used to find positions in result.
	i_n1 = 0
	i_n2 = 0

	# Go from right to left in num1
	# INV: (-1 < i <= len1 - 1) 
	for i in range(len1 - 1, -1, -1):
		carry = 0
		n1 = ord(num1[i]) - 48

		# To shift position to left after every multiplication of a digit in num2
		i_n2 = 0
		# Go from right to left in num2
		for j in range(len2 - 1, -1, -1):
			# Take current digit of second number
			n2 = ord(num2[j]) - 48
			# Multiply with current digit of first number and add result to previously stored result at current position.
			summ = n1 * n2 + result[i_n1 + i_n2] + carry

			# Carry for next iteration
			carry = summ // 10

			# Store result
			result[i_n1 + i_n2] = summ % 10

			i_n2 += 1

			# store carry in next cell
		if (carry > 0):
			result[i_n1 + i_n2] += carry

			# To shift position to left after every
			# multiplication of a digit in num1.
		i_n1 += 1

	# ignore '0's from the right
	i = len(result) - 1
	# INV: (len(result) - 1) AND (i >= 0) AND (result[i] == 0)
	while (i >= 0 and result[i] == 0):
		i = i - 1
	# If all were '0's - means either both or one of num1 or num2 were '0'
	if (i == -1):
		return "0"
	# Generate the result string
	s = ""
	# INV: i>=0 
	while (i >= 0):
		s += chr(result[i] + 48)
		i -= 1
	# Output Assertion: Integer s such that s = num1 * num2
	return int(s)


# # Divide str1 and int, and prints result.
# # Input number as a string, divisor as an int, output as an integer.
def bigdiv(number, divisor):
	# Input Assertion: string number and integer divisor are defined
	# As result can be very large, store it in string
	ans = ""
	
	# Find prefix of number that is larger than divisor.
	idx = 0
	temp = ord(number[idx]) - 48
	# INV: (temp < divisor) AND (temp = (temp * 10 + ord(number[idx + 1]) - 48))
	while (temp < divisor):
		temp = (temp * 10 + ord(number[idx + 1]) - 48)
		idx = idx + 1
	idx = idx + 1

	# Repeatedly divide divisor with temp.
	# After every division, update temp to include one more digit.
	# INV: (len(number)) > idx 
	while ((len(number)) > idx):
		
		# Store result in answer i.e. temp / divisor
		ans = ans + chr(math.floor(temp // divisor) + 48)
		
		# Take next digit of number
		temp = ((temp % divisor) * 10 + ord(number[idx]) - 48)
		idx = idx + 1

	ans = ans + chr(math.floor(temp // divisor) + 48)

	# If divisor is greater than number
	if (len(ans) == 0):
		return "0"


	
	# else return ans as integer
	# Output Assertion: Integer ans such that ans = number//divisor
	return int(ans)


################################## ROUGH ################################## 