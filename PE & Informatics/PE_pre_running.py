# Pre-running functions 1 - 25
import numpy as np
def fastFib(n, memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=fastFib(n-1, memo)+fastFib(n-2, memo)
        memo[n]=result
        return result

def prime(num):
    """Check if a number is prime.
    Args:
        num (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise."""
    if num==1:
        return False
    else:
        n=2
        while n<=int(np.sqrt(num)):
            if num%n==0:
                return False
            n+=1
        return True


def fd_prime(num):
    for _ in range(10001):
        num+=1
        while prime(num)==False:
            num+=1
    return num


def palindrome(num):
	return int(num != 0) and ((num % 10)*(10**int(np.log(num, 10)))+palin(num // 10))


def number_of_factors(num):
    fac=1
    for i in range(2,int(np.sqrt(num))+1):
        if num%i==0:
            fac+=1
    if np.sqrt(num)==int(np.sqrt(num)):
        return fac*2-1
    return fac*2

def triangular_seq(num):
    n=1
    seq=[]
    add=2
    while len(seq)<num:
        seq.append(n)
        n+=add
        add+=1
    return seq


def collatz_length(num):
    seq=[num]
    while num!=1:
        if num%2==0:
            num/=2
        else:
            num=3*num+1
        seq.append(num)
    return len(seq)

def collatz(num):
    seq=[num]
    while num!=1:
        if num%2==0:
            num/=2
        else:
            num=3*num+1
        seq.append(int(num))
    return seq


def paths(n):
    grid = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        grid[i][0] = 1
        grid[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[n][n]

def number_to_english(n: int) -> str:
    """ Translate an integer into words form
    param n: the integer to translate
    returns the English phrasing of :math:`n`
    number_to_english(127)
    'one hundred and twenty-seven'
    """
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= n < 20:
        return ones[n]
    elif 20 <= n <= 90 and n % 10 == 0:
        return tens[n // 10]
    elif 20 < n < 100:
        return tens[n // 10] + "-" + ones[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:
        return ones[n // 100] + " hundred"
    elif 100 < n < 1000:
        return ones[n // 100] + " hundred and " + number_to_english(n % 100)
    elif 1000 < n < 10000:
        pass
    elif n == 1000:
        return "one thousand"
    else:
        raise ValueError("unexpected input")

def solve(target):
    answer = 0
    for i in range(target):
        words = number_to_english(i + 1).replace(" ", "").replace("-", "")
        answer += len(words)
    return answer

def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

def amicable(num):
    factors=[]
    for i in range(1,num):
        if num/i==num//i:
            factors.append(i)
    if sum(factors)!=num:
        num1=sum(factors)
        factors1=[]
        for i in range(1,num1):
            if num1/i==num1//i:
                factors1.append(i)
        if sum(factors1)==num:
            return True
    return False

def length(n):
    return len(list(map(int, str(n))))

def is_factor(n,factor):
    if n%factor==0:
        return True
    return False


def pythagoreanTriplets(limits):
	c, m = 0, 2
	num=[]
	for i in range(1, 1000):
		num.append(i)
	val=[]
	for i in range(1000):
		val.append(0)
	while c < limits : 
		for n in range(1, m): 
			a=m*m-n*n 
			b=2*m*n 
			c=m*m+n*n 
			if c > limits: 
				break
			print('Triplet :', str(a)+',', str(b)+',', str(c))
			print(a+b+c)
			if a+b+c==1000:
				print('Special')
		m+=1