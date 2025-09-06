print('this program checks if the work you input is a Palindromes')#tells you what program does
word = input('enter your word:')#tells user  to enter a word and assigns it to a variable
reversedw = word[::-1]#reverses the word and assigns it to a new varible
if reversedw.upper() == word.upper():#checks if the reversed word in all caps is the same as the orignial word in all caps so the program is not case sensitive
    print('this word is a Palindromes')#prints this word isthe palindromes if last line is true
else:#is the outcome if line 4 isnt true
    print('this word is not a Palindromes')#if line 4 isnt true prints the oppsoite of line 5
