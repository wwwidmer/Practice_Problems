'''
  A palindrome number reads the same both ways. The largest palindrome number from
  the product of 2-digit numbers if 9009 = 91 * 99.
  Find the largest palindrome made from the product of 3-digit numbers.
'''

def main():
    pass

def palindromeCheck(number):
    if len(number) % 2 == 0:
        for x in (int(number/2)):
            if x == number[len(number)-x]:
                print x
            else:
                return False
        return True
