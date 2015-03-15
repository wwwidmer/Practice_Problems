'''
 Project Euler Problem 3:
 The prime factors of 13195 are 5,7,13,and 29
 What is the largest prime factor of! 600851475143?
'''
# Main..
def main():

    print "Prime Factors:\n"
    findPrime = raw_input("input: ")
    try:
        int(findPrime)
    except ValueError:
        print "Incorrect value...Try again..."

    factor_list = factors(int(findPrime))
    prime_factor_list = []
    for x in factor_list:
        if (isPrime(x)):
            prime_factor_list.append(x)
    print max(prime_factor_list)

# Function to find factors... This is a complex problem.
def factors(x):
    factors_list = []
    for n in range(1,int(x**0.5)+2):
        if x % n == 0:
            factors_list.append(n)
    return factors_list

# Determines if a number is a prime... The long way.
def isPrime(x):
    if x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    for n in range(5,int(x**0.5)+1,6):
        if x % n == 0 or x % (n+2) == 0:
            return False

    return True

if __name__ == '__main__':
    main()
