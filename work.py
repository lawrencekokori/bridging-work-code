
distance = int(input('what is the distance beetween the speed cameras you passed in miles:'))
speedc1 = input('what was the time when you passed the first speed camera:')
speedc2 = input('what was the time whee you passed the second speed camera:')

h1, m1 = map(int,speedc1.split(':'))
h2, m2 = map(int,speedc2.split(':'))
diff = (h2 * 60 + m2) - (h1 * 60 + m1)

diffph = diff/60
mph = distance/diffph
print(f'your average speed is {mph}mph')


