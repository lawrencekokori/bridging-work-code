print('this program checks if the work you input is a Palindromes')
word = input('enter your word:')
reversedw = word[::-1]
if reversedw.upper() == word.upper():
    print('this word is a Palindromes')
else:
    print('this word is not a Palindromes')