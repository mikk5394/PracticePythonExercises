
str = input('Type something to check if its palindrome or not: ')

reverse = str[::-1]

if str == reverse:
    print('Typed string is palindrome')
else:
    print('Typed string is NOT palindrome')