
distance = int(input('what is the distance beetween the speed cameras you passed in miles:'))# finds distance
speedc1 = input('what was the time when you passed the first speed camera:')#finds time in xy:ab formast
speedc2 = input('what was the time whee you passed the second speed camera:')#same as last line but for next camera

h1, m1 = map(int,speedc1.split(':'))#splits the minutes and hours and assigns them to seperate vairbales
h2, m2 = map(int,speedc2.split(':'))#same as last line
diff = (h2 * 60 + m2) - (h1 * 60 + m1)#a formula which puts them into minutes and subtracts first camera time from ssecond camera time

diffph = diff/60#puts minutes inot hours
mph = distance/diffph#calcs mph
print(f'your average speed is {mph}mph')#prints speed



