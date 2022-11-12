'''
isPalindrome
Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). 
Otherwise it returns false.

Examples

isPalindrome('awesome') # false
isPalindrome('foobar') # false
isPalindrome('tacocat') # true
isPalindrome('amanaplanacanalpanama') # true
isPalindrome('amanaplanacanalpandemonium') # false
'''


def isPalindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True

    if string[0] != string[-1]:
        return False

    return isPalindrome(string[1:-1])


print(isPalindrome('awesome'))
print(isPalindrome('foobar'))
print(isPalindrome('tacocat'))
print(isPalindrome('amanaplanacanalpanama'))
print(isPalindrome('amanaplanacanalpandemonium'))
