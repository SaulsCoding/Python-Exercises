#value1 = int(input('Input value : '))
#value2 = int(input('Input value : '))
#value3 = int(input('Input value : '))

#sums = value1 + value2 + value3
#average = sums /3

#return average
#print(average)

#fahrenheit = 81
#celsius = (fahrenheit  - 32) / 1.8
#print(str(celsius) + ' degrees celsius')

#user1 = int(input('Please enter value : '))
#user2 = int(input('Please enter value : '))

#largestvalue = max(user1, user2)
#print(largestvalue)

#sum(a, b, c):
    #if a == b or b == c or a == c:
        #sum = 0
    #else:
        #sum = a + b + c
    ##return sum

#print(sum(3, 2, 1))
#print(sum(2, 2, 1))
#print(sum(3, 2, 3))
#print(sum(1, 2, 1))








randomnumber = 10
win = False
turns = 0
while win == False:
    yourguess = input('Please enter a number from 0 to 10 : ')
    turns +=1
    if randomnumber == int(yourguess):
        print('Correct')
        win == True
        break
    else:
        print('Wrong')
        